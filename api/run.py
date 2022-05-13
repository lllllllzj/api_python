
from pathlib import Path
from config import test_api

from api.case import Case
from api.result import CaseResult
from api.runner import Runner

class Run():
    def __init__(self):
        self._init()
        self.runner = Runner()

    def _init(self):
        pass

    def run_yml_case(self, yml_path):
        try:

            case = Case.from_yml_path(self.runner, yml_path)
            case.run()
            caseresult = CaseResult(str(yml_path), case.name, case.errors)
            caseresult.result()
        except Exception as e:
            raise e

    def get_run_path(self):
        return [f"/Users/zijian.liu/PycharmProjects/auto/cases/{v}" for v in test_api]
        # return [f"/Users/zijian.liu/PycharmProjects/auto/cases"]

    def run(self):
        yml_file = []
        run_paths = self.get_run_path()

        for run_path in run_paths:
            for file in Path(run_path).rglob('*.yml'):
                yml_file.append(file)
        # print(yml_file)
        for file in yml_file:
            self.run_yml_case(file)


if __name__ == "__main__":
    r = Run()
    r.run()
