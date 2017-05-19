
from ctypes import *

#array_type = c_char_p * 4
#names = array_type()

#name = c_char_p(b"32323232321313213")
#name = b"testfsafsddfdfsfdewrewdlsjfdlkdsjflkajfdlkaj"


#names[0] = b"test1"
#names[1] = b"test2"
#names[2] = b"test3"
#names[3] = b"test4"

name = create_string_buffer(b'/0'*100)


api = CDLL('./arr2.so')

api.arrtest(byref(name))

#print(name.decode('utf-8'))

print(name.value)

#for t in names:
#    print (t.decode('utf-8'))
