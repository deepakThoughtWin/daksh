from oyente_matrix.oyente.oyente import main
# from etherscan.api import path
# main('contract.sol')


def oyente_analysis(filename):
  oyente_result = main(filename)
  return oyente_result

# oyente_analysis('files/test1.sol')

