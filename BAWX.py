#tested on windows
import os,math,time,click
clr=lambda:click.clear()
#view port size
msx = 25#60#110
msy = 25#60
#rotating speed
mvSp = 0.1
#memory
ang = 0
s=''
###script###
points = [[4,4],[3,7],[7,4],[1,1]]
#helper functions
def cBack(r, g, b, txt):
    return f'\033[48;2;{r};{g};{b}m{txt}\033[0m'
def dist(ax,ay,bx,by):
 dx = ax-bx
 dy = ay-by
 return math.sqrt(dx*dx + dy*dy)
#render frame
def Rend():
 global s
 s='##'*msx+'##\n\r##'
 for i in range(1,msy):
  for e in range(1,msx):
   poc = 0
   bs = 2
   for x,y in points:
    prind = poc-1
    if prind<0: prind = len(points)-1
    xb = points[prind][0]
    yb = points[prind][1]
    cs = (dist(e,i,x,y) + dist(e,i,xb,yb)) / dist(x,y,xb,yb)
    if cs<bs:
     bs = cs
    poc += 1
   col = 255 - round(math.sin(pow(bs-1,0.2) *1.5708)*255)
   s += cBack(col,col,col,"  ")
  s+="##\n\r##"
 s+="##"*msx
#rotation
hpi = math.pi/2
hmsx = msx/2
hmsy = msy/2
smallestSide = hmsx
if smallestSide>hmsy:
 smallestSide = hmsy
smallestSide = smallestSide*0.9
def Sim():
 global ang
 ind = 0
 ang += mvSp
 if ang>math.pi: ang -= math.pi
 for x,y in points:
  cang = ang + hpi*ind
  points[ind][0] = hmsx + math.sin(cang)*smallestSide
  points[ind][1] = hmsy + math.cos(cang)*smallestSide
  ind += 1
#main loop
while True:
 Sim()
 Rend()
 clr()
 print(s)
