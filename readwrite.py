import re

class iotools:
    
    @staticmethod
    def read_instructions(filename):
        library = {}
        with open(filename, 'r') as file:
            for line in file:
                op, code = line.strip().split(':') 
                op = op.strip()
                code = code.strip()
                library[op] = code
        return library
    
    @staticmethod
    def write_to_binary(filename, bin_arr):
        filename = filename + '.bin'
        with open(filename, 'w') as file:
            for line in bin_arr:
                file.write(line + '\n')

    @staticmethod
    def write_to_hex(filename, bin_arr):
        filename = filename + '.hex'
        hex_arr = conversion.bin_to_hex_arr(bin_arr)
        with open(filename, 'w') as file:
            for line in hex_arr:
                file.write(line + ';\n')

    @staticmethod
    def read_compile(filename, library = dict):
        bit_arr = []
        with open(filename, 'r') as file:
            for line in file:
                if(line.strip()[0] == '%'):
                    pass
                else:
                    opcode, dest, data = re.split(r'\s{1,3}', line.strip())
                opcode_bin = library[opcode]
                dest_bin = library[dest]
                data_bin = conversion.decimal_to_binary(data)
                bit_arr.append(opcode_bin + dest_bin + data_bin)
        return bit_arr
    
class conversion:

    @staticmethod
    def decimal_to_binary(num_str):
        num = int(num_str)
        binary_str = bin(num)[2:]
        if len(binary_str) < 8:
            binary_str = '0' * (8 - len(binary_str)) + binary_str
        elif len(binary_str) > 8:
            binary_str = binary_str[-8:]
        return binary_str
    
    @staticmethod 
    def binary_to_hex(bin_str):
        num = int(bin_str, 2)
        hex_str = hex(num)[2:]
        return hex_str.zfill(4)
    
    @staticmethod
    def bin_to_hex_arr(bin_arr):
        hex_arr = []
        for i in range (len(bin_arr)):
            hex_arr.append(conversion.binary_to_hex(bin_arr[i]))
        return hex_arr

    @staticmethod
    def fill_array(bin_arr):
        if len(bin_arr) < 64:
            remaining = 64 - len(bin_arr)
            bin_arr.extend(['0000000000000'] * remaining)
        elif len(bin_arr) > 64:
            bin_arr = bin_arr[:64]
        return bin_arr