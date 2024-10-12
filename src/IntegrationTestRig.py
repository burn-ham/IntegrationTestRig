import os
import subprocess
import time
import unittest

class IntegrationTestRig(unittest.TestCase):
    seconds_to_wait = 5
    resource_file = None

    @classmethod
    def setUpClass(cls):
        project_root = os.path.dirname(os.path.dirname(__file__))
        resource_file = os.path.join(project_root, cls.resource_file)
        cls.service_process = subprocess.Popen(["python", resource_file])
        time.sleep(cls.seconds_to_wait)

    @classmethod
    def tearDownClass(cls):
        cls.service_process.terminate()
        cls.service_process.wait()