from manticore_matrix.manticore.__main__ import main


def manticore_analisys(filename):
  manticore_result = main(filename)
  return manticore_result
 

# print(a)

# from manticore.ethereum import ManticoreEVM, ABI
# m = ManticoreEVM()
# #And now make the contract account to analyze
# # with open("files/Staking.sol") as f:
# #     source_code = f.read()
# source_code = '''
#   pragma solidity >=0.7.0 <0.9.0;


# contract Test {

#    uint public test1; 
#     constructor() public {
#         test1 =10;
#     }
# }
# '''

# #Initialize user and contracts
# user_account = m.create_account(balance=10000)
# contract_account = m.solidity_create_contract(source_code, owner=user_account, balance=0,contract_name='Test')
# # contract_account.set(12345, value=100)
# print(contract_account)
# # value=m.make_symbolic_value(),
# # contract_account.f(value)
# # m.transaction(
# #     caller=user_account,
# #     address=contract_account,
# #     data=m.make_symbolic_buffer(32),
# # )

# # print(f"[+] There are {m.count_terminated_states()} reverted states now")
# # print(f"[+] There are {m.count_busy_states()} alive states now")
# # # for state_id in m.running_state_ids:
# # #     print(m.report(state_id))

# # print(f"[+] Global coverage: {contract_account.address:x}")
# # print(m.global_coverage(contract_account))

# # m.finalize()