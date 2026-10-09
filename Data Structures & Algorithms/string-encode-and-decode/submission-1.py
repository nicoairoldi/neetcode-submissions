class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"
        return encoded
    def decode(self, s: str) -> List[str]:
        word_list = []
        i = 0
        while i < len(s):
            split = s.find('#', i)
            print(i)
            print(split)
            num_index = s[i:split]
            print(f"num:{num_index}")
            num = int(num_index)
            word = s[split+1:split+1+num]
            i = split + 1 + num
            print(word)
            word_list.append(word)
        return word_list

