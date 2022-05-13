
from api.common import json_check
from api.request import get_api_client

class CheckMixin():
    def _json_check(self, obj, exptResponse):
        if isinstance(exptResponse["json"], dict):
            json_check(obj, exptResponse["json"], )
        else:
            assert False, f"{exptResponse}非json结构"

    def _text_check(self, text, exptResponse):
        assert str(exptResponse["text"]) in text, f"期望{exptResponse}，实际{text}"

    def _json_text_check(self, response, exptResponse):
        if "json" in exptResponse:
            self._json_check(self.get_response_json(response), exptResponse)
        elif "text" in exptResponse:
            self._text_check(self.get_response_json(response), exptResponse)

class RunnerMixin():
    def run(self, step):
        # res_param = {}
        assert "request" in step
        r = self._run(step["request"])
        if "response" in step:
            self._response_compare(r, step["response"])


class ApiRunner(CheckMixin, RunnerMixin):
    def __init__(self):
        self.client = get_api_client()

    def _run(self, request):
        return self.client.send(**request)

    def get_response_json(self, response):
        try:
            return response.json()
        except:
            raise Exception(f"非json结构")

    def get_response_text(self, response):
        return response.text

    def _compare_status_code(self, status_code, expt_status_code, text):
        if isinstance(expt_status_code, int):
            assert status_code == expt_status_code, f"状态码不一致，期望{expt_status_code}，实际{status_code}"
        elif isinstance(expt_status_code, str):
            ok = False
            for code in expt_status_code.split(","):
                if int(code) == status_code:
                    ok = True
                    break
            assert ok, f"状态码不一致，期望{expt_status_code}，实际{status_code}，实体{text}"

    def _response_compare(self, response, exptResponse):
        if "status_code" in exptResponse:
            self._compare_status_code(response.status_code, exptResponse["status_code"], response.text)

        self._json_text_check(response, exptResponse)



class Runner():

    def __init__(self):
        self.hanlder = ApiRunner()

    def run(self, step):
        res_param = {}
        for k in step:
            if k == "name":
                continue
            res_param = self.hanlder.run(step[k])
        return res_param