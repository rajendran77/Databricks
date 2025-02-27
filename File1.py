l1=[1,2,3,4,5]
l2=[1,2,3,4]

class Student:
    def __init__(self, l1, l2):
        self.list1=l1
        self.list2=l2
        self.l3 =[] 
    def __add__(self, others):
        l3 = self.list1 + self.list2
        return l3

Student_1=Student(l1, l2)
l3=Student_1 + None
print (l3)
