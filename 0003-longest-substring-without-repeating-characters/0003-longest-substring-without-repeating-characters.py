class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen=set()
        left=0
        max_len=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            max_len=max(max_len,right-left+1)
        return max_len
#If an interviewer asks:

#"Why isn't this O(n²)? There's a while loop inside a for loop."

#"Although there's a while loop inside the for loop, the left pointer never moves backward. Each character is added to the set once and removed once. Therefore, both left and right together perform at most 2n moves, which is O(n). The set provides average O(1) lookup, insertion, and deletion."