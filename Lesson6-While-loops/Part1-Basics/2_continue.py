## The Contihue Statement
'''
**continue** = Skip to the next ieteration!

**Difference from break:**
- **break** --> find 
'''
#Example skip 3
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count) # 1 2  4 5