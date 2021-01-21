filename = 'demofile.txt'
mode = 'r'
f = open(filename, mode)
# for i in range(0, 20):
#   text = f.readline() #read only a single line
#   print(text)
text = f.read() #read the entire file into one variable
print(text)
f.close()
