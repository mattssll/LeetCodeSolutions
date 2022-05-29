class Solution:
    
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
    
        def bool_distinct_letters(s1: str, s2: str) -> bool:
            distinct_letters = 0
            for i in range(len(s1)):

                if s1[i] != s2[i]:
                    distinct_letters += 1
                else:
                    continue

            if distinct_letters <= 2:
                return True
            else:
                return False

        def sorted_distinct_letters(s1: [str], s2: [str]) -> bool:
            distinct_letters = 0
            for i in range(len(s1)):

                if s1[i] != s2[i]:
                    distinct_letters += 1
                else:
                    continue

            if distinct_letters <= 0:
                return True
            else:
                return False


            if len(s1) != len(s2):
                return False
        
        distinct_letters = bool_distinct_letters(s1, s2)
        sorted_distinct_letters = sorted_distinct_letters(sorted(s1), sorted(s2))
        
        if distinct_letters and sorted_distinct_letters:
            return True
        else:
            return False
        
        