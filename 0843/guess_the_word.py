"""
Solution for Guess the Word.

Idea:
Eliminate unmatched
"""

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """

class Master:
    def __init__(self, secret):
        self.secret = secret

    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        return sum(1 for c1, c2 in zip(self.secret, word) if c1 == c2)

# solution
class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def getMatchNum(w, p): return sum(1 for c1, c2 in zip(w, p) if c1 == c2)
        possible = {w for w in wordlist}
        while possible:
            p = possible.pop()
            match = master.guess(p)
            if match == 6: return
            possible = {w for w in possible if getMatchNum(w, p) == match}
        return


# Main.
if __name__ == "__main__":
    secret = "hbaczn"
    wordlist = ["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"]
    master = Master(secret)
    print(Solution().findSecretWord(wordlist, master))
