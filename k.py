from p import p,P
def k2(x,y,z):
 if x=='+':return tuple(y+_ for _ in z)if tt(z)else y+z
 if x=='*':return y*z
 if x=='>':return y>z
 if x=='#':return tuple(z for _ in range(y))
 if x==',':
  if not tt(y):y=(y,)
  if not tt(z):z=(z,)
  return y+z
def k1(x,y):
 if x=='!':return tuple(range(y))
 if x=='|':return tuple(reversed(y))
 if x=='*':return y[0]
def fd(x,d):
 for _ in d:
  if x in _:return _[x]
def ev(x,d):
 if x is None:return x
 try:return int(x)
 except:pass
 if x[0][0]in P:return ap(x[0][0]+('',':')[len(x)==2],tuple(ev(_,d) for _ in x[1:]),d)
 if tt(x[0]):
  if len(x)==2:return adv(x[0],None,ev(x[1],d),d)
  else:return adv(x[0],x[1],ev(x[2],d),d)
 if ts(x)and x.isalpha():return fd(x,d)
 print(x);assert(0)
nn=lambda x:x is not None;ts=lambda x:type(x)is str;tt=lambda x:type(x)is tuple;md=lambda x:dict(zip("xyz"[:len(x)],x))
def ar(x):
 def lar(x):
  if tt(x)and x[0]!='{':return max(lar(_)for _ in x)
  if x in "xyz":return "xyz".find(x)+1
  return 1
 if ts(x)and x[0]in P:return (2,1)[':'in x]
 def car(x):return car(x[2])if tt(x)else ar(x)
 if tt(x):return lar(x[1:]) if x[0]=='{'else car(x)if x[0]=="'"else 1
 return 0
def ap(x,y,d):
 if ts(x):return (k2,k1)[':'in x](x[0],*y)
 if tt(x):
  if x[0]=='{':return ev((('[',)+x[1:]if len(x)>2 else x[1]),(md(y),d[-1]))
  if x[0]=="'":return ap(x[1],ap(x[2],y,d),d)
  if len(x)==3 and x[2]==():return ap(x[0],(ev(x[1],d),y[0]),d)
  if len(x)==2:assert(x[0]in"\\/'");return ad[x[0]](x[1],None,y,d)
def oid(f):
 if f=='+':return 0
def aca(f,y,z,d):
 t=z;r=(t,)
 for _ in range(ev(y,d)):t=ap(f,(t,),d);r+=(t,)
 return r
def acb(f,y,z,d):
 t=z;r=(t,)
 while ap(y,(t,),d):t=ap(f,(t,),d);r+=(t,)
 return r
def acc(f,y,z,d):
 r=();t=ev(y,d);t=t if nn(t)else oid(f)
 if t is None and len(z):t=z[0];r=(t,);z=z[1:]
 return r+tuple(t:=ap(f,(t,_),d) for _ in z)
def scan(x,y,z,d):return(aca if nn(y) and 0==ar(y)and 1==ar(x)else(acc,acb)[1==ar(x)])(x,y,z,d)
def over(x,y,z,d):x=scan(x,y,z,d);return x[-1]if x else x
ad={'\\':scan,'/':over,"'":None}
def adv(x,y,z,d):return ad[x[0]](x[1],y,z,d)
def t():
 def eq(x,y):z=ev(p(x),({},));(print(x,'was',z,'not',y),exit(1))if not z==eval(y)else None
 x=r'!2~(0,1) +/!3~3 1+\!3~(1,2,4) (0>)(1+)/0~0 (2>)(1+)\0~(0,1,2) {2+x+y}/!2~3 *|4(+\|:)\1,1~(5,8)'
 for _ in x.split():eq(*_.split('~'))
def O(x):print(x,end='');sys.stdout.flush()
if __name__=='__main__':
 t();import sys;f=sys.stdin;g={}
 while 1:
  O(' ')if f.isatty()else();
  x=f.readline()
  if not x:break
  x=p(x.strip())
  print(ev(x,(g,)))
