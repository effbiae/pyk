P=":+-*%!&|<>=~,^#_$?@.";m=["av;","['/\\",P,";)]}\n "];c=dict([(chr(x),' ')for x in range(128)])
def f(x,s):
 for a in s:c[a]=x
for i in range(3):f(m[0][i],m[i+1])
def cs(i):
 if(i<len(s)):return c[s[i][0]]
 return';'
def n():
 global i
 if len(s)!=i:i+=1;return s[i-1]
 return' ';
def q():return';'==cs(i)
def E(x):
 x=(x,)
 while n()in";[({":
  x=x+(e(t()),)
 return x
def t():
 if q():return()
 x=n()if not s[i][0]in'([{'else x[1]if 3>len(x:=E(s[i]))and x[0]!='{'else x
 while'a'==cs(i):x=E(x)if'['==s[i]else(n(),x)
 return x
def verb(x):#primitive or derived verb?
 if type(x)==str and len(x)>0:return c[x[0]]=='v'
 return len(x)>0 and type(x[0])==str and c[x[0]]=='a'
def train(x):#is train? if a verb or projection or composition
 if verb(x):return 1
 return type(x)==tuple and len(x)==3 and(x[0]=="'"or x[2]==())
def o3(x,y,z):
 if train(z):return("'",(x,y,()),z)
 return (x,y,z)
def monad(x):
 if type(x)==str and c[x[0]]=='v':return x+':'
 return x
def o2(x,y):
 if train(y):return("'",monad(x),y)
 return (x,y)
def v():return';'<cs(i-1)
def e(x):
 if q():return x
 v_=v();f=t();return o3(f,x,e(t()))if v()>v_ else o2(x,e(f))
def lex(x):
 r=[];i=0
 while i<len(x):
  if i<len(x)-1 and c[x[i]]in'av'and x[i+1]==':':r.append(x[i:2+i]);i+=1
  else:r.append(x[i])
  i+=1
 return r
def p(x):global s,i;s=lex('['+x);i=0;return t()
def test():
    import sys
    if 0: #generate test cases
        print('[')
        for x in ["x;y","(x;y)","f[x;y]","x+y","x+*y","1+3*x","(+x)%y","(+/x)%#x","x+m[*i]/y","1+2-","3*:/2","+-","3+-","5(+\\|:)\\x","f::x,0","{x}"]:
            print("        [%12s,%s ],"%(x.__repr__(),parse(x)))
        print(']')
    for x,y in [
        [          '',() ],
        [         '1','1'],
        [       'x;y',('[', 'x', 'y') ],
        [     '(x;y)',('(', 'x', 'y') ],
        [    'f[x;y]',('f', 'x', 'y') ],
        [       'x+y',('+', 'x', 'y') ],
        [      'x+*y',('+', 'x', ('*', 'y')) ],
        [     '1+3*x',('+', '1', ('*', '3', 'x')) ],
        [    '(+x)%y',('%', ('+', 'x'), 'y') ],
        [  '(+/x)%#x',('%', (('/', '+'), 'x'), ('#', 'x')) ],
        [ 'x+m[*i]/y',('+', 'x', (('/', ('m', ('*', 'i'))), 'y')) ],
        [      '1+2-',("'",('+', '1', ()),('-', '2', ())) ],
        [     '3*:/2',(('/', '*:'), '3', '2') ],
        [        '+-',("'", '+:', '-') ],
        [       '3+-',("'", ('+', '3', ()),'-') ],
        ['5(+\\|:)\\x',(('\\', ("'", ('\\', '+'), '|:')), '5', 'x') ],
        [    'f::x,0',('::', 'f', (',', 'x', '0')) ],
        [       '{x}',('{', 'x') ],
        ]:
        if (r:=p(x))!=y:print('!',repr(x),repr(r),'!=',y);sys.exit(1)
if __name__=='__main__':
 test()
