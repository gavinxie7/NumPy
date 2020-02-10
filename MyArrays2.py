import numpy as np
grades=np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])
print(grades.sum())
print(grades.min())
print(grades.max())
print(grades.mean())
print(grades.std())
print(grades.var())

print(grades.mean(axis=0))
print(grades.mean(axis=1))

numbers=np.array([1,4,9,16,25,36])
print(np.sqrt(numbers))

numbers2=np.arange(1,7)*10
print(numbers2)

#universal function to add arrays
print(np.add(numbers,numbers2))

#let's use the multiply universal function to multiply every element of numbers2 by the scalar value 5:
print(np.multiply(numbers2,5))

#let's reshape numbers2 into a 2-by-3 array, then multiply its values by a one-dimensional array of three elements:
numbers3=numbers2.reshape(2,3)
print(numbers3)
numbers4=np.array([2,4,6])
print(np.multiply(numbers3,numbers4))

#grab a certain number in an array by index
grades=np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])
print(grades[0,1])
print(grades[0][1])
print(grades[1])
#upper limit is not included!!!
print(grades[0:2])
#second row and the fourth row
print(grades[1],grades[3])
print(grades[[1,3]])
#show the first element in each row
print(grades[:,0])
#show the second and third value for each row
print(grades[:,1:3])
#show the first and third value for each row
print(grades[:,[0,2]])

#shallow copies
numbers=np.arange(1,6)
number2=numbers.view()
print(number2)
numbers[1]*=10
print(number2)
#does change in number2 effect numbers?
number2[1]/=10
print(numbers)
#therefore, we can see that the two arrays share the same data thourgh the shallow copies
numbers2=numbers[0:3]
print(numbers2)
numbers[1]*20
print(numbers2)

#deep copies(they do not affect each other)
numbers2=numbers.copy()

#reshape creates a shallow copy or a view
grades=np.array([[87,96,70],[100,87,90]])
print(grades.reshape(1,6))
print(grades)
#resize would keep the change
grades=np.array([[87,96,70],[100,87,90]])
grades.resize(1,6)
print(grades)
#go back to one dimention
grades=np.array([[87,96,70],[100,87,90]])
flattened=grades.flatten()
print(grades)
raveled=grades.ravel()
print(raveled)
raveled[5]=99
print(grades)

grades2=grades.T
print(grades2)
print(grades)

grades=np.array([[87,96,70],[100,87,90]])
grades2=np.array([[94,77,90],[100,81,82]])

h_grades=np.hstack((grades,grades2))
print(h_grades)

v_grades=np.vstack((grades,grades2))
print(v_grades)