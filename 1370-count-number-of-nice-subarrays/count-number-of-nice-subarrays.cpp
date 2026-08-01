class Solution {
public:
int func(vector<int>& nums, int k){
    int n=nums.size();
    int cnt=0, ans=0;
    int i=0;
    for(int j=0;j<n;j++){
        if(nums[j]%2!=0)
          cnt++;
        while(cnt>k){
            if(nums[i]%2!=0)
                cnt--;
            i++;
            }
            ans+=(j-i+1);
        }
        return ans;
}
    int numberOfSubarrays(vector<int>& nums, int k) {
    return func(nums,k)-func(nums,k-1);   
    }
};