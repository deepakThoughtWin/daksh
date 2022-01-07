from slither_matrix.slither.core.variables.local_variable import LocalVariable
from slither_matrix.slither.core.variables.state_variable import StateVariable

from slither_matrix.slither.core.declarations.solidity_variables import SolidityVariable

from slither_matrix.slither.slithir.variables.temporary import TemporaryVariable
from slither_matrix.slither.slithir.variables.constant import Constant
from slither_matrix.slither.slithir.variables.reference import ReferenceVariable
from slither_matrix.slither.slithir.variables.tuple import TupleVariable


def is_valid_rvalue(v):
    return isinstance(
        v,
        (
            StateVariable,
            LocalVariable,
            TemporaryVariable,
            Constant,
            SolidityVariable,
            ReferenceVariable,
        ),
    )


def is_valid_lvalue(v):
    return isinstance(
        v,
        (
            StateVariable,
            LocalVariable,
            TemporaryVariable,
            ReferenceVariable,
            TupleVariable,
        ),
    )
