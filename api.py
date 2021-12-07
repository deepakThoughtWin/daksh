import requests as request
import os
from config import API_KEY,MODULE,ACTION,ADDRESS
from solc_select_version import switch_global_version,install_artifacts
import re

save_path = 'files'
filename = 'test.sol'


def get_code(API_KEY,MODULE,ACTION,ADDRESS):
  response = request.get(f"https://api.etherscan.io/api?module={MODULE}&action={ACTION}&address={ADDRESS}&apikey={API_KEY}")
  json_data=response.json()
  result = json_data['result'][0]
  content=result['SourceCode']
  version=result['CompilerVersion']
  response={
    'content':content,
    'version':version
  }
  return response

def write_code(content,file_name,save_path):
  completeName = os.path.join(save_path, file_name)
  with open(completeName, "w") as file:
        file.write(str(content))
        return 'Success'

def use_or_install(version_string,result):
  version=re.search(r"\d+\.\d+.\d+", version_string).group()
  result=switch_global_version(str(version))
  if result is not None:
    install_artifacts(result)
  

response = get_code(API_KEY,MODULE,ACTION,ADDRESS)
result=response['content']
version_string=response['version']
use_or_install(version_string,result)




file = write_code(result,filename,save_path)
# from slither.__main__ import main
# main()
print(file)