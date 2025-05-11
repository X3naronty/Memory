

class A:
    count = 0
    def __init__(self):
        A.count += 1
        self.count = A.count 
        
a = [A() for i in range(5)]

for item in a:
    print(item.count)