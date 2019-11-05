import cast_upgrade_1_6_2
from cast.application import CastSchema,create_postgres_engine
import logging

class DBTool(object):
    """DBTool for create schema connection"""
    def __init__(self, schema_prefix, host='localhost', port=2280 ):
        super(DBTool, self).__init__()
        self.schema_prefix = schema_prefix
        self.engine = create_postgres_engine(user='operator',
                                password='CastAIP',
                                host=host,
                                port=port)

    def get_schema(self, schema_name):
        logging.info('get schema object')
        app_schema = CastSchema(self.schema_prefix + '_' + schema_name, 
                                engine=self.engine)
        return app_schema
