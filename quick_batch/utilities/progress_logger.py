import functools
import traceback


def log_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"FAILURE: {func_name} failed: {e}")
            traceback.print_exc()
        else:
            print(f"SUCCESS: {func_name} succeeded")
            return result
    return wrapper


def decorate_methods(decorator):
    def decorate(obj):
        if isinstance(obj, type):
            # Decorate class methods
            for name, method in vars(obj).items():
                if callable(method):
                    setattr(obj, name, decorator(method))
            return obj
        else:
            # Decorate standalone functions
            return decorator(obj)
    return decorate
