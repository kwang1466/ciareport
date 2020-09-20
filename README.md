# ciareport
change impact analysis report from CAST AIP database

# how to run
python ciareport.py -o "d:\Reports" -h localhost -p 2280 -s webgoat

NB: 
1. Should use the python.exe in CAST AIP installation folder, for example:
    C:\Program Files\CAST\8.3\ThirdParty\Python34\python.exe
2. By default, ciareport.py would only generate 5 excel report for Impacted Objets; This means you can modify the main in ciareport.py to do more things.
   
   Code to change if needed:
      # iterate changed_objs and generate the impact report for each object
    for count, single_obj in enumerate(changed_objs):
        # normally we only generate for 5 impact_object reort
        if count > 5:
            break
        local_id = single_obj.local_id
        # by default we only calculate 2 levels calling/called
        impact_objs = ciareport.get_impact_objs(local_id, 2, 2, 613)
        impact_headers = ['source_id', 'source_file', 'target_id', 'target_file', 'caller_name',
                          'caller_fullname', 'callee_name', 'callee_fullname',
                          'call_level', 'call_way']
        ciareport.generate_report(impact_headers, impact_objs,
                                  'impactObjs-{}.xls'.format(single_obj.full_name))


