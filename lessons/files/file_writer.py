filename = 'demofile.txt'
mode = 'a'
f = open(filename, mode)
for i in range(0, 20):
  f.write(str(i) + '\n')
f.close()
