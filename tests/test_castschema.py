import sys
sys.path.append('..')
import cast_upgrade_1_6_2
from cast.application import CastSchema,create_postgres_engine
import logging


engine = create_postgres_engine(user='operator',
                           password='CastAIP',
                           host='localhost',
                           port=2280)

central = CastSchema('webgoat_local', engine=engine)

# logging.info(central.get_caip_version())

# for o in central.get_extensions():
#     logging.info(o)

cursor = central.create_cursor()
function_call = 'pre_olia'

central._execute_function(cursor, function_call)

function_call2 = 'OLIA'
paramters = '2832, 2, 2, 0, 613'

central._execute_function(cursor, function_call2, paramters)

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

central._execute_raw_query(cursor, sql_str)

for o in cursor:
    logging.info(o)


# ret = central._execute_raw_query(cursor, 'select * from cdt_objects limit 100')
# logging.info(ret)
# for line in ret:
#     logging.info(str(line))


