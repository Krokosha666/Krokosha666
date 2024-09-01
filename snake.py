import os,math,time,random
from threading import Thread
from getch import getch
clear=lambda:os.system('clear')
char = '\033[41m' + '  ' + '\033[0m'
fd = '\033[43m' + '  ' + '\033[0m'
fill = '  '

mapsizex = 27
mapsizey = 33
maxfood = 30

s=''
out=''
running = True

body = [[math.floor(mapsizex/2),math.floor(mapsizey/2)],[math.floor(mapsizex/2),math.floor(mapsizey/2)+1]]
food = []
godir = random.randint(1,4)
hs=0

def Rend():
 global s
 s='##'*mapsizex+'##\n\r##'
 for i in range(1,mapsizey):
  for e in range(1,mapsizex):
   dy=True
   for a,b in body:
    if b==i and e==a:
     dy=False
     s=s+char
     break
   if dy:
    for a,b in food:
     if b==i and e==a:
      dy=False
      s=s+fd
      break
    if dy:s=s+fill
  s+="##\n\r##"
 csc=len(body)-2
 global hs,out
 if hs<csc: hs=csc
 s+='##'*mapsizex+'\n\r score: '+str(csc)+' highest: '+str(hs)+'  \033[42m'+out+'\033[0m'
 out=''

def Sim():
 h=body[0]
 tl=len(body)-1
 dm=0
 for a,b in food:
  if a==h[0] and b==h[1]:
   food[dm]=None
   food.remove(None)
   body.append([body[tl][0],body[tl][1]])
   break
  dm+=1
 for a,b in body:
  tl-=1
  if tl<0:
   if godir==3:h[0]-=1
   elif godir==4:h[0]+=1
   elif godir==1:h[1]-=1
   elif godir==2:h[1]+=1
   if h[0]<1:
    h[0]=mapsizex-1
   elif h[0]>=mapsizex:
    h[0]=0
   elif h[1]<1:
    h[1]=mapsizey-1
   elif h[1]>=mapsizey:
    h[1]=0
   tl=-1
   for e,n in body:
    tl+=1
    if tl>1 and e==h[0] and n==h[1]:
     while len(body)>tl:
      body[tl]=None
      body.remove(None)
     break
   break
  else:
   tn=tl+1
   body[tn][0]=body[tl][0]
   body[tn][1]=body[tl][1]
 if len(food)<maxfood:
  randx = random.randint(1,mapsizex-1)
  randy = random.randint(1,mapsizey-1)
  DH=True
  for a,b in food:
   if a==randx and b==randy:
    DH=False
  if DH:
   for a,b in body:
    if a==randx and b==randy:
     DH=False
   if DH:
    food.append([randx,randy])
 
wd=True
def GLS():
 while running:
  Sim()
  Rend()
  clear()
  print(s)
  def Wait():
   wed=0
   global wd
   while wed<0.29 and wd:
    time.sleep(0.01)
    wed+=0.011
   if wd and wed>=0.28: wd=False
  global wd
  wd=True
  ck=godir
  thr=Thread(target=Wait)
  thr.start()
  while ck==godir and wd:
   time.sleep(0.005)
  wd=False

Thread(target=GLS).start()

while running:
 while not wd:
   time.sleep(0.03)
 k = getch()
 if k=='w' or k=='2':
  if not godir==2:godir = 1
 elif k=='s' or k=='8':
  if not godir==1:godir = 2
 elif k=='a' or k=='4':
  if not godir==4:godir = 3
 elif k=='d' or k=='6':
  if not godir==3:godir = 4
 elif k=='p': running=False





































































































































































































