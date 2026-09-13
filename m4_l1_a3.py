l=[5,4,3,2,1,0]
sum=0
for i in l:
    sum+=i
print("The sum of the list is: ", sum)

avg=sum/len(l)
print("The average of the list is: ", avg)

l.sort()
print("The sorted list is: ", l)

print("The smallest number in the list is: ", l[0])
print("The largest number in the list is: ", l[-1])