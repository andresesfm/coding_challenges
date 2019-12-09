from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        #Note:requirement is to use greedy algorithm
        i = 0
        reslines = []
        while i<len(words):
            s =[]
            sl = 0
            sls = 0 #string len of spaces(counting at least one space befween words)
            while i<len(words) and (sl + sls + len(words[i]))<=maxWidth:
                sls+=1
                sl += len(words[i])
                s.append(words[i])
                i+=1
            reslines.append([s[:],sl])
        res = []
        for i in range(len(reslines)):
            s,sl = reslines[i]
            spaces = [1 for i in range(len(s)-1)]+[0]
            if i != len(reslines)-1:
                scount = sum(spaces)
                while len(s)>1 and scount+sl<maxWidth:
                    for k in range(len(s)-1):
                        if scount+sl<maxWidth:
                            spaces[k]+=1
                            scount+=1
                        else:
                            break
            line = ""
            for j in range(len(s)):
                line += s[j] + (" "*spaces[j])
            line += " "*(maxWidth -len(line))
            res.append(line)
        return res

def printm(arr: List[str])-> None:
    for i in arr:
        print(i)

if __name__ == "__main__":
    s = Solution()
    printm(s.fullJustify(["What","must","be","acknowledgment","shall","be"],16))
    printm(s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20))
    printm(s.fullJustify(["Listen","to","many,","speak","to","a","few."],6))