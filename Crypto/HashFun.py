
import hashlib # deals with HASH function

text = b"Shalom"

hash = hashlib.md5(text)
print(hash.hexdigest())
print(hash.digest_size)

