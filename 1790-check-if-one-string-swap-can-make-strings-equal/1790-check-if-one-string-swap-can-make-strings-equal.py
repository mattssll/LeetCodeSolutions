class Solution:
    
            
    def areAlmostEqual(self, s1: str, s2: str) -> bool:    
        
        # our helper function that actually solves the issue
        def checker(s1: str, s2: str, is_sorted: bool) -> bool:
            comparison_check_value = 0 if is_sorted else 2
            distinct_letters = 0
            for i in range(len(s1)):

                if s1[i] != s2[i]:
                    distinct_letters += 1
                else:
                    continue

            if distinct_letters <= comparison_check_value:
                return True
            else:
                return False
        
        # checking results
        max_one_swap = checker(s1, s2, False)
        no_different_letters = checker(sorted(s1), sorted(s2), True)
        
        if max_one_swap and no_different_letters:
            return True
        else:
            return False
        
        
        
        
        
        