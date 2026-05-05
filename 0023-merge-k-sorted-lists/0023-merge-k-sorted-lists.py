# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # If no lists are given
        if not lists:
            return None

        # Keep merging lists in pairs until only one sorted list remains
        while len(lists) > 1:
            merged_lists = []

            # Take 2 lists at a time: 0&1, 2&3, 4&5...
            for i in range(0, len(lists), 2):
                l1 = lists[i]

                # If odd number of lists, last list has no pair
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                # Merge the two sorted lists and store result
                merged_lists.append(self.mergeTwoLists(l1, l2))

            # Replace old list collection with newly merged lists
            lists = merged_lists

        # Only one merged sorted list remains
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        # Dummy node avoids edge cases for first node
        dummy = ListNode(0)
        tail = dummy

        # Compare nodes from both lists
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            # Move tail forward
            tail = tail.next

        # Attach remaining nodes
        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next