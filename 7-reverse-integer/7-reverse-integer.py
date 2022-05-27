class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x = x[::-1]
        if x[len(x)-1] == '-':
            x ='-' + x[:len(x)-1]
        x = int(x)
        if x >= 2 ** 31 - 1 or x <= -2 ** 31:      
            return 0 
        
        else:               
            return x
        
        
        
        
        # if x < 0:
        #     x= -1*x
        #     x = str(x)
        #     x= x[::-1]
        #     return -1*int(x) if -1*int(x) > -2**32 else 0
        # else:
        #     x = str(x)
        #     x= x[::-1]
        #     return int(x) if int(x)< 2 ** 31 - 1 else 0     
        