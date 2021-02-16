class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_alt = 0
        highest_alt = cur_alt
        for i in range (len(gain)):
            cur_alt += gain[i]
            if cur_alt > highest_alt:
                highest_alt = cur_alt
        return highest_alt
    

