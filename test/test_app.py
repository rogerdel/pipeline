from app import index, get_time
import time

def test_index():
    assert index() == "Hello world"

def test_time():
    assert get_time() == time.strftime("%H:%M:%S", time.localtime())