# Selenium Lab LLD 6.0

class ElementNotFoundException(Exception):
    """
    (LLD 6.1)
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class NavigationException(Exception):
    """
    (LLD 6.1)
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class DataReadException(Exception):
    """
    (LLD 6.1)
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


# (LLD 6.2) "Output: Customized error message/log"
# pretty sure this means to use print or some other form of logging within the function rather than a return value  - William
def handle_exception(exception_type: Exception, message: str) -> None:
    """
    (LLD 6.2) Handles specific exceptions, logging a user-friendly message.
    Outputs Customized error message/log.
    :param exception_type: Type of Exception
    :param message: Message to log
    """
    pass