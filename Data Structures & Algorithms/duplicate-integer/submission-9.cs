public class Solution {
    public bool hasDuplicate(int[] nums) {
      int n=nums.Length;
      HashSet<int> seen= new HashSet<int>();
      foreach(int num in nums){
        if(seen.Contains(num)){
            return true;
        }
        seen.Add(num);
      }
      return false;
    }
}