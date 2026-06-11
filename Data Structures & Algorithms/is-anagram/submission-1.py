class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st=sorted(s.strip())
        tt=sorted(t.strip())
        if st==tt:
            return True
        else:
            return False
        