#Swap two numbers
#User function Template for python3
class Solution:
    def get(self, a, b):
        #code here
        temp=a
        a=b
        b=temp
        s=[a,b]
        return s

#{ 
#Driver Code Starts.
if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		a,b = map(int,input().strip().split())
		ob = Solution()
		ans=ob.get(a,b)
		print(str(ans[0])+" "+str(ans[1]))
#} Driver Code Ends
