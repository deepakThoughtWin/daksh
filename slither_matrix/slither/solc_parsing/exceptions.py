from slither_matrix.slither.exceptions import SlitherException


class ParsingError(SlitherException):
    pass


class VariableNotFound(SlitherException):
    pass
