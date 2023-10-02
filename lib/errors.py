class InvalidSpanOperationException(Exception):
    """Exception raised when when a matrix operation would change the span"""

    def __init__(self) -> Exception:
        super().__init__("Not allowed, this could change the span!")
