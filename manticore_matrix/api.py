import os

from utils.symbolic_file import test_symbolic_file

save_path = 'files'
filename = 'test1.sol'

completeName = os.path.join(save_path, filename)

test_symbolic_file(completeName)
