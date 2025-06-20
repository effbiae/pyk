from p import p;import sys
def ev(x):
 try:return int(x)
 except:pass
 if x[0]=='!':return range(ev(x[1]))
def accum(f,x):
 if not len(x):return()
 def accu_(f,x,y):
  r0=f(x,y[0])
  return (r0,)+(accu_(f,r0,y[1:])if 1<len(y)else())
 r=(x[0],)
 return r+(accu_(f,x[0],x[1:])if 1<len(x)else())
def scan(x,y,z):
 if x=='+'and y==0:return accum(lambda x,y:x+y,z)
ad={'\\':scan,'/':None,"'":None}
def adv(x,y):
 print(x,y)
 if not y:return x
 if len(y)==1:return ad[x[0]](x[1],0,ev(y[0]))
f=sys.stdin
while 1:
 x=f.readline()
 if not x:break
 x=p(x.strip())
 if type(x[0])==tuple:
  print(adv(x[0],x[1:]))
