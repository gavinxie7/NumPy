'''
old_list=[1,2,3,4,5]
new_list=[]
for i in old_list:
    if filter(i):
        new_list.append(expressions(i)) '''

#new_list=[[expression9i] for i in old_List if filter(i)]

#use of the loop
x=[i for i in range(10)]
print(x)

squares=[i**2 for i in range(10)]
print(squares)

list1=[3,4,5]
multiplied=[i*3 for i in list1]
print(multiplied)

listofwords=["this","is","a","list","of","words"]
new_listofwords=[i[0] for i in listofwords]
print(new_listofwords)

items=[x.lower() for x in ['A','B','C']]
print(items)

items=[x.upper() for x in ['a','b','c']]
print(items)

#use if statements for np
new_range=[i*i for i in range(5) if i%2==0]
print(new_range)

#isdigit for numbers
string="Hello 12345 World"
numbers=[x for x in string if x.isdigit()]
print(numbers)

infile=open("test.txt","r")
result=[i for i in infile if "line3" in i]
print(result)

#using functions for np
def double(x):
    return x*2
print(double(10))

newlist=[double(x) for x in range(10)]
print(newlist)

newlist=[x+y for x in [10,20,30] for y in [20,40,60]]
print(newlist)