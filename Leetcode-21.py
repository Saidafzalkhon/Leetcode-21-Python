# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            son = ListNode()
            uzunlik = son
            
            while list1 and list2:
                if list1.val<list2.val:
                    uzunlik.next = list1
                    list1 = list1.next
                else:
                    uzunlik.next = list2
                    list2 = list2.next
                uzunlik = uzunlik.next
            
            if list1:
                uzunlik.next = list1
            elif list2:
                uzunlik.next = list2
                
            print(son.next)