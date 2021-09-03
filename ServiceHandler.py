"""
Implements a simple service using cx_Freeze.
See below for more information on what methods must be implemented and how they
are called.
"""

import threading
import os
import sys
import cx_Logging
import win32serviceutil, win32service
import win32api, win32con, win32profile, pywintypes
from contextlib import closing
import threading
import servicemanager

"""from NAMEAPP import CLASSAPP
OR 
"""


class Handler:

    # no parameters are permitted; all configuration should be placed in the
    # configuration file and handled in the Initialize() method
    def __init__(self):
        self.stopEvent = threading.Event()
        self.stopRequestedEvent = threading.Event()

    # called when the service is starting
    def initialize(self, configFileName):
        self.directory = os.path.dirname(sys.executable)
        cx_Logging.StartLogging(os.path.join(self.directory, "teste.log"), cx_Logging.DEBUG)
        #pass

    # called when the service is starting immediately after Initialize()
    # use this to perform the work of the service; don't forget to set or check
    # for the stop event or the service GUI will not respond to requests to
    # stop the service
    def run(self):
        cx_Logging.Debug("stdout=%r", sys.stdout)
        sys.stdout = open(os.path.join(self.directory, "stdout.log"), "a")
        sys.stderr = open(os.path.join(self.directory, "stderr.log"), "a")
        """PLACE CODE SERVICE HERE"""
        self.stopRequestedEvent.wait()
        self.stopEvent.set()

    # called when the service is being stopped by the service manager GUI
    def stop(self):
        self.stopRequestedEvent.set()
        self.stopEvent.wait()