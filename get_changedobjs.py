
from sqlalchemy import create_engine, MetaData, Table, Column, Sequence, Integer, \
                       String, select, text, TIMESTAMP, outerjoin, literal_column, union, \
                       delete, or_, and_, alias, inspect, join
from sqlalchemy.sql import func
from sqlalchemy.exc import NoSuchTableError
from collections import defaultdict
import subprocess
import tempfile
from sqlalchemy.schema import CreateSchema, DropSchema

user = 'operator'
password = 'CastAIP'
host = 'localhost'
port = 2280
database = 'postgres'
string = "postgresql+pg8000://%s:%s@%s:%d/%s" % (user, password, host, port, database)

engine = create_engine(string)

cursor = engine.raw_connection().cursor()

cursor.execute("SET search_path TO %s" % 'webgoat_local')

cursor.execute("SET CLIENT_ENCODING TO 'UTF8';")
