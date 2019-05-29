import random
n = random.randint(1,100)
while True:
	number = input('猜猜这个数字是什么：')
	number = int(number)
	if number == n:
		print('恭喜你猜对了!')
		break
	elif number > n:
		print('数字比答案大')
	else:
		print('数字比答案小')