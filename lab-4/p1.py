class node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class myLinkedList:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
    def atBegining(self,newdata):
        newnode=node(newdata)
        newnode.nextval=self.headval
        self.headval=newnode

list=myLinkedList()
list.headval=node('mon')
e2=node('Tue')
e3=node('wed')
e4=node('Thrusday')
e5=node('friday')
e6=node("satarday")
e7=node('sunday')
list.headval.nextval=e2

e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
list.atBegining('gg')
list.listprint()

        