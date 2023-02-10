def myInsertionSort(list):
    for i in range(1,len(list)):
        j=i-1
        nextElement=list[i]
        while(list[j]>nextElement)and(j>=0):
            list[j+1]=list[j]
            j=j-1
        list[j+1]= nextElement
list=[3,5,1,6,9]
print(myInsertionSort(list))
print(list)