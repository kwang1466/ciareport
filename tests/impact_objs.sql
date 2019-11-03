select distinct 
t.IdSource, 
t.IdTarget, 
sourcekey.KeyNam as 调用对象名,
coalesce(sourceobject.FullName, ' ') as 调用对象全名,
targetkey.KeyNam as 被调用对象名, 
coalesce(targetobject.FullName, ' ') as 被调用对象全名,
t.InternalLevel as 调用层次, 
Case t.Ways  
WHEN '1' THEN '被调用'
WHEN '2' THEN '调用'
ELSE '其他' 
END 调用关系

from 
TmpOLIA t, 
webgoat_local.Keys sourcekey left outer join webgoat_local.ObjFulNam sourceObject on sourcekey.IdKey = sourceobject.IdObj ,
webgoat_local.Keys targetkey left outer join webgoat_local.ObjFulNam targetobject on targetkey.IdKey = targetobject.IdObj   

where 
targetkey.IdKey = t.IdTarget 
and sourcekey.IdKey=t.IdSource

order by t.InternalLevel;