class Solution:
    def largestMerge(self, word1, word2):
        merge = ""
        while len(word1) != 0 and len(word2) != 0:
            if word1 >= word2:
                list_word = list(word1)
                merge += list_word.pop(0)
                word1 = ''.join(list_word)
            else:
                list_word = list(word2)
                merge += list_word.pop(0)
                word2 = ''.join(list_word)
        if len(word1) == 0:
            merge += word2
        else:
            merge += word1
        return merge
