from hashlib import sha256

file = open("Power_icon.jfif", "rb")
hash = sha256(file.read()).hexdigest()
file.close()

print(f"The hash of my file is: {hash}")