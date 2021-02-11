a = int(input())
b = int(input())
c = int(input())
result = str(a*b*c)
print_result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in result:
    print_result[int(i)] += 1
for i in print_result:
    print(i)