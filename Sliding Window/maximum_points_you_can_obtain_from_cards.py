'''
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
'''

def maxScore(cardPoints, k):
  max_sum = 0
  for i in range(k):
      max_sum += cardPoints[i]

  left = len(cardPoints)
  right = k - 1

  temp_sum = max_sum

  while left != len(cardPoints) - k:
      left -= 1
      temp_sum += cardPoints[left]
      temp_sum -= cardPoints[right]
      right -= 1

      max_sum = max(temp_sum, max_sum)

  return max_sum
    
  
