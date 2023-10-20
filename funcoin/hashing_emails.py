from hashlib import sha256

secret_phrase = "bolognese"

def get_hash_with_secret_phrase(input_data, secret_phrase):
    combined = input_data + secret_phrase
    return sha256(combined.encode()).hexdigest()

email_dody = "Hi Bob, i guess you shoud be told about blockchain!" \
             " I have invested in Bitcoin and now i have 12.03 BTC."

print(get_hash_with_secret_phrase(email_dody, secret_phrase))