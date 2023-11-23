from uniciclo import convertidor


class memoria:
    def __init__(self, size):
        self.memory = [['0', 'x']] * size
        count = 0
        base_address = '0x10000000'

        while count < size:
            decimal_num = convertidor.hexadecimal_to_decimal(base_address)
            tmp_address = convertidor.decimal_to_hexadecimal(decimal_num + 4 * count)
            self.memory[count] = [tmp_address, 'x']
            count += 1

    def read(self, address):
        for entry in self.memory:
            if address == entry[0] and entry[1] != 'x':
                return entry[1]
        return None

    def write(self, address, value):
        for entry in self.memory:
            if address == entry[0]:
                entry[1] = value
                break

