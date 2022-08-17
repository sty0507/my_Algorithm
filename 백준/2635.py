n = int(input())

list_max = []

for i in range(1, n+1):
	list_arr = [n]
	list_arr.append(i)
	index = 1
	while True:
		num = list_arr[index-1] - list_arr[index]
		if num<0:
			break
		list_arr.append(num)
		index += 1
		if(len(list_max) < len(list_arr)):
			list_max = list_arr

print(len(list_max))
for i in list_max:
	print(i, end=' ')