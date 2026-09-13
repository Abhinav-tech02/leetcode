class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cow, bull = 0, 0
        digits1 = list(secret)
        digits2 = list(guess)

        for i in range(len(digits1)):
            for j in range(len(digits2)):
                if digits1[i] == digits2[j] and i == j:
                    bull += 1
                    digits1[i] = None
                    digits2[j] = None
                    break

        for i in range(len(digits1)):
            if digits1[i] is None:
                continue
            for j in range(len(digits2)):
                if digits2[j] is None:
                    continue
                if digits1[i] == digits2[j]:
                    cow += 1
                    digits2[j] = None  
                    break

        return str(bull) + 'A' + str(cow) + 'B'