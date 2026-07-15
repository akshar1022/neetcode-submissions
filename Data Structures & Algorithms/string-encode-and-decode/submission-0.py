class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        salt="5478"
        for s in strs:
            res+=s
            res+=salt
        return res


    def decode(self, s: str) -> List[str]:
        salt="5478"
        res=s.split(salt)
        res.pop()
        return res
