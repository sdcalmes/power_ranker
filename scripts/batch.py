import subprocess
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

path = 'MY_LOCAL_CONFIG.cfg'

# subprocess.call('python command_line.py -l 185829 -y 2014 -w 1')
# replace(path, 'doPlayoffs      = False', 'doPlayoffs = False')
#
# for x in range(2, 14):
#     if x == 2:
#         print('x is 2')
#         replace(path, 'doPlayoffs = False', 'doPlayoffs = True')
#         replace(path, 'num_simulations = 200000', 'num_simulations = 20000')
#     if x == 5:
#         replace(path, 'num_simulations = 20000', 'num_simulations = 60000')
#     if x == 8:
#         replace(path, 'num_simulations = 60000', 'num_simulations = 100000')
#
#     print('Year: 2014, Week: %s' % x)
#     replace(path, 'week = ' + str(x-1), 'week = ' + str(x))
#     subprocess.call("python command_line.py -c MY_LOCAL_CONFIG.cfg")

subprocess.call('python command_line.py -l 185829 -y 2015 -w 1')
replace(path, 'doPlayoffs      = False', 'doPlayoffs = False')

for x in range(2, 14):
    if x == 2:
        replace(path, 'doPlayoffs = False', 'doPlayoffs = True')
        replace(path, 'num_simulations = 200000', 'num_simulations = 20000')
    if x == 5:
        replace(path, 'num_simulations = 20000', 'num_simulations = 60000')
    if x == 8:
        replace(path, 'num_simulations = 60000', 'num_simulations = 100000')

    print('Year: 2015, Week: %s' % x)
    replace(path, 'week = ' + str(x-1), 'week = ' + str(x))
    subprocess.call("python command_line.py -c MY_LOCAL_CONFIG.cfg")

subprocess.call('python command_line.py -l 185829 -y 2016 -w 1')
replace(path, 'doPlayoffs      = False', 'doPlayoffs = False')

for x in range(2, 14):
    if x == 2:
        print('X is 2')
        replace(path, 'doPlayoffs = False', 'doPlayoffs = True')
        replace(path, 'num_simulations = 200000', 'num_simulations = 20000')
    if x == 5:
        replace(path, 'num_simulations = 20000', 'num_simulations = 60000')
    if x == 8:
        replace(path, 'num_simulations = 60000', 'num_simulations = 100000')

    print('Year: 2016, Week: %s' % x)
    replace(path, 'week = ' + str(x-1), 'week = ' + str(x))
    subprocess.call("python command_line.py -c MY_LOCAL_CONFIG.cfg")

subprocess.call('python command_line.py -l 185829 -y 2017 -w 1')
replace(path, 'doPlayoffs      = False', 'doPlayoffs = False')

for x in range(2, 14):
    if x == 2:
        replace(path, 'doPlayoffs = False', 'doPlayoffs = True')
        replace(path, 'num_simulations = 200000', 'num_simulations = 20000')
    if x == 5:
        replace(path, 'num_simulations = 20000', 'num_simulations = 60000')
    if x == 8:
        replace(path, 'num_simulations = 60000', 'num_simulations = 100000')

    print('Year: 2017, Week: %s' % x)
    replace(path, 'week = ' + str(x-1), 'week = ' + str(x))
    subprocess.call("python command_line.py -c MY_LOCAL_CONFIG.cfg")




