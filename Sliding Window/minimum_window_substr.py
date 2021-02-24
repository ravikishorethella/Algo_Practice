'''
https://leetcode.com/problems/minimum-window-substring/
Given two strings s and t, return the minimum window in s which will contain all the characters in t. 
If there is no such window in s that covers all characters in t, return the empty string "".
'''

def minWindow(s, t):
  t_counter = Counter(t)
  chars = len(t_counter.keys())
  
  matches = 0
  answer = ''
  
  i = 0
  j = -1
  
  while i < len(s):
    # extend the window
    if matches < chars:
        if j == len(s)-1:
            return answer
        j += 1
        s_counter[s[j]] += 1
        if t_counter[s[j]] > 0 and s_counter[s[j]] == t_counter[s[j]]:
            matches += 1
    # contract
    else:
        s_counter[s[i]] -= 1
        if t_counter[s[i]] > 0 and s_counter[s[i]] == t_counter[s[i]] - 1:
            matches -= 1
        i += 1

    # compare matches with chars
    if matches == chars:
        if not answer:
            answer = s[i:j+1]
        elif j - i + 1 < len(answer):
            answer = s[i:j+1]
  return answer
  
