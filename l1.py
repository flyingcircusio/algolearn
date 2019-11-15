import sys
import array
import struct


# IDEAS
#
#
# Operations:
#   * count_nonzero (page/allocation) cost o(1)
#   * bitwise operations
#
# Data structures:
#
#   structs


PAGESIZE = 64


class OutOfMemory(Exception):
    pass

class InvalidMemoryAccess(Exception):
    pass

class OverFlow(Exception):
    pass

class AddressSizeExceeded(Exception):
    pass



class Page(object):

    def __init__(self, address, size):
        self.address = address
        self.data = bytearray(size)
        self.allocated = False

    def free(self):
        if not self.allocated:
            raise InvalidMemoryAccess()
        print('free', '\t\t', hex(self.address))
        self.allocated = False

    def write(self, offset, byte, quiet=False):
        if not self.allocated:
            raise InvalidMemoryAccess()
        if not quiet:
            print('write', '\t\t', hex(self.address+offset), '\t<- ', byte)
        self.data[offset] = byte

    def read(self, offset, quiet=False):
        if not self.allocated:
            raise InvalidMemoryAccess()
        result = self.data[offset]
        if not quiet:
            print('read', '\t\t', hex(self.address+offset), '\t-> ', result)
        return result

    def allocate(self, size, quiet=False):
        self.allocated = True
        if not quiet:
            print("malloc", '\t\t', size, '\t-> ', hex(self.address))
        return self.address


class AlgoVM(object):

    def __init__(self):
        self.ram_size = 2**16
        self.pages = []
        for i in range(self.ram_size // PAGESIZE):
            self.pages.append(Page(i*PAGESIZE, PAGESIZE))
        # Allocate the zero page to ensure malloc will never return
        self.pages[0].allocate(0, quiet=True)
        # How much cost did the running programincur?
        self.cost = 0

    def malloc(self, size):
        self.cost += 1
        if size > PAGESIZE:
            raise OverFlow(
                "Allocating beyond page size is unsupported at this point")
        for page in self.pages:
            if not page.allocated:
                return page.allocate(size)
        raise OutOfMemory()

    def free(self, addr):
        self.cost += 1
        page_num = addr / PAGESIZE
        if not page_num:
            raise InvalidMemoryAccess()
        page = self.pages[page_num ]
        page.free()

    def write(self, addr, byte, quiet=False):
        self.cost += 1
        if not (0 <= byte < 2**8):
            raise ValueError(byte)
        self.pages[addr // PAGESIZE].write(addr % PAGESIZE, byte, quiet=quiet)

    def read(self, addr, quiet=False):
        self.cost += 1
        return self.pages[addr // PAGESIZE].read(addr % PAGESIZE, quiet=quiet)

    def write_addr(self, addr, waddr):
        self.cost += 3
        if not (0 <= waddr < 2**16):
            raise ValueError(waddr)
        print("write_addr", '\t', hex(addr), '\t<- ', hex(waddr))
        ary = array.array('B', struct.pack('<H', waddr))
        self.write(addr, ary[0], quiet=True)
        self.write(addr+1, ary[1], quiet=True)

    def read_addr(self, addr):
        self.cost += 3
        b1, b2 = self.read(addr, quiet=True), self.read(addr+1, quiet=True)
        ary = array.array('B', [b1, b2])
        result = struct.unpack('<H', ary)[0]
        print("read_addr", '\t', hex(addr), '\t-> ', hex(result))
        return result

    def _api(self):
        result = {}
        for name in dir(self):
            if name.startswith('_'):
                continue
            attr = getattr(self, name)
            if callable(attr):
                result[name] = attr
        result['PAGESIZE'] = PAGESIZE
        return result


if __name__ == '__main__':
    vm = AlgoVM()
    source = open(sys.argv[1]).read()
    try:
        exec(source, vm._api(), {})
    except:
        raise
    finally:
        print("Your program required {} performance tokens.".format(vm.cost))
