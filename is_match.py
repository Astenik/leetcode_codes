def is_match(self: str, p: str):
      '''Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        The matching should cover the entire input string (not partial).
        Example 1:
        Input: s = "aa", p = "a"
        Output: false
        Explanation: "a" does not match the entire string "aa".'''
      if self == p:
         return True
      i = 0
      while (i < len(p)) and (self[i] == p[i]):
            i += 1 
      if  i  == len(p):
           return False
      if ('*' in p[i:]) and (len(p[i:]) == 1):
          return True 
      elif (p[i:] == '.')  and (len(self[i:]) == 1):
           return True
      elif (p[i:] == '.*') and (len(self[i:]) >= 1):
           return True 
      else:
           return False 

print(is_match('ab', 'a.'))
