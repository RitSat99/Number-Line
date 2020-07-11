def checkproper(n):
	if n in range(1,100):
		print('success')
		run=True

	else:
		print('Fail')
		run=False

		
numlist=list(range(1,100))
def nextnums():
	for x in numlist:
		if x>n:
			print(x)
		else:
			print(f'{x} is smaller than input')

try:
	n=int(input('Enter a number - '))
except:
	print('Wrong Entry')
else:
	checkproper(n)
	nextnums()
finally:
	print('Ritwik')