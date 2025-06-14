N = int(input("List size = "))
if N<=0:
    print("number must be greater then 0")
    exit()
List_elements = []
for _ in range(N):
    num = int(input())
    List_elements.append(num)
print("List element:",List_elements)
cum_sum = []
current_sum = 0
for num in List_elements:
    current_sum = current_sum + num
    cum_sum.append(current_sum)
print("cum_sum:",cum_sum)
