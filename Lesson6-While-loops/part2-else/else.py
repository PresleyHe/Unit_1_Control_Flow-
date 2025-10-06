#while ... else
'''
the else clause runs when:
the loop completes normally 
WITHOUT hitting a break
'''
#Basic Example
count = 1 
while count <= 3:
    print(count)
    count += 1
else:
    print("Loop Completed")
    
#Basic Example 2
count = 1 
while count <= 5:
    print(count)
    if count == 3:
        break
    count += 1
else:
    print("Loop Completed")