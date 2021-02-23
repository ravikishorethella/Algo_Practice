
'''
Given a string, find the longest substr with atmost 2 distinct chars
'''
# time - O(n)
# space - O(1) - at max we will store the 3 elements in the dict

def longest_substr_with_2_distinct_chars(s):
    store = {}
    maxLength = 0
    count = 0
    start = 0

    for end in range(len(s)):
        # store the chars in the dict
        store[s[end]] = store.get(s[end], 0) + 1

        # if the store[s[end]] == 1, then we have a unique char
        if store[s[end]] == 1:
            count += 1

        # if the count > 2 then we have to move start and decrement the count
        while count > 2:
            store[s[start]] -= 1
            if store[s[start]] == 0:
                count -= 1
            start += 1

        maxLength = max(maxLength, end - start + 1)

    return maxLength


print(longest_substr_with_2_distinct_chars("ecceba"))
