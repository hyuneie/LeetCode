class Solution:
    def minimumSum(self, num: int) -> int:
        numList = [ int(i) for i in list(str(num))]
        print(numList)
        # Greedy algorithm
        numList.sort() 
        SecondDigit1 = numList[0] #2 
        SecondDigit2 = numList[1] #2
        #10의자리수
        SecondDigit = (SecondDigit1 + SecondDigit2) * 10 
        FirstDigit1 = numList[2]
        FirstDigit2 = numList[3]
        #1의자리수
        FirstDigit = FirstDigit1 + FirstDigit2
        return SecondDigit + FirstDigit