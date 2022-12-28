""" this module aimed to laoding and transform the data from the GBFS flux. 
GBFS (General Bikeshare Feed Specification) is a standard data format used to publish information about bikeshare systems, such as availability and location of bikes and stations. 
"""

import pandas as pd
import json
import urllib
import datetime as dt
import time
import os


class GbfsLoader():
    """
    This class aimed to provide an object to load the data of a gbfs flux
    """
    def __init__(self, url_status, url_information):
        """
        initiate the loader with the url of status of the gbfs flux
        """
        self.url_status = url_status
        self.url_information = url_information

    

