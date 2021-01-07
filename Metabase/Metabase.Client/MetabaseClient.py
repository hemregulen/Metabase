import requests
import json


class MetabaseClient:
    def __init__(self, metabase_url, username, password):
        self.metabase_url = metabase_url
        self.username = username
        self.password = password
        self.metabase_session = None


    def has_login(self):
        return self.metabase_session

    def get_metabase_session(self):
        headers = {
            'Content-Type': 'application/json',
        }

        data = '{"username": "%s", "password": "%s"}' % (self.username, self.password)
        response = requests.post('%s/api/session' % self.metabase_url, headers=headers, data=data)
        msg =  json.loads(response.text)
        return msg['id']

    def login(self, refresh_session=False):
        if refresh_session:
            self.metabase_session = None

        if not self.has_login():
            self.metabase_session = self.get_metabase_session()

    def call_metabase_api(self, question=0, start_date="", end_date="", params=[]):
            self.login()
            headers = {
                "Content-Type": "application/json",
                "X-Metabase-Session": self.metabase_session,
            }
        

            uri = self.metabase_url + "/api/card/"+question+"/query/json?parameters=[{\"type\":\"date/single\",\"target\":[\"variable\",[\"template_tag\",\"start_date\"]],\"value\":\""+ start_date+"\"},{\"type\":\"date/single\",\"target\":[\"variable\",[\"template_tag\",\"end_date\"]],\"value\":\""+ end_date +"\"}] "
            #uri = '%s/api/card/%s/query/json%s' % (self.metabase_url, question)
            #data = '{"startdate": "%s", "enddate": "%s"}' % (startdate, enddate)
            #, data=data
            response = requests.post(uri, headers=headers)
            if response.status_code == 401 and response.text == 'UnUnauthenticated':
                self.login(refresh_session=True)
                response = self.call_query()
            return response