print('Enter 4 numbers:')

r = []
for i in range(4):
    r.append(int(input()))

print('%.2f' % ((r[0]+r[1])/(r[2]+r[3])))