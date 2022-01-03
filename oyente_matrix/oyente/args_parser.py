import argparse

def manual_args(filename):
  filename_with_args=argparse.Namespace(allow_paths=None, assertion=False, bytecode=False, compilation_error=False, debug=False, depth_limit=None, evm=False, gas_limit=None, generate_test_cases=False, global_timeout=None, globalblockchain=False, json=False, loop_limit=None, parallel=False, paths=False, remap=None, remote_URL=None, report=False, root_path=None, source='greeter.sol', standard_json=False, standard_json_output=False, state=False, timeout=None, verbose=False, web=False)

  
  return filename_with_args