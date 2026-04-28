class Solution(object):
    def groupAnagrams(self, strs):
        # Using a dictionary to group by the sorted string (the 'key')
        groups = {}
        
        for s in strs:
            # 1. Sort the string to create a universal key for all its anagrams
            # e.g., "stop", "pots", and "tops" all become "opst"
            key =str(sorted(s))
            
            # 2. Add the original string to its corresponding group
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
            
        # 3. Return all the grouped lists
        return list(groups.values())
