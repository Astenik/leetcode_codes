def roman_to_int(number: str):
       _sum = 0
       if 'V' in number:
           ind = number.find('V')
           if number[ind - 1] == 'I':
               _sum += 4 
               number = number.replace("IV",'')
           else: 
                _sum += 5 
                number = number.replace('V', '')
       for ind in range(len(number)):
           if number[ind] == 'X':
               if (ind != 0) and (number[ind - 1] == 'I'):
                  _sum += 9
               elif (ind != len(number) - 1) and (number[ind + 1] == 'L'):
                  _sum += 40 
               elif (ind != len(number) - 1) and number[ind + 1] == 'C':
                  _sum += 90 
               else:
                   _sum += 10 
           elif number[ind] == 'C':
               if (ind != len(number) - 1) and number[ind + 1] == 'D':
                  _sum += 400 
               elif  (ind != len(number) - 1) and number[ind + 1] == 'M':
                  _sum += 900 
               else:
                  _sum += 100
           elif number[ind] == 'I':
               _sum += 1 
           elif number[ind] == 'M':
               _sum += 1000 
           elif number[ind] == 'L':
               _sum += 50 
           elif number[ind] == 'D':
               _sum += 500 
       return _sum 

print(roman_to_int('IVXXC'))
