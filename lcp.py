#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        str1=max(arr)
        str2=min(arr)
        pre=""
        for i in range(len(str2)):
            if str2[i]!=str1[i]:
                break;
            else:
                pre+=str2[i]
        
        if len(pre)==0:
            return -1
        else:
            return pre

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends