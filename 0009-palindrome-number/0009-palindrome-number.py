class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp= list(str(x))
        test=temp.copy()
        temp.reverse()
        print(temp)
        print(test)
        if temp==test:
            return True
        return False
        