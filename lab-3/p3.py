def mySelectionSort(list):
    for i in range(len(list)):
        min=i
        for j in range(i+1,len(list)):
            if list[min]>list[j]:
                min=j
        list[i],list[min]=list[min],list[i]

list=[3,5,2,1,6]
mySelectionSort(list)
print(list)