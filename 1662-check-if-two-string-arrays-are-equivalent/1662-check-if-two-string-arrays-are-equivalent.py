class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        str1=""
        str2=""

        for i in range(len(word1)):
            str1+=word1[i]

        for i in range(len(word2)):
            str2+=word2[i]
            
        return str1==str2