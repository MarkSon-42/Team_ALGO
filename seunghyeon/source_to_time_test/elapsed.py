import time


def elapsed(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rst = original_func(*args, **kwargs)
        print("function execution time: %0.9f sec" % (time.time() - start))

        return rst

    return wrapper


@elapsed
# !! 원하는 함수에 자유롭게 사용 !!
# def my_func(msg):
#     print("print '%s'" % msg)


# my_func("You need python")