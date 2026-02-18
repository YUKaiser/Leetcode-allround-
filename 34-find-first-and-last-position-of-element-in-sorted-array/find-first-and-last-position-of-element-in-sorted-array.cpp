class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
       int n=nums.size();
       int startind=-1,endind=-1;
       for(int i=0;i<n;i++){
        if(nums[i]==target){
            if(startind==-1)
             startind=i;
           endind=max(endind,i);
        }
       }
       vector<int> ans={startind,endind};
       return ans; 
    }
};