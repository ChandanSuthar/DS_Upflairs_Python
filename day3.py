###________boolean, list_______

# var1 = True
# var2 = False
# print(var1, var2)
# print(type(var1), type(var2))

#list = alternate version of array for python

# ls = [25,41,35,72,26.3,22,30.0,'updown','upflairs',True]
# print(ls)
# print(type(ls))
# print(ls[1])
# print(len(ls))
# print(ls[7])
# st=ls[7]
# print(st[2::])
# st1=ls[8]
# print(st1[4:7:1])

#mutable - changeble (list)
#imutable - unchangeble

#insert, remove, manipulate
st_name=['taniya','yash','prerna','ruchika','aditya','kalika']

# st_name[0]="tanya"
# st_name.append('chandan')
# st_name.pop()
# print(st_name)
# st_name.insert(1,'tyrion')
# print(st_name)
# st_name.remove('aditya')
# print(st_name)
# del st_name[1]
# print(st_name)
# ls2 = [85,4,5,6,9,85,25,4,63,6,7]

# ls1.reverse()
# print(ls1) 
# print(ls1[::-1])
# ls2.sort(reverse=True)
# print(ls2)

ls1 = ['A','B','C','D','E']
ls2 = ['F','G','H']
# concat_list = ls1 + ls2
# print(concat_list)
# ls1.append(ls2)
# print(ls1)

# ls1.extend(ls2)
# print(ls1)
# print(ls1.index('C'))
# ls2 = [10,20,3.1,'upflairs pvt ltd', 500,400]
# ls2[2]= 100
#'upflairs pvt ltd' = 'upflairs'
#'upflairs pvt ltd' = 'flipkart pvt ltd'

#__________tuple__________
#imutable - unchangeble

# tpl=(25,41,63,96,'upflairs',True,25.2)
# print(tpl)
# print(type(tpl))
# del tpl[4] - deletion not possible
# tpl[4] = 'flipkart' - assignment not possible
# tpl.count()
# print(tpl.index(96))

#_____---SET---______
st = {52,1,63,85,74,96,54,25,45,8,54,5,54,66,3,54}
# print(st)
# print(type(st))
# st.add(500)
# st.remove(500)
# st.discard(54)
# print(st)

# st1 = {52,41,63,96,78,54}
# st2 = {52,41,65,55,22}
# st1.update(st2) # st1 + st2

# print(st1.intersection(st2))

#---___---dictionary---___---
#collection of items stored in form of key values

# marks = {'mohot':52,'rohit':56,'rockey':53,'mohit':54}
# print(marks)
# print(type(marks))
