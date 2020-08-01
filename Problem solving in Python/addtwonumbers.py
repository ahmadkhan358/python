class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        newNode = ListNode(val)
        if self.head == None and self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def listHead(self):
        return self.head 

    def printList(self):
        temp = self.head

        while temp != None:
            print(temp.val)
            temp = temp.next    


class Solution:
    
    def sum(self, l1, l2):
        carry = 0
        llist1 = l1
        llist2 = l2
        sumlist = LinkedList()
        while llist1 != None or llist2 != None:
            if llist1 == None:
                temp = llist2.val + carry
            elif llist2 == None:
                temp = llist1.val + carry
            else:
                temp = llist1.val + llist2.val + carry      
            carry = 0
            if temp > 9:
                carry = int(temp / 10)
                temp = round(((temp / 10) - carry) * 10)
            
            sumlist.insert(temp)

            if llist1 != None:
                llist1 = llist1.next
            
            if llist2 != None:
                llist2 = llist2.next

        if carry != 0:
            sumlist.insert(carry)


        return sumlist

        
       
         
if __name__ == "__main__":
    LL1 = LinkedList()
    LL1.insert(1)
    LL1.insert(2)
    LL1.insert(5)


    LL2 = LinkedList()
    LL2.insert(4)
    LL2.insert(2)
    LL2.insert(6)
    LL2.insert(8)
   


    s = Solution()
    sumlist = s.sum(LL1.listHead(), LL2.listHead())
    sumlist.printList()

    
