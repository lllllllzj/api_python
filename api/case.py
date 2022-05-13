from api.common import read_yaml


class Case():
    def __init__(self, runner, name, steps, teardowns, filepath):
        self.name = name
        self.steps = steps
        self.runner = runner
        self.teardowns = teardowns
        self.filepath = filepath
        self.errors = []

    @classmethod
    def from_yml_path(cls, runner, yml_path):
        _case = read_yaml(yml_path)
        name = _case["name"]
        # setup = _case["setup"] if "setup" in _case else []
        _steps = _case["steps"] if "steps" in _case else []
        steps = _steps
        teardowns = _case["teardown"] if "teardown" in _case else []
        return cls(runner, name, steps, teardowns, yml_path)

    def _run(self, steps):
        i = 0
        for step in steps:
            name = step["name"]
            try:
                res_params = self.runner.run(step)
            except Exception as e:
                self.errors.append(f"步骤{i+1}：{name}失败，原因{e}")
            except AssertionError as e:
                self.errors.append(f"步骤{i+1}：{name}失败，原因{e}")

            i+=1

    def run(self):
        try:
            self._run(self.steps)
        except Exception as e:
            raise e
