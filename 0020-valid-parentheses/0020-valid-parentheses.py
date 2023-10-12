class Solution:
    def isValid(self, s: str) -> bool:
        """
        1. create an empty stack
        2. create a dict relating our closing brackets to the opening brackets
        3. loop through our string
            - determine if the char is an opening or closing bracket
            - if the char is closing, check to see if the last item added to our stack is the matching open bracket
                - if it is, remove the matching char
                - if not, return False - that means the string is not valid
            - if the char is opening, we will add it to our stack
        4. if the stack is empty, we will return True otherwise return False
        """
        
        stack = []
        closeToOpen = {"}" : "{", "]" : "[", ")" : "("}
        
        for char in s:
            if char in closeToOpen: #closing bracket
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char) #opening bracket
                
        return True if len(stack) == 0 else False