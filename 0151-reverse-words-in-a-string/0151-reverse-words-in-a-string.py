class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words.reverse()
        cleaned = [x for x in words if x.strip()]
        return " ".join(cleaned).strip()
        