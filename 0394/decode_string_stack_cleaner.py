"""
Solution for Decode String, O(n).

Idea:
Stack, cleaner solution.
"""

# Solution.
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, num = [["", 1]], "" # chats, nums
        for c in s:
            if c.isdigit():
                num += c # continue adding char to old number
            elif c == "[":
                stack.append(["", int(num)]) # end of adding number, start adding chars
                num = "" # reset num
            elif c != "]":
                stack[-1][0] += c # continue adding chars
            elif c == "]":
                stack_top = stack.pop() # end adding chars, pop
                stack[-1][0] += stack_top[0] * stack_top[1] # if stack
            else: "print invalid?"
        return stack[-1][0]

# Main.
if __name__ == "__main__":
    s = "2[abc]3[cd]ef"
    print(Solution().decodeString(s))
