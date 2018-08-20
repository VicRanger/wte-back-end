import json;
import requests;
from urllib import parse;
class Http:
    @staticmethod
    def Get(_url,_data):
        data_urlencode = parse.urlencode(_data);
        # print(data_urlencode);
        req_url = _url+data_urlencode;
        req = requests.get(req_url,verify=False);
        res = json.dumps(req.json());
        return res;

# Http.Get('http://suggestion.baidu.com/su?',{'wd':'cmd','action':'opensearch','ie':'UTF-8'});