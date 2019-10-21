"""
Solution for Decode String, O(n).

Idea:
Stack.
"""

# Solution.
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = "1[" + s + "]" # formalize the string to let it start with a number
        repeat, temp, output = [""], [], ""
        for c in s:
            if c.isdigit():
                if type(repeat[-1]) == type(0): repeat.append(c) # a new number
                else: repeat[-1] += c # continue adding char to old number
            elif c == "[":
                repeat[-1] = int(repeat[-1]) # end of adding number
                temp.append("") # start adding chars
            elif c != "]":
                temp[-1] += c # continue adding chars
            elif c == "]":
                this_repeat, this_temp = repeat.pop(), temp.pop() # end adding chars, pop
                if temp: temp[-1] = temp[-1] + this_temp * this_repeat # if stack unempty
                else: output += this_temp * this_repeat # if stack empty, add output together
            else: "print invalid?"
        return output

# Main.
if __name__ == "__main__":
    s = "2[abc]3[cd]ef"
    print(Solution().decodeString(s))
