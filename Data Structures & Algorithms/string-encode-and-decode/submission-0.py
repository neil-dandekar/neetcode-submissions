class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for s in strs:
            encoded += str(len(s)) + '|' + s

        # print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        
        i = 0
        decoded = []
        print(s)
        while i < len(s):
            num = ''

            while i < len(s) and s[i] != '|':
                num += s[i]
                i += 1

            # print(num)
            num = int(num)


            i += 1
            word = s[i:i+num]
            # print(word)
            decoded.append(word)
            
            i = i+num

        return decoded



