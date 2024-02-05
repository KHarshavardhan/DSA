class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            match i:
                case '+':
                    a,b=stack.pop(),stack.pop()
                    stack.append(b+a)
                case  '-':
                    a,b=stack.pop(),stack.pop()
                    stack.append(b-a)
                case '*':
                    a,b=stack.pop(),stack.pop()
                    stack.append(b*a)
                case '/':
                    a,b=stack.pop(),stack.pop()
                    stack.append(int(b/a))
                case _:
                    stack.append(int(i))
        return stack.pop()
