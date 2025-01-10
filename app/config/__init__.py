import json
import os

cwd = os.getcwd()
path = os.path.join(cwd,"app", "config","headers.json")
with open(path) as config_file:
    data = json.load(config_file)
    content_type = data['headers']['Content-Type']
    token = data['headers']['Token']
    database_tmo = data['headers']['Database_TMO']
    database_monachil = data['headers']['Database_Monachil']
    user_agent = data['headers']['User-Agent']
    url = data['headers']['Url']