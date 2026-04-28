class Solution(object):
    def groupAnagrams(self, strs):
        main_list = []
        set_a = set()
        
        for i in range(len(strs)):
            if i in set_a:
                continue
                
            inter_list = []
            # Pre-sort the "anchor" word once
            sorted_i = sorted(strs[i])
            
            for j in range(i, len(strs)):
                if j in set_a:
                    continue
                
                # Compare sorted characters instead of rotations
                if len(strs[i]) == len(strs[j]) and sorted_i == sorted(strs[j]):
                    inter_list.append(strs[j])
                    set_a.add(j)
                    
            if inter_list:
                main_list.append(inter_list)

        return main_list
