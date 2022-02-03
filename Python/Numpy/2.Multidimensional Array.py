a2  = np.array([[1,2],[3,4]])
print(a2)
print(a2.shape)
print(a2.ndim)

# access element.
print("elements", a2[0,1]) # prints individual elements 
print("elements", a2[0]) # print one row

print(a2.T) # print transpose
print(np.linalg.inv(a2))# prints inverse and remeber to keep it square matrix
print(np.linalg.det(a2)) # determinant
print(np.diag(a))# diagonal elements of the array
