import logging
import pg8000


class DBTool(object):
    """DBTool for create schema connection"""

    def __init__(self, schema_prefix, host='localhost', port=2280):
        super(DBTool, self).__init__()
        self.schema_prefix = schema_prefix
        conn = pg8000.connect(host=host, port=port, database='postgres',
                              user="operator", password="CastAIP")
        self.cursor = conn.cursor()

    def get_schema(self, schema_name):
        logging.info('get schema object')
        # print('get schema object')

        # print("SET search_path TO {}_{}".format(self.schema_prefix, schema_name))
        self.cursor.execute("SET search_path TO {}_{}".format(self.schema_prefix, schema_name))
        self.cursor.execute("SET CLIENT_ENCODING TO 'UTF8';")
        return self.cursor
