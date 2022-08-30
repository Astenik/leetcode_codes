def max_area(highs: list):
      '''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith
          line are (i, 0) and (i, height[i]).
          Find two lines that together with the x-axis form a container, such that the container contains the most water.
          Return the maximum amount of water a container can store.
          Notice that you may not slant the container.'''
      res = []
      for i in range(len(highs)):
        for j in range(i + 1, len(highs)):
             area = min(highs[i], highs[j])*(j - i)
             res.append(area) 
      _max = res[0] 
      for num in res:
         if num > _max:
             _max = num 
      return _max

print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
