from requests import Request, Session
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ApiRequest():
    def __init__(self, host, port=443):
        self.host = host
        self.port = port
        self.headers = None
        self.proto = "https"
        self.prefix = "/api/v4/shop"
        self.url = ""
        self.s = Session()

    def _url(self, url):
        # https://test.shopee.co.id/api/v4/shop/get_follow_prize_campaign?shopid=7432325
        self.url = f'{self.proto}://{self.host}:{self.port}{self.prefix}' \
                   f'{url}'


    def send(self, **kw):
        method = None if "method" not in kw else kw["method"]
        url = None if "url" not in kw else kw["url"]
        json = None if "json" not in kw else kw["json"]
        data = None
        params = None
        timeout = 30

        headers = None if "headers" not in kw else kw["headers"]
        cookies = None if "cookies" not in kw else kw["cookies"]
        # cookies = {"SPC_EC":"S3VRdld1RmZ3N05yMkFUcUf7NNhY3mrrEL5gQSwzYKM/p5301QxFlx9UbuP9VvvYsoI1SEB41Si7g1TbUe9V3SRoddVESfX4026Qn/gJTNzfJwtJagvKN6i1wtxCbyDa5LoobbguySsOQLZ/7IhgPg=="}

        self._url(url)
        print(self.url)

        r = Request(
            method=method.upper(),
            url=self.url,
            headers=headers,
            data=data,
            cookies=cookies,
            json=json,
            params=params,

        )
        prepped = r.prepare()
        res = self.s.send(prepped, verify=False, timeout=timeout)
        # print(res)
        print(res.text)
        return res

    def post(self, url, data=None, json=None, **kwargs):
        self._url(url)
        return self.s.post(self.url, data=data, json=json, **kwargs)

    def get(self, url, params=None, **kwargs):
        self._url(url)
        return self.s.get(self.url, params=None, **kwargs)

def get_api_client():
    # api_client = ApiRequest("test.shopee.co.id")
    api_client = ApiRequest("test.shopee.sg")
    return api_client

if __name__ == "__main__":
    t = ApiRequest("test.shopee.co.id")
    ret = t.get("get_template_v2", {"method":"GET"})
    print(ret.text)