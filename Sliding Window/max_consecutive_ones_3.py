'''
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s. 
'''

# time - O(n)
# space - O(1)

def longestOnes(A, K):
  maxCount = 0
  zeroCount = 0
  start = 0

  # sliding window end starts from 0
  for end in range(len(A)):
      if A[end] == 0:
          zeroCount += 1

      while zeroCount > K:
          if A[start] == 0:
              zeroCount -= 1
          start += 1

      maxCount = max(maxCount, end - start + 1)

  return maxCount
