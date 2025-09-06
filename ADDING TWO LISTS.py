# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
i =int((input("enter the no of elements to be in first list")))
list1=[]
for yuo in range(i):
    item=int(input("enter the no"))
    list1.append(item)
    print("your first list is",list1)

r=int(input("enter no of elements that second list must posses"))
hon=[]
if(r!=i):
    print("no on the list exceeds each other ")
    SystemExit

for yt in range(r):
    jrf=int(input("enter no to be added in list 2"))
    hon.append(jrf)
    print("your list 2 is",hon)

jdk=[]
for nrt in range(r):
    y=list1[nrt]+hon[nrt]
    
    jdk.append(y)
    print("the added list of elements is",jdk)






    