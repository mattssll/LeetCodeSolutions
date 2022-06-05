class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = []
        for idx,char in sorted(zip(indices, s)):
            arr.append(char)
        return "".join(arr)