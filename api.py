import os

import requests as request

from config import ACTION, ADDRESS, API_KEY, MODULE
from slither.__main__ import main
from utils.versions import use_or_install

save_path = 'files'
filename = 'test.sol'


def get_code(API_KEY,MODULE,ACTION,ADDRESS):
  #function for getting solidity code using address from etherscan
  response = request.get(f"https://api.etherscan.io/api?module={MODULE}&action={ACTION}&address={ADDRESS}&apikey={API_KEY}")
  json_data=response.json()
  result = json_data['result'][0]
  content=result['SourceCode']
  version=result['CompilerVersion']
  response={
    'content':content,
    'version':version
  }
  use_or_install(version,content)
  return response

def write_code(content,file_name,save_path):
  #function for writing code into file
  completeName = os.path.join(save_path, file_name)
  with open(completeName, "w") as file:
        file.write(str(content))
        return 'Success'


  
#calling  etherscan api
response = get_code(API_KEY,MODULE,ACTION,ADDRESS)
#content parsed from response
content=response['content']
#write api response in file
file = write_code(content,filename,save_path)

#Run analyzer(updated slithir=> human_summary,__main__.py)
analyzer=main()
print(analyzer)
