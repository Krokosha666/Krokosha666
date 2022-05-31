import os,math,time,click
from threading import Thread
clr=lambda:click.clear()
fill = '  '

msx = 60#116
msy = 60

mvSp = 0.1

points = [[4,4],[23,7],[7,24],[10,10]]

ang = 0
s=''

def cBack(r, g, b, text):
    return f'\033[48;2;{r};{g};{b}m{text}\033[0m'

def dist(ax,ay,bx,by):
 dx = ax-bx
 dy = ay-by
 return math.sqrt(dx*dx + dy*dy)

def Rend():
 global s
 s='##'*msx+'##\n\r##'
 stab = {}
 for i in range(1,msy):
  def doTheThing():
   ns = ""
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
    colsc = math.sin(pow(bs-1,0.2) *1.570796326795)
    col = 255 - round(colsc*255)
    ns += cBack(col,col,col,fill)
   stab[i] = ns
  Thread(target=doTheThing).start()
 while len(stab)+1!=msy:
  time.sleep(0.0001)
 for i in stab.values():
  s+=i
  s+="##\n\r##"
 s+="##"*msx# + "\n\r"

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

while True:
 Thread(target=Sim).start()
 Rend()
 clr()
 print(s)
 #time.sleep(0.016)