#
#
#
#

def list_init():
    return malloc(2)


def list_append(l, v):
    node = malloc(3)
    write(node, v)
    first = read_addr(l)
    if first == 0:
        write_addr(l, node)
    else:
        cur = first
        while cur != 0:
            prev = cur
            cur = read_addr(cur+1)
        write_addr(prev+1, node)


def list_len(l):
    pass


def list_remove(l):
    pass


def list_insert(l, pos, v):
    pass


def list_contains(l, v):
    return False


l = list_init()
list_append(l, 4)
list_append(l, 5)
list_append(l, 64)
list_append(l, 65)
list_append(l, 128)
list_append(l, 129)
list_append(l, 3)
list_append(l, 2)
list_append(l, 1)
list_append(l, 22)


print(list_contains(l, 1))
print(list_contains(l, 20))
print(list_contains(l, 77))
print(list_contains(l, 22))
