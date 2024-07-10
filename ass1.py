# *
# **
# ***
# ****
# *****
# ******
for i in range(1,7):
    for j in range(1,i+1):
        print("*",end="")
    print(" ")
print("\n")

# 1
# 12
# 123
# 1234
# 12345
# 123456
for i in range(1,7):
    for j in range(1,i+1):
        print(j,end="")
    print(" ")

#min&max with loops
ls = [2, -7, -55, 45, 32, 66, 77, 4, 1, 77, 9, 98]

max_value = ls[0]
min_value = ls[0]

for i in ls[1:]:
    if i > max_value:
        max_value = i
    if i < min_value:
        min_value = i

print("Min value:", min_value)
print("Max value:", max_value)
