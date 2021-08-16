import struct

var = 8
buf = struct.pack("!i", var)
var2 = struct.unpack("!i", buf)[0]
print(buf)
print(var2)