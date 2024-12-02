from collections import Counter 
#  part 1
a, b = [], [] #create 2 lists 
with open('input.txt', 'r') as file:
    for line in file.readlines(): # reades every line
        x,y = (int(z) for z in line.split())
        a.append(x) # append elements to lists one by one
        b.append(y) 
 # Sorting 2 list to find corresponding elements(smallest to smallest)    
a.sort()
b.sort()
 
result = 0
for i in range(len(a)): # looping each element  
    distance = a[i]-b[i] # and find differences of each corresponding element
    result += abs(distance) # abs() to ignore negative nums
    
print(f'Sum of distance difference: {result}')
 
 #   part 2
c= Counter(b) #counts the appearences
similarity_score = 0

for times in a: # checking each number in a list to find equal nums and appearences
    similarity_score += times * c.get(times, 0) # multiple by how many times it is in right list for similaity score
print(f'similarity Score: {similarity_score}')