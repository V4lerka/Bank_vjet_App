import pytest
from src.decorators import log
from time import time, ctime
import os

def test_log_except(capsys):
    x, y = 2, 0

    @log()
    def foo(a, b):
        return a / b

    with pytest.raises(Exception, match="division by zero"):
        foo(x, y)
        captured = capsys.readouterr()
        assert captured.out == f"Time: {ctime(time())}. Function foo error: division by zero. Inputs: {x}, {y}\n"


def test_log_success(capsys):
    x, y = 2, 1
    empty = {}

    @log()
    def foo(a, b):
        return a, b

    start = time()
    foo(x, y)
    end = time()
    captured = capsys.readouterr()
    assert captured.out == (f"Time: {ctime(time())}. Function foo is OK. "
                            f"Inputs: {x, y}, {empty}. "
                            f"Elapsed time: {end - start:.2f} sec. Result: {x, y}\n")

def test_log_file_creation():
        empty = {}
        x, y = 1, 2
        @log(filename="test_log")
        def foo(a, b):
            return a + b

        start = time()
        foo(x, y)
        end = time()

        assert os.path.exists("../test_log.txt"), "Log file was not created!"
        with open("../test_log.txt", 'r') as file:
            content = file.read()
            assert f"Time: {ctime(time())}. Function foo is OK. Inputs: {x, y}, {empty}. Elapsed time: {end - start:.2f} sec. Result: {x + y}\n" in content

def test_log_file_creation2():
    x, y = 2, 0

    @log(filename="test_log")
    def foo(a, b):
        return a / b

    with pytest.raises(Exception, match="division by zero"):
        foo(x, y)
        assert os.path.exists("../test_log.txt"), "Log file was not created!"
        with open("../test_log.txt", 'r') as file:
            content = file.read()
            assert f"Time: {ctime(time())}. Function foo error: division by zero. Inputs: {x}, {y}\n" in content