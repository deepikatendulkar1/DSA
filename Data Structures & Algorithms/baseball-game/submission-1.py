class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for op in operations:
            if op=='+':
                num1=stack.pop()
                num2=stack.pop()
                stack.append(num2)
                stack.append(num1)
                stack.append(num1+num2)
            elif op=='C':
                stack.pop()
            elif op=='D':
                nextnumber= stack.pop()
                stack.append(nextnumber)
                stack.append(2*nextnumber)
            else:
                stack.append(int(op))
        return sum(stack)