import os
import re

from .solc_select_version import install_artifacts, switch_global_version


def use_or_install(code_version,result):
  version=re.search(r"\d+\.\d+.\d+", code_version).group()
  result=switch_global_version(str(version))
  if result is not None:
    install_artifacts(result)
    return "Sucess"
