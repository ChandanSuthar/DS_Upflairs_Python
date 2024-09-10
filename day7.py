## function in programming lang

#1.add to numbers
#defination
# def add_2(num1,num2):
#     output = num1 + num2
#     return output

# a=int(input('enter 1st number: '))
# b=int(input('enter 2nd number: '))

# #calling
# output = add_2(a,b)
# print("yor output is : ",output)

ls = [41,52,63,36,25,14,47,58,69,96,85,74]
print(len(ls))

my_len = 0
for i in ls[0:]:
    my_len+=1
print(my_len)

def my_len(ls):
    c=0
    for i in ls:
        c+=1
    return c

#assignment given



#____________________________________= Module In Python =____________________________________

manager_name = "Dharmpal ji"
manager_address = "Bihar"

employee_list = ['rohit','rahul','mohit','suresh','jagdeesh']

rohit_id = 'hello@gmail.com'
rohit_pass = "124@786"

def rohit_hii():
    print("employee name: ",employee_list[0])
    print('rohit id: ',rohit_id)
    print('rohit password: ',rohit_pass)

def dharmpal_hii():
    print("manager name: ",manager_name)
    print('manager id: ',manager_id)
    print('manager password: ',manager_pass)



manager_id = 'manager_boss@gmail.com'
manager_pass = 'boss123456'
