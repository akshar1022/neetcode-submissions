class Solution:
    def isValid(self, s: str) -> bool:
        track=[]
        if(s[0]==']' or s[0]=='}' or s[0]==')'):
            return False

        for i in s:
            if(len(track)==0):
                if(i==']' or i=='}' or i==')'):
                    return False

            if(i=='[' or i=='{' or i=='('):
                track.append(i)
            else:
                if(i==']'):
                    if(track[-1]=='['):
                        track.pop()
                    else:
                        return False
                if(i=='}'):
                    if(track[-1]=='{'):
                        track.pop()
                    else:
                        return False 
                if(i==')'):
                    if(track[-1]=='('):
                        track.pop()
                    else:
                        return False     
        if(len(track)==0):
            return True
        else:
            return False



        