class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
         sentence = sentence.split(" ")
        for i, word in enumerate(sentence):
            for j in xrange(1, 100):
                if word[:j] in dict:
                    sentence[i] = word[:j]
                    break
        return " ".join(sentence)