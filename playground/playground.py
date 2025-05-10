import os
import time
import random

# x = input("2 numbers with space");
# x, y = tuple(map(lambda x: int(x), x.split(' ')));
# print(type(x), type(y));
# height, width = 4, 4
# a = {(i, j): 1 for i in range(height + 1) for j in range(width + 1)}

# for i in range(height + 1):
# 	s = ""
# 	for j in range(width + 1):
# 		s += str(i) + "," + str(j) + ":" + str(a[i, j]) + " "
# 	print(s)
	
	
# def clear_screen():
# 	os.system("clear");

	
# while True:
# 	delta_time = 5
# 	timer = 0
# 	delay = 1
# 	clear_screen()
# 	while(timer < delta_time):
# 		time.sleep(delay)	
# 		timer += 1
# 		print('#')

# arr = ["#", "#", "$", "$", "@", "@", "%", "%", "~", "~", "*", "*", "+", "+", ")", ")"] 

# def get_item():
# 	item = arr.pop(random.randrange(len(arr))) 
# 	return item

# a = [[get_item() for i in range(4)] for j in range(4)] 

# for i in a:
# 	s = ""
# 	for j in i:
# 		s += " " + j
# 	print(s)
		
		

def get_arr(*rest):
	print(type(rest))
	for i in rest: 
		print(i)

get_arr(1, 2, 3)