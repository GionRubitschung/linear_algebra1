import numpy as np
from lib.errors import InvalidSpanOperationException


def add_row(
    X: np.ndarray, row_one: int, row_two: int, factor: int, matrix_type: str = "int"
) -> np.ndarray:
    """Operates an addition of two rows inside a given matrix `X`

    Args:
        X (np.ndarray): The given matrix
        row_one (int): Index of row one in `X`
        row_two (int): Index of row two in `X`
        factor (int): Factor applied to `X[row_two]` how much to the row `X[row_one]` adds,
            use negative values for substraction
        matrix_type (str, optional): Type of the matrix entries,
            for example `float64` or `int`. Defaults to `int`.

    Raises:
        InvalidSpanOperationException: If `row_one` equals `row_two`,
            the operation cannot be done

    Returns:
        np.ndarray: The edited matrix
    """
    if row_one == row_two:
        raise InvalidSpanOperationException()

    X = X.astype("float64")
    X[row_one] += factor * X[row_two]
    return X.astype(matrix_type)


def multiply_row(
    X: np.ndarray, row: int, factor: int, matrix_type: str = "int"
) -> np.ndarray:
    """Operates a multiplication of a row inside a given matrix `X`

    Args:
        X (np.ndarray): The given matrix
        row (int): Index of the row to multiply in `X`
        factor (int): Factor of how much to multiply
        matrix_type (str, optional): Type of the matrix entries,
            for example `float64` or `int`. Defaults to `int`.

    Raises:
        InvalidSpanOperationException: If `factor` equals `0`,
            the multiplication is invalid

    Returns:
        np.ndarray: The edited matrix
    """
    if factor == 0:
        raise InvalidSpanOperationException()
    X = X.astype("float64")
    X[row] = factor * X[row]
    return X.astype(matrix_type)


def swap_row(
    X: np.ndarray, row_one: int, row_two: int, matrix_type: str = "int"
) -> np.ndarray:
    """Operates a swap of row inside a given matrix `X`

    Args:
        X (np.ndarray): The given matrix
        row_one (int): Index of row 1
        row_two (int): Index of row 2
        matrix_type (str, optional): Type of the matrix entries,
            for example `float64` or `int`. Defaults to `int`.

    Returns:
        np.ndarray: The edited matrix
    """
    X = X.astype("float64")
    X[[row_one, row_two]] = X[[row_two, row_one]]
    return X.astype(matrix_type)
