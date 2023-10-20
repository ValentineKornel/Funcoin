import hashlib

input_bytes = b"Backpack "
output = hashlib.sha256(input_bytes)

print(output.hexdigest())