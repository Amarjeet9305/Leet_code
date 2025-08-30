import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = []
        # Push all heads into heap (store as tuple (val, index, node))
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        
        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# ---------------- DRIVER CODE ----------------
def build_linked_list(arr):
    """Helper to convert array to linked list"""
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    """Helper to print linked list"""
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


if __name__ == "__main__":
    # Example input: k sorted lists
    l1 = build_linked_list([1,4,5])
    l2 = build_linked_list([1,3,4])
    l3 = build_linked_list([2,6])

    lists = [l1, l2, l3]

    solution = Solution()
    merged_head = solution.mergeKLists(lists)

    print("Merged Linked List:")
    print_linked_list(merged_head)

