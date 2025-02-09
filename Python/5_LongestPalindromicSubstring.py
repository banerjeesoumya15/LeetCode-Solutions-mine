#Difficulty = Medium
#Submission Speed = 48.40%
'''
Before Jumping onto Solution, know that:
=>Palindromes are of two types: Odd Palindromes (length is odd) and Even Palindrome (length is even)
=>We traverse the array, and for every element, we suppose that current element is the middle element and check for the largest palindromic
  substring that can be made which has middle element as the current element.
Note that, In case of even palindrome, there are two middle elements.
=> We check for both Odd and even Palindromes
=> How to check for largest palindromic substring with given middle element?
    we maintain two pointers left and right.
    Initialize them with current index (middle element index) and In every loop we check s[left]==s[right] (and check for 
    boundary errors too, left and right dont go out of the size of array or 0). In the body of the loop we decrease the left
    and increase the right pointer.
'''
'''
Time Complexity =  O(N^2)
Space Complexity = O(N)
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        size = len(s)
        for i in range(size):
            #Odd Palindrome
            left,right = i,i
            ls = ""
            while 0<=left<size and 0<=right<size and s[left]==s[right]:
                if left==right:
                    ls = s[left]
                else:
                    ls = s[left] + ls + s[right]
                left-=1
                right+=1
            #Even Palindrome
            left,right = i,i+1
            rs = ""
            while 0<=left<size and 0<=right<size and s[left]==s[right]:
                rs = s[left] + rs + s[right]
                left-=1
                right+=1
            temp = ls if len(ls)>len(rs) else rs
            longest = temp if len(temp)>len(longest) else longest
        return longest
      
'''
My Submission
https://leetcode.com/problems/longest-palindromic-substring/
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if s == s[::-1]:
            return s
        
        longest = ""
        
        for i in range(len(s)):
            
            # odd palindrome
            l = r = i
            odd_p = s[i]
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if l==r:
                    odd_p = s[l]
                else:
                    odd_p = s[l] + odd_p + s[r]
                l-=1
                r+=1
                
            longest = odd_p[:] if len(odd_p) > len(longest) else longest[:]
            #len_odd = l-r+1
            
            # even palindrome
            l = i
            r = i+1
            even_p = ""
            while(l>=0 and r<len(s) and s[l]==s[r]):
                even_p = s[l] + even_p + s[r]
                l-=1
                r+=1
                
            longest = even_p[:] if len(even_p) > len(longest) else longest[:]
            #len_even = l-r+1
            
        return longest
            
            
        
