string = input("insert the string: ")
def longest_substring_without_repeating_chars(s):
      '''Given a string s, thif function finds 
      the length of the longest substring without repeating characters.'''
      name = ''
      res = [ ]
      i = 0
      while i < len(s):
         for ii in range(i, len(s)):
            if not string[ii] in name:
               name += string[ii] 
            else:
                i = ii + 1
                break
         res.append(len(name))
         i += 1
      _max = res[0]
      for num in res:
         if num > _max:
            _max = num 
      return _max 
print(f'length of the longest substring without repeating characters {longest_substring_without_repeating_chars(string)}')
