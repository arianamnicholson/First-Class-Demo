#excersise 1
water_per_person = 20 
if water_per_person > 19 :
  print water_per_person, ': post emergency levels'
#excersise 2
x=12
if x % 2 == 0:
 print ("x is even.")
else:
  print("x is odd.")
#excersise 3
def even_odd(x):
  if x % 2 == 0:
    print ("x is even.")
  else:
    print("x is odd.")
even_odd(12)
#excersise 4
def ifequal (x, y):
  if x < y:
   print ("x is Less")
  elif x == y:
    print ("Equal")
  else:
    print ("Y is Greater" )
ifequal(5, 10)
#excersise 5
def countdown(n):
  if n == 0:
    print ('Blastoff!')
  else:
    print (n)
    countdown (n-1)
countdown (10)
#excersise 6
def cube(num) :
  return num*num*num
print cube(3)
def sumInt(num):
  if num == 0:
    return 0
  else: 
    return num + sumInt(num - 1)
print sumInt(0)
