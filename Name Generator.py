#interface for project

print("Hi there")

def check_list(list, check, j, p, m, s):
	t = 0
	for h in threeletters:
		if (h[0] == (i[j]+i[j+1]+i[j+2])):
			if (j==0): p+=1
			elif ((j+2)==(len(i)-1)): s+=1
			else: m+=1
			t = 1
	if t == 0:
		return True,p,m,s
	else:
		return False,p,m,s

def add_the_stuff(list, j, p, m, s, check):
	check,p,m,s = check_list(threeletters, check, j, p, m, s)
	if (check == True):
		threeletters.append([(i[j]+i[j+1]+i[j+2]),len(i),p, m, s])
	
#scan through all names looking for 2 and 3 letter combinations
text = open('names')
names = text.read()
names = names.split('\n')
othernames = []
twoletters = set()
threeletters = []
check = True
for name in names:
	if (name!=''): othernames.append(name.strip().lower())

for i in othernames:
	j = 0
	p = 0
	m = 0
	s = 0
	while ((j+2)!=(len(i))):
		add_the_stuff(threeletters, j, p, m, s, check)
		j+=1
		
	if (len(i) == 3):
		add_the_stuff(threeletters, j, p, m, s, check)


for i in othernames:
	for j in range(0,len(i)):
		if((j-1)>=0):
			twoletters.add(i[j-1]+i[j])
			
		else:
			twoletters.add(i[j]+i[j+1])
#print(twoletters)
print(threeletters)
print(len(threeletters))
