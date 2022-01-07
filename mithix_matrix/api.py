from pythx import Client
import time
import os
import sys

from mithix_matrix.mythx_cli.analyze.command import analyze
 
# analyze(('files/test1.sol',))

def mithix_analisys(filename):
  mithix_result = analyze((filename,))
  return mithix_result


# SolidityJob('files/c.sol')
# c = Client(api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2MmI0NjYyYy00NzcwLTQxNWMtYjFhZS01OTAwZDllZDI2YmEiLCJpYXQiOjE2MzY0MDczMTcuOTczLCJpc3MiOiJNeXRoWCBBdXRoIFNlcnZpY2UiLCJleHAiOjE5NTE5ODMzMTcuOTcsInVzZXJJZCI6IjYxODk5NzhiMWZkMzkzMjdmMTFhMjk4NSJ9.jZr0Xg_5K6cZpbhspUWxZSNjVDUSPsglwwm1gE4Tkdo")

# def MythixAnalysis(**source):
#     # submit bytecode, source files, their AST and more!
#     resp = c.analyze(**source)

#     # wait for the analysis to finish
#     print(resp)
#     while not c.analysis_ready(resp.uuid):
#         time.sleep(1)

#     # have all your security report data at your fingertips
#     for issue in c.report(resp.uuid):
#         print(issue.swc_title or "Undefined", "-", issue.description_short)

#     # Output:
#     # Assert Violation - A reachable exception has been detected.
# import json
# source=os.path.join(sys.path[0], "Staking.json")
# with open((source), "r") as f:
#     source=json.load(f)
    
# MythixAnalysis(contract_name=source['contractName'], bytecode=source['deployedBytecode'], solc_version='0.5.6')
