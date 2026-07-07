class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: 1 way to climb 1 step, 2 ways to climb 2 steps.
        if n <= 2:
            return n
        
        # Variables to store the previous two results
        two_steps_behind = 1
        one_step_behind = 2
        
        # Calculate ways for steps 3 up to n
        for _ in range(3, n + 1):
            current = one_step_behind + two_steps_behind
            
            # Shift our variables forward for the next iteration
            two_steps_behind = one_step_behind
            one_step_behind = current
            
        return one_step_behind