class Solution(object):
    def __init__(self):
        self.negativeFlag = False
        
    def reverse(self, num):
        if (num < 0):
            self.negativeFlag = True
            num = -num
        
        prev_rev_num = 0
        rev_num = 0
        while (num != 0): 
            curr_digit = num % 10
            rev_num = (rev_num * 10) + curr_digit
    
            if (rev_num >= 2147483647 or
                rev_num <= -2147483648):
                rev_num = 0
            if ((rev_num - curr_digit) // 10 != prev_rev_num):
                return 0
            
            prev_rev_num = rev_num
            num = num //10
        
        return -rev_num if (self.negativeFlag == True) else rev_num

    