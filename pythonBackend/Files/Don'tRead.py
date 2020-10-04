###########################################################################
# readLine will only read the only one line
#########################################################################

file = open('test.txt')
line = file.readline()
while line != '':
    print(line)
    line = file.readline()
print(line)
