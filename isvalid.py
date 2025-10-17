class Solution:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid using a stack-based approach.
    """
    def isValid(self, s: str) -> bool:
        # A list to serve as the stack (LIFO data structure)
        stack = []
        
        # A map to store the corresponding open bracket for each close bracket
        # This is used for quick and correct matching.
        mapping = {
            ")": "(", 
            "}": "{", 
            "]": "["
        }
        
        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                
                # Pop the top element if the stack isn't empty, otherwise use a placeholder '#'.
                # The placeholder handles the case of an unmatched closing bracket (e.g., "}")
                top_element = stack.pop() if stack else '#'
                
                # Check for a mismatch: 
                # The popped element (top_element) must be the correct opening bracket 
                # corresponding to the current closing bracket (mapping[char]).
                if top_element != mapping[char]:
                    return False
            
            # If the character is an opening bracket, push it onto the stack
            else:
                stack.append(char)
                
        # After iterating through the string, the stack must be empty.
        # If it's not empty, it means there are unclosed open brackets (e.g., "([").
        # 'not stack' returns True if the stack is empty, and False otherwise.
        return not stack