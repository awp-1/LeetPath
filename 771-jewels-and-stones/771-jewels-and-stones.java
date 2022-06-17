class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int count=0;
        Set<Character> ob=new HashSet<Character>();
        for(int i=0;i<jewels.length();i++)
        {
            ob.add(jewels.charAt(i));
        }
        for(int i=0;i<stones.length();i++)
        {
            if(ob.contains(stones.charAt(i)))
                count++;
        }
        return count;
        
    }
}