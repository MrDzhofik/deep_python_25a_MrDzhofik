import functools


def retry_deco(retries=1, expected_exceptions=None):
    if expected_exceptions is None:
        expected_exceptions = []

    catch_exceptions = (RuntimeError, ValueError, TypeError, ZeroDivisionError,
                        KeyError, IndexError, NameError, SyntaxError)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    result = func(*args, **kwargs)
                    print(
                        f'run "{func.__name__}" with positional args = {args},'
                        f' keyword kwargs = {kwargs}, attempt = {attempt + 1},'
                        f' result = {result}'
                    )
                    return result
                except catch_exceptions as e:
                    print(
                        f'run "{func.__name__}" with positional args = {args},'
                        f' keyword kwargs = {kwargs}, attempt = {attempt + 1},'
                        f' exception = {e.__class__.__name__}'
                    )
                    if type(e) in expected_exceptions:
                        break
                    attempt += 1
            return None
        return wrapper
    return decorator


@retry_deco(3)
def add(a, b):
    return a + b


@retry_deco(3)
def check_str(value=None):
    if value is None:
        raise ValueError()
    return isinstance(value, str)


@retry_deco(2, [ValueError])
def check_int(value=None):
    if value is None:
        raise ValueError()
    return isinstance(value, int)


@retry_deco(1)
def zero():
    return 1/0
