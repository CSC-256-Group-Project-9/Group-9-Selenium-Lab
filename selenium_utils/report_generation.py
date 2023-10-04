# Selenium Lab LLD 4.0

class Report:
    """
    Mentioned in LLD 4.1 "Output: New report object"
    """
    pass


def initialize_report() -> Report:
    """
    (LLD 4.1) Initializes a new report for capturing test results.
    :return: New report object
    """
    pass


def log_result(test_name: str, test_result: str, report: Report) -> None:
    """
    (LLD 4.2) Logs a test result into the provided report.
    :param test_name: Test Name
    :param test_result: Test Result (Pass/Fail)
    :param report: Report object
    """
    pass
