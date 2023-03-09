from lib.rparser import Parser

# source file, needs to be a raw text file
IN_FILE = 'input_text.txt'

# these two should be rpy files
# output file don't name this the same as the init file
# probably make it the same as the input just .rpy
OUT_FILE = 'output.rpy'
# file where the init stuff goes, you dont 'need' to change this
INIT_FILE = 'script.rpy'

p = Parser()

# parsing the file
with open(IN_FILE, 'r') as f:
    for line in f:
        p.parse_line(IN_FILE, line)

with open(OUT_FILE, 'w') as f:
    for line in p.get_file(IN_FILE):
        f.write(line)
        
# creating the init file
with open(INIT_FILE, 'w') as f:
    for line in p.get_init():
        f.write(line)