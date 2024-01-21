#  Pascal's Triangle

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
 1
 11
 121
 1331
 14641
 15101051
# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]

class Solution(object):
    def create(self,triangle,pre,i,n):
        if i>=n:
            return 
        demo=[1]*(i+1)
        j=0
        k=1
        while j+1<len(pre):
            demo[k]=pre[j]+pre[j+1]
            j+=1
            k+=1
        i+=1
        triangle.append(demo)
        self.create(triangle,triangle[-1],i,n)
        return triangle

    def generate(self, numRows):
        triangle=[]
        pre=[]
        i=0
        return self.create(triangle,pre,i,numRows)