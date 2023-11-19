from readwrite import iotools
from readwrite import conversion
import os

hello = '''
 _   _      _ _       
| | | | ___| | | ___  
| |_| |/ _ \ | |/ _ \ 
|  _  |  __/ | | (_) |
|_| |_|\___|_|_|\___/ 
'''
print(hello)

instructions = iotools.read_instructions('instructions.txt')
program_direc = input('Directory of program: ').strip()
bin_arr = iotools.read_compile(program_direc, instructions)
full_arr = conversion.fill_array(bin_arr)
new_filename = input('New Filename: ').strip()

while(True):
    choice = input('Write to Hex? y/n:')
    if choice == 'y':
        iotools.write_to_hex(new_filename, full_arr)
        break
    elif choice == 'n':
        iotools.write_to_binary(new_filename, full_arr)
        break
    elif choice == 'debug':
        iotools.write_to_hex(new_filename, full_arr)
        iotools.write_to_binary(new_filename, full_arr)
        break
