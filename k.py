from p import p,P;import sys
def k2(x,y,z):
 if x=='+':return y+z
 if x=='>':return y>z
def k1(x,y):
 if x=='!':return tuple(range(y))
def ev(x):
 if x is None:return x
 try:return int(x)
 except:pass
 if x[0][0]in P:return ap(x[0][0]+('',':')[len(x)==2],(ev(_) for _ in x[1:]))
 if type(x[0])==tuple:
  if len(x)==2:return adv(x[0],None,ev(x[1]))
  else:return adv(x[0],x[1],ev(x[2]))
 if type(x)==tuple:
  if x[0]in"\\/'":return ev(x[1])+x[0]
 if x in P:return x
 print(x);assert(0)
nn=lambda x:x is not None
def ar(x):
 if type(x)==str:return (2,1)[':'in x]
 if type(x)==tuple:return 1
def ap(x,y):
 if type(x)==str:return (k2,k1)[':'in x](x[0],*y)
 if type(x)==tuple:
  if len(x)==3 and x[2]==():return ap(x[0],(ev(x[1]),y[0]))
def oid(f):
 if f=='+':return 0
def acb(f,y,z):
 t=z;r=(t,)
 while ap(y,(t,)):
  t=ap(f,(t,));r+=(t,)
 return r
def acc(f,y,z):r=();t=ev(y);t=t if nn(t)else oid(f);[(t:=ap(f,(t,_)),r:=r+(t,))for _ in z];return r
def scan(x,y,z):return (acc,acb)[1==ar(x)](x,y,z)
def over(x,y,z):x=scan(x,y,z);return x[-1]if x else x
ad={'\\':scan,'/':over,"'":None}
def adv(x,y,z):return ad[x[0]](x[1],y,z)
def t():
 def eq(x,y):z=ev(p(x));(print(x,'was',z,'not',y),exit(1))if not z==eval(y)else None
 x=r'!2:(0,1) +/!3:3 1+\!3:(1,2,4) (0>)(1+)\0:(0,) (2>)(1+)\0:(0,1,2)'
 for _ in x.split():eq(*_.split(':'))
def O(x):print(x,end='');sys.stdout.flush()
if __name__=='__main__':
 t();f=sys.stdin
 while 1:
  O(' ')if f.isatty()else();
  x=f.readline()
  if not x:break
  x=p(x.strip())
  print(ev(x))
