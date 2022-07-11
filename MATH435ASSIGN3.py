#!/usr/bin/env python
# coding: utf-8

# Math 435
# Leo Jaos
# 02/10/2022
# Assign 3

# 1). Use the Bisection method to find p3 for f (x) = √x − cos x on [0, 1].

# In[72]:


import math
def funct(x):
    return math.sqrt(x) - math.cos(x)

x = 0
b1 = 0
b2 = 1
chk = True
res = 0
# iterative counter 
count = 0;
# Checks if zero exists, intermediate value THM
def IVT(b1, b2):
    if funct(b1)*funct(b2) > 0:
        return False
    else:
        return True
# If Zero exists
if IVT(b1, b2):
    while count < 3:

        p = (b1 + b2)/(2)

        if funct(b1)*funct(p) < 0 :
            # Then there is a root in [b1,p]
            b2 = p;
            count+=1

        elif funct(b1)*funct(p) == 0 :
         # p is a root
            count += 1
            res = p
            chk = False

        else:
            # funct("b1")*funct("p") > 0 
            # Then there is a root in [p,b]
            count +=1
            b1 = p
    print("p3 for f (x) = √x − cos x on [0, 1]:")
    print("\tZero is ", p)
else:
    print("No zero in interval [%3.10f,%3.10f]" % (b1,b2))
    


# 3). Use the Bisection method to find solutions accurate to within 10−2 for x3 − 7x2 + 14x − 6 = 0 on each interval.
# <br>a. [0, 1] 
# <br>b. [1, 3.2] 
# <br>c. [3.2, 4]

# In[71]:


import math

# Function definition
def funct(x):
    return x**3 - 7*x**2 + 14*x - 6
# Checks if zero exists, intermediate value THM
def IVT(b1, b2):
    if funct(b1)*funct(b2) > 0:
        return False
    else:
        return True
# This function returns the amount of bisection iterations
# it takes to find a zero with an accuracy of 1/x
def fCount(b1,b2,x):
    return (math.floor((math.log(x*(b2 - b1))/(math.log(2)))) + 1)
def bMethod(b1,b2,count):
    # If Zero exists
    if IVT(b1, b2):
        num = fCount(b1,b2,100)
        while count < num:

            p = (b1 + b2)/(2)

            if funct(b1)*funct(p) < 0 :
                # Then there is a root in [b1,p]
                b2 = p;
                count+=1

            elif funct(b1)*funct(p) == 0 :
             # p is a root
                count += 1

            else:
                # funct("b1")*funct("p") > 0 
                # Then there is a root in [p,b]
                count +=1
                b1 = p
        print("\tZero is %1.4f after %d iterations" % (p, num))
    else:
        print("\tNo zero in interval [%3.10f,%3.10f]" % (b1,b2))
# a
print("a). For interval [0,1]")
bMethod(0,1,0)
# b
print("b). For interval [1,3.2]")
bMethod(1,3.2,0)
# c
print("c). For interval [3.2,4]")
bMethod(3.2,4,0)


# 6). Use the Bisection method to find solutions, accurate to within 10−5 for the following problems.
# <br>
# a. 3x − ex = 0 for 1 ≤ x ≤ 2
# <br>
# b. 2x + 3 cos x − ex = 0 for 0 ≤ x ≤ 1
# <br>
# c. x2 − 4x + 4 − ln x = 0 for 1 ≤ x ≤ 2 and

# In[69]:


# Function definition
def funct(x):
    return 3*x - math.exp(x)
# Checks if zero exists, intermediate value THM
def IVT(b1, b2):
    if funct(b1)*funct(b2) > 0:
        return False
    else:
        return True
# This function returns the amount of bisection iterations
# it takes to find a zero with an accuracy of 1/x
def fCount(b1,b2,x):
    return (math.floor((math.log(x*(b2 - b1))/(math.log(2)))) + 1)
def bMethod(b1,b2,count):
    # If Zero exists
    if IVT(b1, b2):
        num = fCount(b1,b2,100000)
        while count < num:

            p = (b1 + b2)/(2)

            if funct(b1)*funct(p) < 0 :
                # Then there is a root in [b1,p]
                b2 = p;
                count+=1

            elif funct(b1)*funct(p) == 0 :
             # p is a root
                count += 1

            else:
                # funct("b1")*funct("p") > 0 
                # Then there is a root in [p,b]
                count +=1
                b1 = p
        print("\tZero is %1.6f after %d iterations" % (p, num))
    else:
        print("\tNo zero in interval [%d,%d]" % (b1,b2))
# a
print("Bisection for 3x − e^x = 0 for 1 ≤ x ≤ 2")
bMethod(1,2,0)
# Function definition
def funct(x):
    return (2*x) + (3*math.cos(x)) - (math.exp(x))
# b
print("Bisection for 2x + 3 cos x − ex = 0 for 0 ≤ x ≤ 1")
bMethod(0,1,0)



# 14). Use Theorem 2.1 to find a bound for the number of iterations needed to achieve an approximation with accuracy 10−3 to the solution of x3+x−4 = 0 lying in the interval [1, 4]. Find an approximation to the root with this degree of accuracy

# In[70]:


# Function definition
def funct(x):
    return x**3 + x -4
# Checks if zero exists, intermediate value THM
def IVT(b1, b2):
    if funct(b1)*funct(b2) > 0:
        return False
    else:
        return True
# This function returns the amount of bisection iterations
# it takes to find a zero with an accuracy of 1/x
def fCount(b1,b2,x):
    return (math.floor((math.log(x*(b2 - b1))/(math.log(2)))) + 1)
def bMethod(b1,b2,count):
    # If Zero exists
    if IVT(b1, b2):
        num = fCount(b1,b2,1000)
        while count < num:

            p = (b1 + b2)/(2)

            if funct(b1)*funct(p) < 0 :
                # Then there is a root in [b1,p]
                b2 = p;
                count+=1

            elif funct(b1)*funct(p) == 0 :
             # p is a root
                count += 1

            else:
                # funct("b1")*funct("p") > 0 
                # Then there is a root in [p,b]
                count +=1
                b1 = p
        print("\tZero is %1.5f after %d iterations" % (p, num))
        print("\tAnd so, the lower bound for the number of iterations is: %d" % num)
    else:
        print("No zero in interval [%d,%d]" % (b1,b2))
# a
print("Bisection for x3+x−4 = 0 where for 1 ≤ x ≤ 4")
bMethod(1,4,0)



# In[ ]:




