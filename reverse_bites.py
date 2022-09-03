def reverse_bites(number: str):
      '''this function reverses bites of a given 32 bites unsigned integer.'''
      lst = []
      for i in range(len(number) - 1, 0, -1):
           lst.append(number[i])
      n = len(lst)
      res = 0
      for num in lst:
         res += int(num) * 2**n 
         n -= 1 
      return res 
number = '00000010100101000001111010011100'
print(f"your reversed number is: {reverse_bites(number)}")
