def pascal_triangle(n):
   trow = [1]
   y = [0]
   for _ in range(max(n, 0)):
      print(trow)
      trow=[l + r for l, r in zip(trow+y, y+trow)]
   return n >= 1
n = int(input())
pascal_triangle(n) 