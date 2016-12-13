import random
import math

def runFinal():
  value = True
  while value == True:
    print''
    print''
    print'#*******************************************************'
    print'# Menu Defition - input varible selection to run program'
    print'# 1 = 1000 Coin flips'
    print'# 2 = Monte Carlo for Pi'
    print'# 3 = Drunkard problem'
    print'# 4 = Arctan problem'
    print'# 5 = GCD problem'
    print'# 0 = exit the program'
    print'#*******************************************************'
    x = int(raw_input("Enter a digit from 1-5: "))
    if x == 1:
      runThis1()
    if x == 2:
      runThis2()
    if x == 3:
      runThis3()
    if x == 4:
      callArctan()
    if x == 5:
      callGCD()
    if x == 0:
      value = False
  
#*************************************
#Part 1 - 1st Exercise - 1000 coin flips
#*************************************
def thousandFlips():
  total_heads = 0
  total_tails = 0
  total_heads1 = 0
  total_tails1 = 0
  total_heads2 = 0
  total_tails2 = 0
  exactlytwoheads = 0
  count = 0
  
  while count < 3000:

    coin1 = random.randint(1, 2)
    coin2 = random.randint(1, 2)
    coin3 = random.randint(1, 2)
    
    if (coin1 == 1 and coin2 == 1) or (coin1 == 1 and coin3 == 1):
      exactlytwoheads += 1
    
    if coin1 == 1:
      
      total_heads += 1
      
      count += 1

    elif coin1 == 2:
      
      total_tails += 1
      
      count += 1
    
    if coin2 == 1:
      
      total_heads1 += 1
      
      count += 1

    elif coin2 == 2:
      
      total_tails1 += 1
      
      count += 1
      
    if coin3 == 1:
      
      total_heads2 += 1
      
      count += 1

    elif coin3 == 2:
      
      total_tails2 += 1
      
      count += 1
  print"*********************************************"
  print"Exactly two heads count = ", exactlytwoheads
  print"*********************************************"    
  print"Coin1 Head Count =",total_heads, "|| Tail Count =" ,total_tails
  print"Coin2 Head Count =",total_heads1, "|| Tail Count =" ,total_tails2
  print"Coin3 Head Count =",total_heads1, "|| Tail Count =" ,total_tails2
  print""

def runThis1():
  i = 0
  while i < 10:
    print i+1
    i = i + 1
    
    thousandFlips()

#**************************************
#Part 1 - 2nd Exercise - Monte Carlo Pi
#**************************************

def monteCarlo():
  i = 0
  trials = 0.0
  hit = 0.0
  x = 0.0
  y = 0.0
  while i < 50000:
    i = i + 1
    
    
    x = decision1()
    y = decision1()
   
   
    trials+=1
    
    if( x*x + y*y ) <= 4.0:
      
      hit+=1
   
  print 'pi/4 = ', float(hit) / float(trials)
  print 'Pi = ', 4 * float(hit) / float(trials)
  
def decision1():
  
  return random.uniform(0,2)

def runThis2():
  i = 0
  while i < 10:
    i+=1
    print''
    print i
    print '-------------------------------------'
    monteCarlo()
    print '-------------------------------------'
    print ''

#*******************************
#Part 1 - 3rd Exercise - Drunkard
#*******************************
def drunkard():
  x = 0
  y = 0
  amountOfSteps = 50
  unitsDistant = 20
  probEast = 1.0/6.0
  probNorth = 1.0/4.0
  probSouth = 1.0/4.0
  probWest = 1.0/3.0
  amountOfDrunks = 1000
  distance = 0.0
  count = 0
  count2 = 0
 
  for t in range (0, amountOfDrunks):
    x = 0
    y = 0
      
    for i in range (0,amountOfSteps):
      r = decision()
      if r > 0 and r <= probEast:
        x = x + 1
      elif r > probEast and r <= (probEast + probNorth):
        y = y + 1
      elif r > probEast + probNorth and r <= (probEast + probNorth + probSouth):
        y = y - 1
      else:
        x = x - 1

    distance = math.sqrt(x**2 + y**2)
    if(distance > 20):
      count = count + 1
  solution = (count*1.0/amountOfDrunks) * 100    

  print "**************************************************"
  print "Out of ", amountOfDrunks,"drunks", count, "will be 20 units from origin"
  print("This gives us a probability of...")
  print "%",solution
  print ""
    
      
  
def decision():
  return random.random()
  
def runThis3():
  i = 0
  for i in range(0,10):
    print(i+1)
    drunkard()
  
  
#**************************************
#Part 2 - 1st Exercise - arctan
#**************************************
import math
def arctan(x):
  a = 2**(-38/2)
  b = x/(1 + math.sqrt(1+x**2))
  c = 1.0
  d = 1.0
  holder = x
  t = 1
  while t == 1:
    

    c = (2*c) / (1 + a)
    d = (2*a*b) / (1 + b**2)
    d = d / (1 + math.sqrt(1-d**2))
    d = (b + d) / (1-b*d)
    b = d / (1 + math.sqrt(1+d**2))
    a = (2 * math.sqrt(a)) / (1 + a)

    estimated = c * math.log((1+b) / (1-b))
    actual = math.atan(x)
    absoluteError = estimated - actual


  
    if absoluteError < 0:
      absoluteError = (absoluteError * -1)
    else:
      absoluteError = absoluteError
    
    print 'atan = ', estimated, 'error is ', absoluteError 
    if (1-a) <= 2**-38:
      t = 0
def callArctan():
    print'arctan(2)'
    arctan(2)
    print'arctan(-2)'
    arctan(-2)
    print'arctan(99999)'
    arctan(99999)
#**************************************
#Part 2 - 2nd Exercise - Greatest Common Divisor
#**************************************  
    
def gCommonDiv(a, b):
    aholder = a
    bholder = b
    while b != 0:
        (a, b) = (b, a % b)
    print 'The greatest common divisor of',aholder,'and',bholder, 'is', a
    return a
def callGCD():
  i = 0

  while i < 5:
    rInt = random.randint(1,3000)
    rInt2 = random.randint(1,3000)
    i+=1
    gCommonDiv(rInt, rInt2)
 

  
