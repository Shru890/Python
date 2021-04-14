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

#Number of 1 Bits
class Solution:
	def setBits(self, N):
		# code here
		count=0
		N=bin(N).replace("0b", "")
		for i in N:
		    if i=="1":
		        count+=1
		return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)
