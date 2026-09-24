class Solution:

    def encode(self, strs: List[str]) -> str:
        number=''
        for words in strs:
            number += f'{len(words)}#{words}'
        return number

    def decode(self, s: str) -> List[str]:
        str_length=0
        start=0
    
        decoded=[]
        while start<len(s):
              for i in range(start,len(s)):
                  if s[i] == '#':
                     str_length = int(s[start:i])
                     word_start=i+1
                     word_end=word_start+str_length
                     start=word_end
                     decoded.append(s[word_start:word_end])
                     break
                
        return decoded
