import inspect

from indentedlogs.utils import func_in_frame_info


def test_func_in_frame_info():
    def foo():
        return inspect.stack()

    stack = foo()
    func = func_in_frame_info(stack[0])
    assert func is foo
