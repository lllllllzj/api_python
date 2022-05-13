import yaml


def read_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def json_check(ori, expt, is_container_compare=False):
    if isinstance(ori, dict):
        for k, v in expt.items():
            assert k in ori, f"数据{ori},返回值中没有校验对象{k}"
            json_check(ori[k], v, is_container_compare)
    elif isinstance(ori, list):
        assert len(ori) >= len(expt), f"校验数组超高难度超出返回数组长度，期望值{expt}，实际值{ori}"
        for index, exptItem in enumerate(expt):
            json_check(ori[index], exptItem, is_container_compare)
    elif isinstance(ori, str):
        if is_container_compare:
            assert expt in ori, f"实际值{ori}不包含{expt}"
        else:
            assert ori == expt, f"实际值{ori}不等于{expt}"
    else:
        assert ori == expt, f"实际值{ori}不等于{expt}"