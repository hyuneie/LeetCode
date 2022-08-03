class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
#         words = paragraph.lower().split(' ')
        
#         wordlist = []
#         for s in words:
#             wordlist.append(''.join(filter(str.isalnum,s )))
        
#         print(wordlist)
        
#         for ban in banned:
#             while ban in wordlist:
#                 wordlist.pop(wordlist.index(ban))
                
#         return max(wordlist, key=wordlist.count)
    
            # 정규표현식으로 문자열이 아닌것들 모두 띄어쓰기로 바꿔주기
        paragraph = re.sub('[^\w]+', ' ', paragraph.lower())
        # list comprehension을 활용하여, banned에 포함되지 않는 것들을 list로 변환 후 collections.Counter 함수를 활용
        myCounter = collections.Counter([Word for Word in paragraph.split() if Word not in banned])
        # 가장 common한 단어 뽑기
        return myCounter.most_common(1)[0][0]