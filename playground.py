import os
import time

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
	
	
def clear_screen():
	os.system("clear");

	
while True:
	delta_time = 5
	timer = 0
	delay = 1
	clear_screen()
	while(timer < delta_time):
		time.sleep(delay)	
		timer += 1
		print('#')
