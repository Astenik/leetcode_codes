def is_palindrome(sentence):
        return sentence == sentence[::-1]
def longest_palindrome(s):
     res = []
     i = 0
     while i < len(s):
         k = i
         string = ''
         while is_palindrome(string) and i < len(s):
              string += s[i] 
              i += 1
         if is_palindrome(string):
              res.append(string)
         else:
              res.append(string[:-1])
         i = k + 1
     _max = res[0]
     print(res)
     for num in res:
        if len(num) > len(_max):
             _max = num 
     return _max 
string = input("insert string: ")
print(f"longest palindrome substring is: {longest_palindrome(string)}")
