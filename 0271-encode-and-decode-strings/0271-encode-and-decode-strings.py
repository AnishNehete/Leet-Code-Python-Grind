class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_parts = [] #list to collect each encoded piece, list is efficient

        for s in strs:
            encoded_parts.append(str(len(s))+ '#' +s) #store length

        return ''.join(encoded_parts) #combine all encoded pieces into one

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []

        l = 0 #pointer to scan
        while l < len(s):
            r = l

            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            word = s[r +1:r + 1 + length]
            result.append(word)

            l =r + 1 + length #move i to the start of the next encoded string block
        return result
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))