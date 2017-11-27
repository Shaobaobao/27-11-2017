array = [2,4,2,10,6,8,9,3,0,8]
largest = 0
i = 0
while i < len(array):
    if largest < array[i]:
        largest = array[i]
    i = i + 1  
print(largest)
        
