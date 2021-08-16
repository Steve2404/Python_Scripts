import struct

int_var = 4
buf = struct.pack("!i 138s" ,int_var, "bonjour")
int_var2 = struct.unpack("!i 138s", buf)[0]
print(int_var2)