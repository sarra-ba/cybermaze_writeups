from Crypto.Util.number import *
p=getPrime(512)
q=getPrime(512)
flag="CM{????????????????????}"
m=bytes_to_long(flag.encode())
n=p*q
phi=(p-1)*(q-1)
e=?
c=pow(m,e,n)
with open("out.txt","w") as f:
    f.write(f' n={n}\n')
    f.write(f' c={c}\n')
    f.write(f' e={e}\n')
    