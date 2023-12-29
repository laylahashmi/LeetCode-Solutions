class Solution:
    def isValid(self, s: str) -> bool:
        '''
        1. create an empty stack
        2. create an object relating opening and closing brackets
        3. check and see if the char in s is in closing brackets
            - if it is, this means its a closing bracket
                -check if the last item in the stack is the open bracket for the closed one
                    - if it is, then remove the open bracket from the stack
                    - if not, then return False bc the string is not valid
            - if not, then it is an opening bracket and we need to add it to our stack
        4. if the stack is empty, return True, if its not empty return False
        '''
        
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
        
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False