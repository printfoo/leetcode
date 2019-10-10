"""
Solution for Integer to English Words.

Idea:
Recursion.
Note: "Thousand Million Billion" can appear only once.
Note: "Hundred" can appear multiple times.
"""

# Solution.
class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        to20 = " One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split(" ")
        to100 = "  Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split(" ")
        to1b = "Billion Million Thousand"
        
        def get_words(num):
            if num < 20:
                return to20[num]
            elif num < 100:
                return " ".join([to100[num//10], to20[num%10]]).strip()
            elif num < 1000:
                return " ".join([to20[num//100], "Hundred", get_words(num%100)]).strip()
            else:
                for power, scale in zip([9, 6, 3], to1b.split(" ")):
                    if num >= 10**power:
                        return " ".join([get_words(num//10**power), scale, get_words(num%10**power)]).strip()
                
        words = get_words(num)
        return words.strip() if words else "Zero"
        

# Main.
if __name__ == "__main__":
    num = 1234567891
    print(Solution().numberToWords(num))
