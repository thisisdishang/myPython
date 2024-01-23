# Substract two list elements and output new list if the element in the first list are greater

list1=[95,1,41,85,9]
list2=[4,15,2,78,6]
subslist=[]

if len(list1)>len(list2):
    for i in range(len(list1)):
        if(list1[i]>list2[i]):
            subslist.append(list1[i]-list2[i])
elif len(list1)<len(list2):
    for i in range(len(list2)):
        if(list1[i]>list2[i]):
            subslist.append(list1[i]-list2[i])    
else:
    for i in range(len(list1)):
        if(list1[i]>list2[i]):
            subslist.append(list1[i]-list2[i])   

print(list1)
print(list2)
print("List After Substract")
print(subslist)    