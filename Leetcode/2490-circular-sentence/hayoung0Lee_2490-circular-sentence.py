class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # second condition
        first = sentence[0]
        last = sentence[-1]
        if first != last:
            return False;
        
        # first condition
        words = sentence.split(" ")
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            first = w1[-1]
            last = w2[0]
            if first != last:
                return False
            
        return True