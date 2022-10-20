from requests import request
from requests.compat import urljoin, quote_plus

class AcuApi(object):
    def __init_(self):
        api_key = 'jOYXa4tVzJliNq0hn2gkSEwuazYNWMbX' # ToDo move value to env
        api_url = 'http://dataservice.accuweather.com/'
    
    def get_location_key(self, keyword=None):
        url_loc = 'locations/v1/cities/search'
        url = urljoin(self.api_url, url_loc)
        payload = {'apikey':self.api_key,'q': keyword}
        result = request.get(url, params=payload)
        if result.status_code == 200:
            data = result.json()
            return data["Key"]
        else:
            return None
    def current_condition(self,keyword=None,loc_key=None):
        cu_url = 'currentconditions/v1'
        if not loc_key:
            loc_key = self.get_location_key(keyword)
        if loc_key:
            url = urljoin(self.api_url,cu_url,  quote_plus(keyword), self.api_key)
        payload = {'apikey':self.api_key}
        result = request.get(url, params=payload)
        if result.status_code == 200:
            data = result.json()
            return data["Key"]
        else:
            return None
