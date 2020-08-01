# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0

        sum = l1.val + l2.val

        if sum >= 10:
            sum = sum - 10
            carry = 1

        result = ListNode(sum)

        last = result

        l1 = l1.next
        l2 = l2.next

        while l1 == None and l2 == None:
            sum = l1.val + l2.val + carry
            carry = 0 
            if sum >= 10:
                sum = sum - 10
                carry = 1

            node = ListNode(sum)
            last.next = node
            last = node
            
            l1 = l1.next
            l2 = l2.next

        if carry == 1:
            node = ListNode(carry)
            last.next = node
            last = node

        return result



a = ListNode(2)
b = ListNode(4)
c = ListNode(3)

a.next = b
b.next = c


x = ListNode(5)
y = ListNode(6)
z = ListNode(4)

x.next = y
y.next = z

sol = Solution()
r = sol.addTwoNumbers(a,x)

print(r.next.val)
while(r != None):
    print(r.val)
    r = r.next

        