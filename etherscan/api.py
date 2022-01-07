import json
import os
import sys

import requests as request

from config import ACTION, ADDRESS, API_KEY, MODULE
from slither_matrix.slither.__main__ import main
from utils.args_parser import manual_human_summary_args
from utils.versions import use_or_install
from utils.writer import write_code
from slither_matrix.api import slither_analisys
from manticore_matrix.api import manticore_analisys
from mithix_matrix.api import mithix_analisys
# from oyente_matrix.oyente.oyente import main as oyente_main
from oyente_matrix.oyente.api import oyente_analysis
# sys.path.append('/home/hp/projects/devesh/devesh_app/') 
# from mithix_matrix import MythixAnalysis

save_path = 'files'
filename = 'test1.sol'

def get_code(API_KEY,MODULE,ACTION,ADDRESS):
  #function for getting solidity code using address from etherscan
  response = request.get(f"https://api.etherscan.io/api?module={MODULE}&action={ACTION}&address={ADDRESS}&apikey={API_KEY}")
  json_data=response.json()
  result = json_data['result'][0]
  source_code=result['SourceCode']
  # MythixAnalysis(source_code)
  version=result['CompilerVersion']
  content_length = len(source_code)
  content_str = source_code[1:content_length-1]
  try:
    content=json.loads(content_str)
    source=content['sources']
    for contract_name in source:
      source_content=source[f'{contract_name}']
      content=source_content['content']  
      path=write_code(content, contract_name,save_path)
  except ValueError:
    content=source_code
    path=write_code(content,filename,save_path)
  if content  == '':
    print(f"API's response with address {ADDRESS} returns None")
    print('Please try different address ..')
    sys.exit(1)
  else:
    response={
      'content':content,
      'version':version,
      'path':path
    }
    # use_or_install(version,content)
  
    return response


#calling  etherscan api
response = get_code(API_KEY,MODULE,ACTION,ADDRESS)
#content parsed from response
# content=response['content']
path=response['path']

slither_result = slither_analisys('files/g.sol')
manticore_result = manticore_analisys('files/g.sol')
# mithix_result = mithix_analisys(path)
# oyente_result = oyente_analysis(path)

print("-------------------------------------------------------")
print("Slither - ",slither_result)
print("-------------------------------------------------------")
print("Manticore - ",manticore_result)
print("-------------------------------------------------------")
print("oyente - ",oyente_analysis('files/g.sol'))
print("---------------Mythx Test Started----------------------")
print("Mythx - ",mithix_analisys(path))



