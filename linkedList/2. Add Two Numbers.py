from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    primer = 0

    while l1 or l2:
        if l1 and l2:
            temp = l1.val + l2.val + primer
            l1 = l1.next
            l2 = l2.next
        elif l1:
            temp = l1.val + primer
            l1 = l1.next
        else:
            temp = l2.val + primer
            l2 = l2.next

        if temp >= 10:
            temp %= 10
            primer = 1
        else:
            primer = 0

        curr.next = ListNode(val=temp)
        curr = curr.next

    if primer != 0:
        curr.next = ListNode(val=1)

    return dummy.next
