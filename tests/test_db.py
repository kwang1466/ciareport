import pg8000

conn = pg8000.connect(host='localhost', port=2280, database='postgres', user="operator", password="CastAIP")
cursor = conn.cursor()
sql_str = '''select  idm.local_object_id,cos.object_id as central_object_id,cos.object_name,cos.module_name,cos.snapshot_name,cos.object_status, case when lower(cos.object_status) like 'deleted'then (select dtdv.techno_type_name from dss_techno_display_vw dtdv where dtdv.techno_type_id = cos.obejct_techno_type_id ) else ( select dot.object_type_name from  dss_object_types dot, dss_objects dob where dob.object_id = cos.object_id and dot.object_type_id = dob.object_type_id) end as OBJECT_TYPE from csv_objects_statuses cos left outer join csv_obj_mapping idm on cos.object_id=idm.central_object_id where snaphot_id = (select max(snapshot_id) from dss_snapshots) and object_is_artifact = 'Artifact'and object_status not like 'Unchanged';'''
cursor.execute('set search_path=webgoat_central')
cursor.execute(sql_str)
results = cursor.fetchall()
for row in results:
    print(row)
