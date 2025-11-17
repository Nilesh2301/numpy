import numpy as np
# x = np.array([1,2,3,4])#for array
# print(x)
# y = [1,2,3,4]#for list
# print(y)
# z = np.array([1, 2, 3, 4])
# print(type(z))
# output is---->
# [1 2 3 4]
# [1, 2, 3, 4]
# <class 'numpy.ndarray'>
# l = []
# for i in range(1,5):
#     int_1 =input("Enter no. = ")
#     l.append(int_1)
# print("list:", l)
# print("Array:", np.array(l))
# output--->
# Enter no. = 4
# Enter no. = 6
# Enter no. = 7
# Enter no. = 8
# list: ['4', '6', '7', '8']
# Array: ['4' '6' '7' '8']  
# z = np.array([[1, 2, 3, 4]])
# i = np.array([[[1, 2, 3, 4]]])
# print(z.ndim)
# print(i.ndim)
# ar2 = np.array([[2,4,6],[2,4,6]])
# print(ar2)
# print(ar2.ndim)
# ar3 = np.array([[[ 1,2,3,4,],[3,4,5,6],[4,7,5,2]]])
# print(ar3.ndim)
# print(ar3)
#output---->
# 2
# 3        
# [[2 4 6] 
#  [2 4 6]]
# 2        
# 3        
# [[[1 2 3 4]
#   [3 4 5 6]
#   [4 7 5 2]]]
# arn = np.array([3,4,5,6,],ndmin = 10)
# print(arn)
# print(arn.ndim)
#output--->
# [[[[[[[[[[3 4 5 6]]]]]]]]]]
# 10
#---------------------------------------------------------->"For Zeros"
# ar_zero = np.zeros(3)                                     [Matrix ko pura
# print(ar_zero)                                             Zero krne ke liye]
# print()
# ar_zero2 = np.zeros((3,4))
# print(ar_zero2)
#output--->
# [0. 0. 0.]

# [[0. 0. 0. 0.] 
#  [0. 0. 0. 0.] 
#  [0. 0. 0. 0.]]
# ---------------------------------------------------------->"For Ones"
# ar_one = np.ones(4)                                         [Matrix ke elements
# print(ar_one)                                                ko one krne ke liye]
# print()
# ar_one2 = np.ones((3,4))
# print(ar_one2)
#Output--->
# [1. 1. 1. 1.]

# [[1. 1. 1. 1.] 
#  [1. 1. 1. 1.] 
#  [1. 1. 1. 1.]]
# ---------------------------------------------------------->"For Empty"
# ar_em = np.empty(4)
# print(ar_em)
#output--->
# [[1. 1. 1. 1.]             [Isme all elements previous matrix 
#  [1. 1. 1. 1.]              jaise hote koi changes nhi hota]
#  [1. 1. 1. 1.]]
# ---------------------------------------------------------->"For Range"
# ar_rn = np.arange(6)
# print(ar_rn)
#output--->
# [0 1 2 3 4 5]
# ---------------------------------------------------------->"For Diagonal"
# ar_dia = np.eye(4)
# print(ar_dia)
#output--->
# [[1. 0. 0. 0.] 
#  [0. 1. 0. 0.] 
#  [0. 0. 1. 0.] 
#  [0. 0. 0. 1.]]
# ar_dia = np.eye(4,5)
# print(ar_dia)
#output--->
# [[1. 0. 0. 0. 0.] 
#  [0. 1. 0. 0. 0.] 
#  [0. 0. 1. 0. 0.] 
#  [0. 0. 0. 1. 0.]]
# ---------------------------------------------------------->"For Linspace"
# ar_lin = np.linspace(0,20,num=5)
# print(ar_lin)
#output--->
# [ 0.  5. 10. 15. 20.]
# --------------------------------------------------------------------------->"For R A N D O M"
# ---------------------------------------------------------->"For Rand()"
# var = np.random.rand(4)                        [ 0 se 1 ke beeech 
# print(var)                                       ke numbers # positive]
#output--->
# [0.77178661 0.72451388 0.50291819 0.68953041]-->bar bar run krne par value alg alg milegi random
# var = np.random.rand(3,4)
# print(var)
#output--->
# [[0.55217041 0.08481248 0.40906616 0.8202366 ] 
#  [0.57890372 0.02343788 0.45760045 0.48217826] 
#  [0.80167871 0.40515792 0.46263893 0.77332445]]
# ---------------------------------------------------------->"For Randn()"
# var2 = np.random.randn(4)                      [ 0 se 1 ya 0 ke as pas ke
# print(var2)                                      kuch numbers jo neg aur pos dono ho sakte]
#output--->
# [ 0.70654459  0.30601941 -0.02983318  0.42321602]
# ---------------------------------------------------------->"For Ranf()"
# var3 = np.random.ranf(4)
# print(var3)
#output--->
# [0.58744156 0.97593897 0.46902218 0.03977837]
# ---------------------------------------------------------->"For Randint()"
# var4 = np.random.randint(4,18,4)
# print(var4)
#output--->
# [12 16 13 15]
# -------------------------------------------------------------------------------->"DATA TYPE"
# var = np.array([2,3,4,5]) 
# print("Data Type: ",var.dtype)
# var1 = np.array([1.0,1.2,1.3]) 
# print("Data Type: ",var1.dtype)
# var3 = np.array(["a","b","c","d"])
# print("Data Type: ",var3.dtype)
# var4 = np.array([2,3,4,5,"a","b","c"])
# print("Data Type: ",var4.dtyp
#output--->
# Data Type:  int64  
# DatType:  float64
# Data Type:  <U1    
# Data Type:  <U21  a 
# x1 = np.array([1,2,4,5],dtype = np.int8)
# print("Data Type: ",x1.dtype)
# print(x1)
# x2 = np.array([2,3,4,5,],dtype = "f")
# print("Data Type: ",x2.dtype)
# x3 = np.array([2,3,4,5])

# new = np.float32(x3)

# new_one = np.int32(new)

# print("Data Type: ",x3.dtype)
# print("Data Type: ",new.dtype)
# print("Data Type: ",new_one.dtype)

# print(x3)
# print(new)
# print(new_one)
#output--->
# Data Type:  int64  
# Data Type:  float32
# Data Type:  int32  
# [2 3 4 5]
# [2. 3. 4. 5.]      
# [2 3 4 5]
# x4 = np.array([3,4,5,6])
# new_1 = x4.astype(float)
# print(x4)
# print(new_1)
#output--->
# [3 4 5 6]---> integre ke form me
# [3. 4. 5. 6.]---> float ke form me
# ----------------------------------------------------------------------------"Arthimetic operation"
# var = np.array([3,4,5])----------for add 1D array
# varadd = var + 3
# print(varadd)
# var2 = np.array([4,5,7])---------for add 2D array
# var3 = np.array([3,5,8])
# varadd1 = var2 + var3
# print(varadd1)
# var21 = np.array([4,5,7])
# var31 = np.array([3,5,8])
# varadd1 = np.add(var21,var31)-------(or use np.add)
# print(varadd1)
# var4 = np.array([3,4,5])----------for sub 
# varsub = var4 - 3
# print(varsub)
# var5 = np.array([3,4,5])---------for multy
# varmulti = var5 * 3
# print(varmulti)
# var6 = np.array([3,4,5])----------for div
# vardiv = var6 / 3
# print(vardiv)
# var5 = np.array([3,4,5])----------for mod
# varmulti = var5 % 3
# print(varmulti)
# #output--->
# [6 7 8]
# [ 7 10 15]
# [ 7 10 15]
# [0 1 2]
# [ 9 12 15]
# [1.         1.33333333 1.66666667]
# [0 1 2]
# var30 = np.array([[2,3,4],[4,5,6]])
# var31 = np.array([[1,5,6],[4,9,5]])
# print(var30)
# print(var31)
# print()
# varadd = var30 + var31-----same as(-,*,/,%)
# print(varadd)
# var5 = np.array([3,4,5])
# varmulti = np.reciprocal(var5)
# print(varmulti)
#output--->
# [[2 3 4] 
#  [4 5 6]]
# [[1 5 6]   
#  [4 9 5]]  

# [[ 3  8 10]
#  [ 8 14 11]]
# [0 0 0]
#----------------------------------------------------------------------"Arthimetic Function"
#----------------------------------------------------"For find min $ max value"
# var = np.array([3,4,7,2,1,6])
# print("min: ",np.min(var))----------only find min value
# print("max: ",np.max(var))----------only find max value
# ----------------------------------------------------min/max value with position
# var = np.array([3,4,7,2,1,6])
# print("min: ",np.min(var),np.argmin(var))
# print("max: ",np.max(var),np.argmax(var))
#output--->
# min:  1 4
# max:  7 2
# var = np.array([[2,5,1,4],[4,5,2,7]])-----------------" 2D array me min max find karna"
# print(np.min(var,axis = 1))
# print(np.max(var,axis = 1))
#output--->
# [1 2]
# [5 7]
# var = np.array([[2,5,1,4],[4,5,2,7]])---------"column me min /max find krnA"
# print(np.min(var,axis = 0))
#output--->
# [2 5 1 4]
# var = np.array([2,5,1,4])---------------------"For find square root"
# print("sqrt: ",np.sqrt(var))
#output--->
# qrt:  [1.41421356 2.23606798 1.         2.        ]
# var2 = np.array([3,2,6])-----------------------"For find sin/cos...values"
# print(np.sin(var2))----------------use "Sin"
# print(np.cos(var2))----------------Use"cos"
# print(np.cumsum(var2))-------------Use"cumsum"
#output--->
# [ 0.14112001  0.90929743 -0.2794155 ]
# [-0.9899925  -0.41614684  0.96017029]
#[ 3  5 11]
# --------------------------------------------------------------"Shape"
# var = np.array([[3,4,5,7],[4,5,3,2],[4,1,1,2]])
# print(var)
# print()
# print(var.shape)
#output--->
# [[3 4 5 7] 
#  [4 5 3 2] 
#  [4 1 1 2]]

# (3, 4)
# var9 = np.array([3,5,2,6],ndmin=3)
# print(var9)
#output--->
# [[[3 5 2 6]]]
# --------------------------------mix 
# var2 = np.array([3,4,5,6,],ndmin = 3)
# print(var2)
# print(var2.ndim)
# print(var2.shape)
# output--->
# [[[3 4 5 6]]]
# 3        
# (1, 1, 4)
# --------------------------------------------------------------"ReShape"
# var4 = np.array ([5,7,2,4,8,9,6,7,3])
# x = var4.reshape(3,3)
# print(x)
# one = x.reshape(-1)
# print(one)
#output--->
# [[5 7 2] 
#  [4 8 9] 
#  [6 7 3]]
# [5 7 2 4 8 9 6 7 3]
# --------------------------------------------------------------------------------"Broadcasting"
# var = np.array([3,5,6])
# print(var.shape)
# var2 = np.array([[3],[5],[6])
# print(var2)
# print(var + var2)
#output--->
# (3,)
# [[3]       
#  [5]       
#  [6]]      
# [[ 6  8  9]
#  [ 8 10 11]
#  [ 9 11 12]]
# var2 = np.array([[3,2],[5,3],[6,4]])
# print(var2)
#output--->
# [[3 2] 
#  [5 3] 
#  [6 4]]
# x = np.array([[1],[2]])
# print(x.shape)
# x1 = np.array([[1,2,3],[4,5,6]])
# print(x1.shape)
# print(x+x1)
#output--->
# (2, 1)
# (2, 3)   
# [[2 3 4] 
#  [6 7 8]]
# -------------------------------------------------------------------"Indexing"
#-------------------------------------------"For 1D"
# var = np.array([3,5,7,9])
# print(var[2])
# print(var[-2])
# Output--->
# 7
# 7
#-------------------------------------------"For 2D"
# var = np.array([[2,3,4],[4,5,6]])
# print(var[0,1])
# print(var[1,2])
# Output--->
# 3
# 6
#--------------------------------------------"For 3D"
# var = np.array([[[1,3,5],[4,6,5]]])
# print(var[0,0,2])
# print(var[0,1,1])
#output--->
# 5
# 6
















