# import sys
# sys.path.append('..')
import cast_upgrade_1_6_2
import unittest
import logging
from cast.application.test import run
from cast.application import create_postgres_engine

logging.root.setLevel(logging.DEBUG)


class TestIntegration(unittest.TestCase):

    def test1(self):

        run(kb_name='t19354_local', application_name='T19354', engine=create_postgres_engine())
        # run(kb_name='t19354_local', application_name='T19354')


if __name__ == "__main__":
    unittest.main()
