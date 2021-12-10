import os
import re

from .solc_select_version import install_artifacts, switch_global_version,current_version


def use_or_install(code_version,result):
  version=re.search(r"\d+\.\d+.\d+", code_version).group()
  sys_version=current_version()
  if sys_version ==version:
    print(f'{version} found in system')
  else:
    print(f'{version} required')
    result=switch_global_version(str(version))
    if result is not None:
      installation=install_artifacts(result)
      return "Sucess"
  
    
    
    
