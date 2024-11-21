
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = ListNode(1)
n2 = ListNode(2)
head.next = n2
tem = ListNode(head.val)
tem.next = head.next
head = head.next
tem.next = None


head.next = tem

# print(Solution().letterCombinations("23"))