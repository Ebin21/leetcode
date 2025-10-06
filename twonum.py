# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Initialize a dummy head node and a current pointer
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop through both lists and the carry
        while l1 or l2 or carry:
            
            # Get the values of the current nodes or 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and new carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            new_digit = total_sum % 10
            
            # Create a new node and append it to the result list
            current.next = ListNode(new_digit)
            
            # Move the current pointer to the new node
            current = current.next
            
            # Move the pointers for l1 and l2 to the next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # Return the head of the resulting linked list, skipping the dummy head
        return dummy_head.next