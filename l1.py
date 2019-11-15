import sys
import array
import struct


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
        self.allocated = False

    def write(self, offset, byte):
        if not self.allocated:
            raise InvalidMemoryAccess()
        print('write', hex(self.address), offset, byte)
        self.data[offset] = byte

    def read(self, offset):
        if not self.allocated:
            raise InvalidMemoryAccess()
        result = self.data[offset]
        print('read', hex(self.address), offset, result)
        return result


class AlgoVM(object):

    def __init__(self, pages=640):
        self.ram_size = pages * PAGESIZE
        if self.ram_size > 65*1024:
            raise AddressSizeExceeded
        self.pages = []
        for i in range(pages):
            self.pages.append(Page(i*PAGESIZE, PAGESIZE))

    def malloc(self, size):
        for page in self.pages:
            if not page.allocated:
                page.allocated = True
                print("malloc", hex(page.address))
                return page.address
        raise OutOfMemory()

    def free(self, addr):
        page_num = addr / PAGESIZE
        page = self.pages[page_num ]
        page.free()

    def write(self, addr, byte):
        if not (0 <= byte < 2**8):
            raise ValueError(byte)
        self.pages[addr // PAGESIZE].write(addr % PAGESIZE, byte)

    def read(self, addr):
        return self.pages[addr // PAGESIZE].read(addr % PAGESIZE)

    def write_addr(self, addr, waddr):
        if not (0 <= waddr < 2**16):
            raise ValueError(waddr)
        ary = array.array('B', struct.pack('<H', waddr))
        self.write(addr, ary[0])
        self.write(addr+1, ary[1])

    def read_addr(self, addr):
        b1, b2 = self.read(addr), self.read(addr+1)
        ary = array.array('B', [b1, b2])
        return struct.unpack('<H', ary)[0]

    def _api(self):
        result = {}
        for name in dir(self):
            if name.startswith('_'):
                continue
            attr = getattr(self, name)
            if callable(attr):
                result[name] = attr
        return result


if __name__ == '__main__':
    vm = AlgoVM(1000)
    source = open(sys.argv[1]).read()
    exec(source, vm._api(), {})
