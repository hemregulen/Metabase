import jwt
import requests
import json
import psycopg2
import datetime
import uuid

from datetime import datetime
from MetabaseClient import MetabaseClient
from datetime import date, timedelta


class CallModule:

    def __init__(self):
        self.matabase = matabase
        self.sqlconnection = sqlconnection

    def execute():
        m_client = MetabaseClient(metabase_url=[metabaseurl], username=[metabaseusername], password=[metabasepassword])
        e = m_client.call_metabase_api(281,"2020-09-30", "2020-09-30")
        jsondata = json.loads(e.text)
        try:
            for value in jsondata:
                try:
                   print(value[0]);

                except (Exception, psycopg2.DatabaseError) as error :
                    if(connection):
                        print("Failed this data : "+value[0], error)
        except (Exception, psycopg2.DatabaseError) as error :
                    if(connection):
                        print("Failed", error)
