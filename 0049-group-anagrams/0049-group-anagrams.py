from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for word in strs:
            count = [0]*26 #letter:  a b c d e f g h i j k ...
                            #index:   0 1 2 3 4 5 6 7 8 9 10 ...
                            #count:   0 0 0 0 0 0 0 0 0 0 0 ...
            for char in word :
                count[ord(char) - ord('a')]+=1 # At this point count is a list [1,000,1]
            key = tuple(count)
            hmap[key].append(word)

        return list(hmap.values())

    #For every word:

    #Make empty buckets

    #Count the letters

    #Turn buckets into a fingerprint

    #Put word in the matching box
