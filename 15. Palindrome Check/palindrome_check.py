'''
given a string s, check if the string is a palindrome or not
'''

# two pointe approach
# time - O(n) | Space - O(1)
def isPalindrome(s):
    leftIdx = 0
    rightIdx = len(s)-1
    while leftIdx < rightIdx:
        if s[leftIdx] != s[rightIdx]:
            return False
        leftIdx = leftIdx + 1
        rightIdx = rightIdx - 1
    return True

# using stack
# time - O(n) | Space - O(n)
def isPalindrome(s):
    stack = []
    for ch in s:
        stack.append(ch)
    
    for ch in s:
        if ch != stack.pop():
            return False
    return True

# time - O(n^2) | Space - O(n)
def isPalindrome(s):
    reversedString = ''
    for i in reversed(range(len(s))):
        reversedString += s[i]
    return reversedString == s

# time - O(n) | Space - O(n)
def isPalindrome(s):
    reversedChars = []
    for i in reversed(range(len(s))):
        reversedChars.append(s[i])
    return s == "".join(reversedChars)

# time - O(n) | Space - O(n)
def isPalindrome(s, i=0):
    j = len(s) - 1 - i
    return True if i>=j else s[i] == s[j] and isPalindrome(s, i+1)
