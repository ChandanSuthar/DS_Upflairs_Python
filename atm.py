name = input("tell me your name:")
print("go to hell",name)

message= """
how may i serve you rtrd.

select one of them or leave them be
type 1 >>>> Check Balance.
type 2 >>>> Deposit
type 3 >>>> Withdrawl

"""
print(message)
task = int(input("input your choice bstd: "))
av_amount=5000

if task >=1 and task <=3:
    print('Welcome to you in sasta bank program')

    if task == 1:
        # check balance program
        print('your available amount is: ', av_amount, 'INR')
    elif task == 2:
        # check deposit amount
        dep_amount=int(input('how much you have poor boy: '))
        if dep_amount > 0:
            av_amount += dep_amount
            print('current balance: ',av_amount)
        else:
            print("can't add anything if you don't have anything")

    else:
        # check withdrawl amount
        wit_amount = int(input("how much u need u weed: "))
        if wit_amount <= av_amount:
            av_amount -= wit_amount
            print("now u have only:",av_amount)
        elif av_amount == 0:
            print("u need money u begger")
        else:
            print("you don't have that much nigga")
else: 
    print("choose between 1 to 3!!!")