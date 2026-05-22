class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):

        a = headA
        b = headB

        while a != b:

            if a:
                a = a.next
            else:
                a = headB

            if b:
                b = b.next
            else:
                b = headA

        return a

common = ListNode(7)
common.next = ListNode(8)

headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = common

headB = ListNode(3)
headB.next = common

sol = Solution()

intersection = sol.getIntersectionNode(headA, headB)

if intersection:
    print("Intersection at node with value:", intersection.val)
else:
    print("No intersection")