class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_rev = digits[::-1] 
        carry = 0
        digits_rev[0] += 1
        for i in range(len(digits_rev)-1):
            if(digits_rev[i] > 9 ):
                carry = digits_rev[i]//10
                digits_rev[i+1] = digits_rev[i+1] + carry
                digits_rev[i] = digits_rev[i] % 10
        if(digits_rev[-1] > 9):
            while(digits_rev[-1] > 9):
                carry = digits_rev[-1]//10
                digits_rev.append(carry)
                digits_rev[-2] = digits_rev[-2] % 10
        return digits_rev[::-1]