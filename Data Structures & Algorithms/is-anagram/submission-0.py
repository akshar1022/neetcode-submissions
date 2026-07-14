class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        track_list=[0]*26
        for i in s:
            track_list[ord(i)-ord('a')]+=1
        for i in t:
            track_list[ord(i)-ord('a')]-=1
        for i in track_list:
            if (i!=0):
                return False
        return True
            

        