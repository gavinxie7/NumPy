import numpy as np

integers=np.array([x for x in range (2,21,2)])
print(integers)

integers_2d=np.array([[1,2,3],[4,5,6]])
print(integers_2d)

print(np.full((3,5),13))

print(np.arange(5))

print(np.arange(5,10))

print(np.arange(10,1,-2))

print(np.linspace(0.0,1.0,num=5))

""" array1=np.arange(1,21)
print(array1)
array2=array1.reshape(4,5)
print(array2)
array3=np.arange(1,100001).reshape(4,25000)
print(array3)
array4=np.arange(1,100001).reshape(100,1000)
print(array4) """

numbers=np.arange(1,6)
print(numbers*2)

numbers+=10
print(numbers)

numbers2=np.linspace(1.1,5.5,5)
print(numbers2)
print(numbers*numbers2)

print(numbers>3)

print(numbers2<numbers)
print(numbers2==numbers)