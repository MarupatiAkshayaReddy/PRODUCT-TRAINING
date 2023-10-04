class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(s,opencount=0,closecount=0):
            if opencount==closecount==n:
                res.append(s)
            if opencount<n:
                l.append(s+'(',opencount+1,closecount)
            if closecount<opencount:
                backtrack(s+')',opencount,closecount+1)
            return res
        return backtrack(s="")
obj=Solution()
obj.generateParenthesis()

            
        

    
