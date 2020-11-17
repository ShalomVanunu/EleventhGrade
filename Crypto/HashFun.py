
import hashlib



text = b"shalom"

hash = hashlib.md5(text)

print(hash.hexdigest())
print(hash.digest_size)

