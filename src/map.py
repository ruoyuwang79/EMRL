fd1 = open('img.csv', 'r')
a = fd1.read().split('\n')
a = [i.split(',') for i in a]

for i in range(len(a)):
	for j in range(len(a[i])):
		if (i > 32 and i < 38) and (j > 109 and j < 114):
			a[i][j] = '255'

a[26][92] = '255'

# a[23][105] = '0'

content = ''
for i in a:
	for j in i:
		content += j
		content += ','
	content = '\n'.join(content.rsplit(',', 1))

fd2 = open('img.csv', 'w')
fd2.write(content[:-1])

fd1.close()
fd2.close()