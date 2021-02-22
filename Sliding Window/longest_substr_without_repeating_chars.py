'''
Given a string, find the longest substr without repeating characters
'''
# time - O(n) - one pass 
# space - O(m) - m distinct chars

def longest_substr_without_rep_chars(s):
    start = 0
    end = 0
    count = 0
    store = {}
    while end < len(s):
        if s[end] in store and d[s[end]] >= start:
            start = d[s[end]] + 1

        count = max(count, end - start + 1)
        d[s[end]] = end
        end += 1

    return count
