import hashlib

text = input("Enter a String ");

hash_object1 = hashlib. md5(text. encode())
hash_object2 = hashlib. sha256(text. encode())
hash_object3 = hashlib. sha1(text. encode())

md5_hash = hash_object1. hexdigest()
sha256_hash = hash_object2. hexdigest()
sha1_hash = hash_object3. hexdigest()

print("MD5 Hash    - ",md5_hash)
print("SHA256 Hash - ",sha256_hash)
print("SHA1 Hash   - ",sha1_hash)