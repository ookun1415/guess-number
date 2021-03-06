import random #import載入 random 模組-隨機

r = random.randint(1,100) #randint 隨機整數(random+int)
r = int(r)
count = 0 #count 計數
while True:
	count += 1 #count = count + 1的快寫法
	num = input('請猜數字')
	num = int(num)
	if num == r:
		print('猜中了!!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('答案比', num, '小')
	elif num < r:
	    print("答案比", num, '大')
	print('這是你猜的第', count, '次')