import unittest
import json
import os
from app import app
import io

CURRENT_DIRECTORY = os.path.dirname(__file__)

# TODO replace template test with name of tool and add real tests
class TemplateTest(unittest.TestCase):
    '''
    Implements unit testing for the template.
    '''

    def setUp(self):
        self.app = app.test_client()

    def sample_test(self):
        self.assertTrue(True)