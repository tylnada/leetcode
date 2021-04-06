# two hash maps

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        map_pat = {}
        map_word = {}
        if len(words) != len(pattern):
            return False

        for pat, word in zip(pattern, words):
            if pat not in map_pat:
                map_pat[pat] = word
                if word not in map_word:
                    map_word[word] = pat
                else:
                    if map_word[word] != pat:
                        return False
            else:
                if map_pat[pat] != word:
                    return False
        return True
      
      
#genius solution
class Solution:
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
  
#genius 2nd
class Solution:
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return list(map(s.find, s)) == list(map(t.index, t))
