class Solution(object):
    def checkString(self, s):
        
        cond  = False

        for x in s:
            if x == "a": 
                if cond:
                    return False
            else:
                cond = True     
        return True