import nacl.encoding
import nacl.signing

bobs_private_key = nacl.signing.SigningKey.generate()
bobs_public_key = bobs_private_key.verify_key

bobs_public_key_hex = bobs_public_key.encode(encoder=nacl.encoding.HexEncoder)

signed = bobs_private_key.sign((b'Send $37 to Alice'))

print(signed)
print(bobs_public_key_hex)


verify_key = nacl.signing.VerifyKey(bobs_public_key_hex, encoder=nacl.encoding.HexEncoder)

print(verify_key.verify(signed))