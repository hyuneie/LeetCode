class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsList = list(jewels)
        stonesList = list(stones)
        Counts = collections.Counter(stonesList)
        print(Counts.items())
        Answer = 0
        for stone in stonesList:
            if stone in jewelsList:
                Answer += 1
        return Answer