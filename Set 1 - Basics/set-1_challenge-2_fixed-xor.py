import base64

def xor_val(val1, val2):
        # it will return a string that has to be
        # converted back to hex for proper output.
        return ''.join([chr(x ^ y) for x,y in zip(val1, val2)])


if __name__ == "__main__":
    # Need to use bytearray() function, for converting it into
    # a collection of bytes
    value1 = bytearray('1c0111001f010100061a024b53535009181c'.decode('hex'))
    value2 = bytearray('686974207468652062756c6c277320657965'.decode('hex'))

    xor_value = xor_val(value1, value2)

    #print xor_value
    # then would require to convert the string back to hex
    print ''.join(x.encode('hex') for x in xor_value)

# Hint: "Always operate on raw bytes, never encoded strings.
# Only use hex and base64 for pretty printing."

