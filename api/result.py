from pathlib import Path

class CaseResult():
    def __init__(self, casepath, casename, errors=[]):
        self.casepath = Path(casepath).as_posix()
        self.casename = casename
        self.errors = errors

    def result(self):
        if not self.errors:
            print("case:{0}, result: Passed".format(self.casepath))
        else:
            print("case:{0}, result: Failed".format(self.casepath))
            for error in self.errors:
                print(error)