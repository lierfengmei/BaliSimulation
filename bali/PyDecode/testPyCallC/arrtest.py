
from ctypes import *

array_type = c_char_p * 4
names = array_type()

names[0] = b"0"
names[1] = b"test2fdasfa"
names[2] = b"test3dfafsj"
names[3] = b"test4fdasfafsasfa"

api = CDLL('./arr.so')

api.arrtest(names,4)



name2 = c_char(100)






for t in names:
    print (t.decode('utf-8'))
