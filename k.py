from p import p,P;import sys
def ev(x):
 try:return int(x)
 except:pass
 if x[0]=='!':return tuple(range(ev(x[1])))
 if type(x[0])==tuple:
  if len(x)==2:return adv(x[0],None,ev(x[1]))
  else:return adv(x[0],x[1],ev(x[2]))
 if type(x)==tuple:
  if x[0]in"\\/'":return ev(x[1])+x[0]
 if x in P:return x
 print(x);assert(0)
def accu_(f,y,z):
 if not len(z):return()
 r0=f(y,z[0]);return (r0,)+(accu_(f,r0,z[1:])if 1<len(z)else())
def accum1(f,y,z):return accu_(f,y,z)
def accum0(f,y,z):return()if not len(z)else(z[0],)+accu_(f,z[0],z[1:])
def scan(x,y,z):
 if x=='+':return(accum1,accum0)[y is None](lambda x,y:x+y,ev(y)if y else y,z)
def over(x,y,z):return scan(x,y,z)[-1]
ad={'\\':scan,'/':over,"'":None}
def adv(x,y,z):return ad[x[0]](x[1],y,z)
def t():
 def eq(x,y):z=ev(p(x));(print(x,'was',z,'not',y),exit(1))if not z==eval(y)else None
 x='!2:(0,1) +/!3:3 1+\!3:(1,2,4)'
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
