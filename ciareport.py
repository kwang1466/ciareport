import cast_upgrade_1_6_2
import logging
from db_util import *
import argparse
from packages import xlwt
from cast_objs import *


class CIAReport(object):
    """docstring for CIAReport"""
    def __init__(self, report_path, db_util):
        super(CIAReport, self).__init__()
        self.db_util = db_util
        self.report_path = report_path

    def get_changed_objs(self):
        logging.info('starting to get changed objects')
        sql_str = '''
                    select  idm.local_object_id,cos.object_id as central_object_id,cos.object_name,cos.module_name,cos.snapshot_name,cos.object_status,
                    case 
                     when lower(cos.object_status) like 'deleted'
                        then (select dtdv.techno_type_name from dss_techno_display_vw dtdv where dtdv.techno_type_id = cos.obejct_techno_type_id )
                    else ( select dot.object_type_name from  dss_object_types dot, dss_objects dob where dob.object_id = cos.object_id and dot.object_type_id = dob.object_type_id)
                    end as OBJECT_TYPE
                    from csv_objects_statuses cos left outer join csv_obj_mapping idm on cos.object_id=idm.central_object_id
                    where snaphot_id = (select max(snapshot_id) from dss_snapshots) and object_is_artifact = 'Artifact'
                    and object_status not like 'Unchanged';
                  '''
        sql_str = ''.join(sql_str.split('\n'))
        # logging.info(sql_str)
        central_schema = self.db_util.get_schema('central')
        cursor = central_schema.create_cursor()
        cursor.execute(sql_str)
        count = 0
        change_obj_list = list()
        for o in cursor:
            count += 1
            # logging.info(o)
            change_obj_list.append(ChangedObj(o[0], o[1], o[2], o[3], o[4], o[5], o[6]))

        logging.info('Found {} changed objects'.format(count))
        return change_obj_list
        
    def get_impact_objs(self, obj_id, called_lvl, calling_lvl, obj_type='613'):
        # try to get impact objects from local schema
        logging.info('Starting to get impacted objects')
        local_schema = self.db_util.get_schema('local')
        cursor = local_schema.create_cursor()
        function_call = 'pre_olia'

        local_schema._execute_function(cursor, function_call)

        function_call2 = 'OLIA'
        # function: olia in local schema
        # olia(p_idsource integer, p_levelcalled integer, 
        #      p_levelcalling integer, p_accknd integer, p_objtyp integer)
        paramters = '{},{},{},{},{}'.format(obj_id, called_lvl, calling_lvl, 0, obj_type)

        # paramters = '2832, 2, 2, 0, 613'
        local_schema._execute_function(cursor, function_call2, paramters)

        sql_str = '''
        select distinct 
        t.IdSource, 
        t.IdTarget, 
        sourcekey.KeyNam as caller_name,
        coalesce(sourceobject.FullName, ' ') as caller_fullname,
        targetkey.KeyNam as callee_name, 
        coalesce(targetobject.FullName, ' ') as callee_fullname,
        t.InternalLevel as call_level, 
        Case t.Ways  
        WHEN '1' THEN 'called'
        WHEN '2' THEN 'calling'
        ELSE 'others' 
        END call_relationships
        from 
        TmpOLIA t, 
        webgoat_local.Keys sourcekey left outer join webgoat_local.ObjFulNam sourceObject on sourcekey.IdKey = sourceobject.IdObj ,
        webgoat_local.Keys targetkey left outer join webgoat_local.ObjFulNam targetobject on targetkey.IdKey = targetobject.IdObj   
        where 
        targetkey.IdKey = t.IdTarget 
        and sourcekey.IdKey=t.IdSource
        order by t.InternalLevel;
        '''
        sql_str = ''.join(sql_str.split('\n'))
        cursor.execute(sql_str)
        count = 0
        impact_obj_list = list()
        for o in cursor:
            count += 1
            # logging.info(o)
            impact_obj_list.append(ImpactObj(o[0], o[1], o[2], o[3], o[4], o[5], o[6], o[7]))

        logging.info('Found {} impacted objects'.format(count))
        return impact_obj_list

    def generate_report(self, headers, data, report_name):
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Report')

        # Sheet header, first row
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        for col_num, val in enumerate(headers):
            ws.write(row_num, col_num, val, font_style)

        # Sheet body, remaining rows
        default_style = xlwt.XFStyle()
        for rowdata in data:
            row_num += 1
            for col, field in enumerate(headers):
                # logging.info(field)
                if hasattr(rowdata, field):
                    # logging.info('{}:{}'.format(col, getattr(rowdata, field)))
                    ws.write(row_num, col, getattr(rowdata, field), default_style)

        wb.save(self.report_path + '/' + report_name)
        logging.info("Genereated Report Done!")        


if __name__ == '__main__':
    logging.info('start generating report!')

    parser = argparse.ArgumentParser(add_help=False)
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-o', required=False, dest='report_path', default='./Reports', help='report location')
    requiredNamed.add_argument('-h', required=False, dest='host', default='localhost', help='database host name or ip')
    requiredNamed.add_argument('-p', required=False, dest='port', default=2280, help='database port')
    requiredNamed.add_argument('-s', required=False, dest='schema_prefix', default='webgoat', help='Schema Prefix Name')
    args = parser.parse_args()

    report_path = args.report_path
    host = args.host
    port = args.port
    schema_prefix = args.schema_prefix
    # use db tool to create engine and connect to database
    db_util = DBTool(schema_prefix, host, port)
    ciareport = CIAReport(report_path, db_util)
    # get changed objects from central schema
    changed_objs = ciareport.get_changed_objs()
    changed_headers = ['local_id', 'central_id', 'full_name',
                       'module', 'snapshot', 'status', 'obj_type']
    ciareport.generate_report(changed_headers, changed_objs, 'changedObjs.xls')

    # # get impact objects from local schema for specific object
    # impact_objs = ciareport.get_impact_objs(2832, 2, 2, 613)
    # # ciareport.generate_report( impact_objs, 'impactObjs.xls')
    # impact_headers = ['source_id', 'target_id', 'caller_name',
    #                   'caller_fullname', 'callee_name', 'callee_fullname',
    #                   'call_level', 'call_way']
    # ciareport.generate_report(impact_headers, impact_objs, 'impactObjs.xls')

    # iterate changed_objs and generate the impact report for each object
    for count, single_obj in enumerate(changed_objs):
        # normally we only generate for 5 impact_object reort
        if count > 5:
            break
        local_id = single_obj.local_id
        # by default we only calculate 2 levels calling/called
        impact_objs = ciareport.get_impact_objs(local_id, 2, 2, 613)
        # ciareport.generate_report( impact_objs, 'impactObjs.xls')
        impact_headers = ['source_id', 'target_id', 'caller_name',
                          'caller_fullname', 'callee_name', 'callee_fullname',
                          'call_level', 'call_way']
        ciareport.generate_report(impact_headers, impact_objs, 
                                  'impactObjs-{}.xls'.format(single_obj.full_name))