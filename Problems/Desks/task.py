# put your python code here
groups = map(int, [input(), input(), input()])
quantity = 0
for x in groups:
    quantity += x // 2 + x % 2
print(quantity)
