import functools


def retry_deco(retries=1, expected_exceptions=None):
    if expected_exceptions is None:
        expected_exceptions = []

    if isinstance(expected_exceptions, (tuple, list)):
        expected_exceptions = tuple(
            exc for exc in expected_exceptions
            if isinstance(exc, type) and issubclass(exc, BaseException)
        )

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                output = f'run "{func.__name__}" with positional'
                output += f'args = {args}, keyword kwargs = {kwargs},'
                output += f'attempt = {attempt + 1},'
                try:
                    result = func(*args, **kwargs)
                    output += f' result = {result}'
                    print(output)
                except expected_exceptions as e:
                    output += f' exception = {e.__class__.__name__}'
                    attempt += 1
                    print(output)
                    break
                except Exception as e:
                    output += f' exception = {e.__class__.__name__}'
                    attempt += 1
                    print(output)
        return wrapper
    return decorator


def add(a, b):
    return a + b


def check_str(value=None):
    if value is None:
        raise ValueError()
    return isinstance(value, str)


def check_int(value=None):
    if value is None:
        raise ValueError()
    return isinstance(value, int)


def zero():
    return 1/0
