#list comprehensions- given three integers and representing the dimensions of a cuboid along with an integer.Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to. using list comprehensions rather than multiple loops#

###asked for the input###
x = int(input())
y = int(input())
z = int(input())
n = int(input())

#created a empty list#
coordicates =[]

#using Loops to generate all possible combinations in range#
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):

              #check condition#
                if i + j + k != n: 

                  #add it to empty list and print#
                    coordicates.append([i, j, k])
    
    print(coordicates)
