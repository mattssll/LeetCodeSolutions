class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        match_rule = 0
        for item in items:
            dictValue = {"type" : item[0], "color" : item[1], "name" : item[2]}
            if (ruleKey, ruleValue) in dictValue.items():
                match_rule += 1
        return match_rule