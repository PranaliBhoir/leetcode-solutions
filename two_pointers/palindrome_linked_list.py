#https://leetcode.com/problems/palindrome-linked-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):

        values = []

        current = head

        # Convert linked list to array
        while current:
            values.append(current.val)
            current = current.next

        left = 0
        right = len(values) - 1

        while left < right:

            if values[left] != values[right]:
                return False

            left += 1
            right -= 1

        return True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

sol = Solution()

print(sol.isPalindrome(head))