#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    result = None
    try:
        result = fct(*args)
    except Exception as err:
        print("Exception:", err, file=stderr)
    finally:
        return result
