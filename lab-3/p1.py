# Bubble Sorting !! - Side by Side : 
# list  =  3,6,1,5,9 
def myBubbleSort(list):
          for x in range(len(list)-1,0,-1):       #Error Line!
                    for idx in range(x):
                              if list[idx]>list[idx+1]:
                                        temp = list[idx]    #Error Line
                                        list[idx] = list[idx+1]
                                        list[idx+1] = temp
list = [3,6,1,5,9]
myBubbleSort(list)
print(list)

