import ctypes
dll = ctypes.CDLL('Test.dll')
rst = dll.TestTest()
print(rst)
size = -1
rst = ctypes.string_at(rst, size)
print(rst.decode('utf-8'))
