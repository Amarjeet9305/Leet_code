#Problem Summary:You are given two linked lists (l1 and l2) representing two non-negative 
# integers in reverse order (least significant digit first). You need to return their sum 
# as a new linked list in the same reverse order format

# Approach: We simulate manual addition process like how add digits from right to left
#Initialize a dummy head node to build the result list.

#Use a pointer curr to build the resulting list.

#Initialize a variable carry = 0.

#Traverse both lists (l1, l2) while any of them is not null or carry is non-zero:

#Get val1 from l1 (0 if l1 is exhausted).

#Get val2 from l2 (0 if l2 is exhausted).

#Compute: total = val1 + val2 + carry

#Compute: digit = total % 10 and carry = total // 10

# Add a new node with value digit to the result list.

#Move l1 and l2 to their next nodes.

#After the loop, return dummy_head.next.


# Create a node on single linked list

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Corrected function outside the class
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy_head = ListNode()
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        current.next = ListNode(digit)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next

# Helper to convert list to linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    curr = dummy
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# Helper to convert linked list to list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test Case
l1 = list_to_linkedlist([2, 4, 3])  # 342
l2 = list_to_linkedlist([5, 6, 4])  # 465   

result = addTwoNumbers(l1, l2)
print(linkedlist_to_list(result))  # Output: [7, 0, 8]
