class Solution:
    
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
    
        def bool_distinct_letters(s1: str, s2: str, is_sorted: bool) -> bool:
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

        
        distinct_letters = bool_distinct_letters(s1, s2, False)
        sorted_distinct_letters = bool_distinct_letters(sorted(s1), sorted(s2), True)
        
        if distinct_letters and sorted_distinct_letters:
            return True
        else:
            return False
        
        
        
        