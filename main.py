from readwrite import iotools
from readwrite import conversion

hello = '''


 __  __  ____ _   _    ____ ___  ____  _____                   
|  \/  |/ ___| | | |  / ___/ _ \|  _ \| ____|                  
| |\/| | |   | | | | | |  | | | | | | |  _| _____              
| |  | | |___| |_| | | |__| |_| | |_| | |__|_____|             
|_|__|_|\____|\___/   \____\___/|____/|_____| _____ ___  ____  
|_   _|  _ \    / \  | \ | / ___|| |      / \|_   _/ _ \|  _ \ 
  | | | |_) |  / _ \ |  \| \___ \| |     / _ \ | || | | | |_) |
  | | |  _ <  / ___ \| |\  |___) | |___ / ___ \| || |_| |  _ < 
  |_| |_| \_\/_/   \_\_| \_|____/|_____/_/   \_\_| \___/|_| \_\\

'''
print(hello)

instructions = iotools.read_instructions('instructions.txt')
program_direc = input('Directory of program: ').strip()
bin_arr, comment_arr = iotools.read_compile(program_direc, instructions)
comments = conversion.fill_str_arr(comment_arr)
full_arr = conversion.fill_array(bin_arr)
new_filename = input('New Filename: ').strip()

while(True):
    choice = input('Write to binary? y/n:')
    if choice == 'y':
        iotools.write_to_binary(new_filename, full_arr)
        break
    elif choice == 'n':
        break
iotools.write_to_hex(new_filename, full_arr, comments)