import re

class iotools:
    
    @staticmethod
    def read_instructions(filename):
        library = {}
        with open(filename, 'r') as file:
            for line in file:
                op, code = line.strip().lower().split(':') 
                op = op.strip()
                code = code.strip()
                library[op] = code
        return library
    
    @staticmethod
    def write_to_binary(filename, bin_arr):
        filename = filename + '.txt'
        with open(filename, 'w') as file:
            for line in bin_arr:
                file.write(line + '\n')

    @staticmethod
    def write_to_hex(filename, bin_arr, comment_arr):
        filename = filename + '.hex'
        hex_arr = conversion.bin_to_hex_arr(bin_arr)
        with open(filename, 'w') as file:
            for i in range(len(hex_arr)):
                file.write(hex_arr[i] + ';' + comment_arr[i] + '\n')

    @staticmethod
    def read_compile(filename, library = dict):
        bit_arr = []
        comment_arr = []
        with open(filename, 'r') as file:
            for line in file:
                if line.strip().startswith('%'):
                    bit_arr.append('0000000000000')
                else:
                    try:
                        opcode, dest, data, comment = re.split(r'\s{1,15}', line.lower().strip())
                        if comment.startswith('%'):
                            comment = comment[1:]
                        else:
                            raise ValueError('Error due to earlier errors')
                    except:
                        try: 
                            opcode, dest, data = re.split(r'\s{1,15}', line.lower().strip())
                            comment = ''
                        except:
                            opcode, data = re.split(r'\s{1,15}', line.lower().strip())
                            dest = 'n'
                            comment = ''

                    
                    opcode_bin = library[opcode]
                    dest_bin = library[dest]
                    if data.startswith('$'):
                        data = data[1:]
                    else:
                        data_bin = conversion.decimal_to_binary(data)
                    bit_arr.append(opcode_bin + dest_bin + data_bin)
                    comment_arr.append(comment)
        return [bit_arr, comment_arr]

    @staticmethod
    def read_compile_revamp(filename = str, library = dict):
        bit_arr = []
        with open(filename, 'r') as file:
            for line in file:

                try:
                    op, data, comment = re.split(r'[,;]', line.lower().strip(), 3)
                except:
                    raise Exception('Error due to earlier errors')
                pass
                    
                    

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
    
    @staticmethod
    def fill_str_arr(str_arr):
        if len(str_arr) < 64:
            remaining = 64 - len(str_arr)
            str_arr.extend([''] * remaining)
        elif len(str_arr) > 64:
            str_arr = str_arr[:64]
        return str_arr