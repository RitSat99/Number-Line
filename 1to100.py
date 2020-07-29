
def checkproper(n):
	if n in range(1,100):
		print('success')
	if n not in range(1,100):
		print('Out of Scope')
		
		
numlist=list(range(1,100))
def nextnums():
	for x in numlist:
		if x>n:
			print(x)
		if x==n:
			print(f'{x} is equal to your input')
		if x<n:
			print(f'{x} is smaller than input')

while True:
	
	try:
		n=int(input('Enter a number - '))
		checkproper(n)
		if n not in range(1,100):
			continue
		else:
			pass
	except:
		print('Invalid input')
		continue
	else:
		nextnums()
		ask=input('Try Again? Y/N : ')
		if ask.lower()[0]=='y':
			continue
		else:
			break

# Ritwik Satpathy