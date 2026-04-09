class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for score in operations:
            if score == "+":
                curr_value = stack[-1]+stack[-2]
                stack.append(int(curr_value))
            elif score == "C":
                stack.pop()
            elif score == "D":
                curr_value = 2*stack[-1]
                stack.append(int(curr_value))
            else:
                stack.append(int(score))
        
        return sum(stack)