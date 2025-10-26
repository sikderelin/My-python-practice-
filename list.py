###Initialize list and read in the value of followed by N lines of commands, where each command will be of the 7types. Iterate through each command in order and perform the corresponding operation on the list.###


N = int(input()) #---> number of command will be using, so whatever number user input that how many commaned will be use 
   
list = [] # --> empty list

#loops through N number of command and asks the user to input
    for i in range(N):
        e = input().split() #--> Split the string(command) into parts(index) to macth with the conditon.

##After spliting to index, the first index[0] is the command.## 
##if the command(indedx[0]) matches, it will convert rest of string to integers.##

#--> if it matches, converts the position(index[1]) and value(index[2] to integers and insert the value at the specific position in the list.
        if e[0] == 'insert':  
           position = int(e[1])
           value = int(e[2])
           list.insert(position, value)
          
#--> if the command matched, convert the value to integer and adds to/remove from the end of the list 
        elif e[0] == 'append':
            list.append(int(e[1]))
            
        elif e[0] == 'remove':
            list.remove(int(e[1]))
            
        elif e[0] == 'sort': #-->if matches, sorts the list in ascending order.
            list.sort()
            
        elif e[0] == 'pop': #--> if matches, removes the last element of the list.
            list.pop()
        
        elif e[0] == 'reverse': #--> if matches, reverses the order of the list.
            list.reverse()
            
        elif e[0] == 'print':
            print(list)
           
        
