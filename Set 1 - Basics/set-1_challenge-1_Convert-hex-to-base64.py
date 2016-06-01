import base64

# Need to use bytearray() function, for converting it into
# a collection of bytes
hexstring = bytearray(raw_input().decode('hex'))
base64string = base64.b64encode(hexstring)

print base64string    

# Hint: "Always operate on raw bytes, never encoded strings.
# Only use hex and base64 for pretty printing."
