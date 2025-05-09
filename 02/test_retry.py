from pytest import CaptureFixture
from retryp import retry_deco, check_str


def test_decorator_retries():
    attempts = []

    @retry_deco(3)
    def failing_function():
        attempts.append(1)
        raise RuntimeError("Test error")

    failing_function()
    assert len(attempts) == 3


def test_decorator_no_retry_on_expected():
    attempts = []

    @retry_deco(3, [ValueError])
    def specific_exception_function():
        attempts.append(1)
        raise ValueError("Test expected error")

    specific_exception_function()
    assert len(attempts) == 1


def test_output_log(capsys: CaptureFixture[str]):
    check_str(value=None)
    output = capsys.readouterr()
    expected_output = (
        'run "check_str" with positional args = (), keyword kwargs = '
        '{\'value\': None}, attempt = 1, exception = ValueError\n'
        'run "check_str" with positional args = (), keyword kwargs = '
        '{\'value\': None}, attempt = 2, exception = ValueError\n'
        'run "check_str" with positional args = (), keyword kwargs = '
        '{\'value\': None}, attempt = 3, exception = ValueError\n'
    )
    assert output.out == expected_output
