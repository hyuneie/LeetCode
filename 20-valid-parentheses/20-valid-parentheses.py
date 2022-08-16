class Solution:
    def isValid(self, s: str) -> bool:
        InputList = list(s)
        Stack = []
        for Input in InputList:
            if Input in ['(', '{', '[']: #open 이라면
                Stack.append(Input)
            else: #Close라면
                if len(Stack) == 0:
                    return False
                if Stack[len(Stack)-1] == '(' and Input == ')':
                    Stack.pop()
                elif Stack[len(Stack)-1] == '{' and Input == '}':
                    Stack.pop()
                elif Stack[len(Stack)-1] == '[' and Input == ']':
                    Stack.pop()
                else:
                    return False
        if len(Stack) > 0:
            return False
        return True