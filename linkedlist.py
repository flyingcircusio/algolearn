#
#
#
#


def append(list, value):
    node = malloc(3)
    write(node, value)
    first = read_addr(list)
    if first == 0:
        write_addr(list, node)
    else:
        cur = first
        while cur != 0:
            prev = cur
            cur = read_addr(cur+1)
        write_addr(prev+1, node)


def len(list):
    pass

def remove(list):
    pass

def insert(list, pos, value):
    pass

def contains(list, value):
    pass



list = malloc(2)

append(list, 4)
append(list, 5)
append(list, 6)
append(list, 7)

