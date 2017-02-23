import struct

# Functions for converting between IEEE754 binary 32/64-bit representations:
def float_to_binary(num):
    """
    Converts a python float to a 32-bit single precision IEEE754 binary string.
    """
    try:
        return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))
    except OverflowError:
        if str(num)[0] == '-':
            return float_to_binary(float('-inf'))
        else:
            return float_to_binary(float('inf'))


def binary_to_float(binstring):
    """
    Converts a 32-bit single precision binary string to a float.
    Raises a ValueError if the input is not 32 characters long.
    """
    if len(binstring) != 32:
        raise ValueError("Binary number must be 32 bits long")
    chars = "".join(chr(int(binstring[i:i + 8], 2)) for i in xrange(0, len(binstring), 8))
    return str(struct.unpack('!f', chars)[0])


def double_to_binary(num):
    """
    Converts a python float to a 64-bit double precision IEEE754 binary string.
    """
    return bin(struct.unpack('!Q', struct.pack('!d', num))[0])[2:].zfill(64)

def binary_to_double(binstring):
    """
    Converts a 64-bit double precision binary string to a float.
    Raises a ValueError if the input is not 64 characters long.
    """
    if len(binstring) != 64:
        raise ValueError("Binary number must be 64 bits long")
    chars = "".join(chr(int(binstring[i:i + 8], 2)) for i in xrange(0, len(binstring), 8))
    return str(struct.unpack('!d', chars)[0])

def hex_to_bin(hexstring):
    return bin(int(hexstring, 16))[2:].zfill(32)

def hex_to_bin64(hexstring):
    return bin(int(hexstring, 16))[2:].zfill(64)
if __name__ =="__main__":
    print hex(int(float_to_binary(-1.5),2))