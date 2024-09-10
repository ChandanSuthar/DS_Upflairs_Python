#------loop-------
#loop
#1.for
#2.while
#3.do while

# for i in range(10): # 10
#     print("nothing",i)
# print("\n")
# for i in range(5,10): # 
#     print("nothing",i)

# i=0
# while (i<=10):
#     print('hello World ',i)
#     i=i+1
#     i+=1

# for i in range(100):
#     print("Welcome")

# condition = True
# while condition:
#     user_input = input("do you want to stop:(Y/y): ")
#     if user_input == 'Y' or user_input == "y":
#         condition = False
#         print("bye")
#     else:
#         print("Welcome bastard")
    
#break , continue

# for i in range(10):
#     print(i)
#     if i==5:
#         break

# for i in range(10):
#     if i==5:
#         continue
#     print(i)

ls = [52,41,63,96,85,7,45,86,6,9,12,36,72,11,22,33]

# if 85 in ls:
#     print('present')
# else:
#     print("not present")

count = 0
for item in ls:
    if item == 85:
        print("present ",count)
        break
    count +=1

print("final count ",count)

# ls min(), max()
# without using min,max find it via loops

"""make the following patterns:
*
**
***
****
*****
******

1
12
123
1234
12345
123456

"""