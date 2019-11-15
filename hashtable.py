#
#
#
#


def hash_init():
    hash = None
    return hash


def hash_add(hash, value):
    pass


def hash_len(hash):
    pass


def hash_remove(hash):
    pass


def hash_insert(hash, pos, value):
    pass


def hash_contains(hash, value):
    return False


h = hash_init()
hash_add(h, 4)
hash_add(h, 5)
hash_add(h, 64)
hash_add(h, 65)
hash_add(h, 128)
hash_add(h, 129)
hash_add(h, 3)
hash_add(h, 2)
hash_add(h, 1)
hash_add(h, 22)

print(hash_contains(h, 1))
print(hash_contains(h, 20))
print(hash_contains(h, 77))
print(hash_contains(h, 22))
