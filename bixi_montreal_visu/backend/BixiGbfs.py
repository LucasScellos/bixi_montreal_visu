
import pandas as pd
import json
import urllib
import datetime as dt
import time
import os
from backend.GbfsLaoder import GbfsLoader

class BixiGbfsLoader(GbfsLoader):
    """
    This class is inherited from GbfsLoader with the function with the correct url from 
    """
    def __init__():
        super.__init__(
            url_status="https://gbfs.velobixi.com/gbfs/en/station_status.json",
            url_information="https://gbfs.velobixi.com/gbfs/en/station_information.json"
        )

    def query_station_status(self):
        """
        this function aims to provide the data from the station status
        """
        with urllib.request.urlopen(self.url_status) as data_url:
            self.data_status = json.loads(data_url.read().decode())

    def data_status_cleaning(self):
            """
            This function clean the data of the json file and convert it in a Pandas Dataframe 
            
            """
            df = pd.DataFrame(self.data_status['data']['stations'])
            # drop inactive stations
            df = df[df.is_renting==1]
            df = df[df.is_returning==1]
            df = df.drop_duplicates(['station_id','last_reported'])
            df.last_reported = df.last_reported.map(lambda x: dt.datetime.utcfromtimestamp(x))
            df['time'] = self.data_status['last_updated']
            df.time = df.time.map(lambda x: dt.datetime.utcfromtimestamp(x))
            df = df.set_index('time')
            df.index = df.index.tz_localize('UTC')
            df = pd.pivot_table(df,columns='station_id',index='time',values='num_bikes_available')
            return df
