mport itertools
ones = ['', 'One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
teens = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen',
         'Seventeen','Eighteen','Nineteen']
tens = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
units = ones + teens + list(map(lambda n: n[0]+("-"+n[1] if n[1] else ''), 
                                itertools.product(tens,ones)))
thousands = ['','Thousand','Million','Billion','Trillion','Quadrillion']
def n2words(N, z=0, q=[]):
    if N==0: return ' '.join(q[::-1])
    N,r = divmod(N, 1000)
    if r>0:
        h,u = divmod(r, 100)
        words = (ones[h]+' Hundred ' if h>0 else '') + units[u]+" "+thousands[z]
        q.append(words)
    return n2words(N, z+1, q)
N = int(input("Enter a number to spell out? "))
print ('Zero' if N==0 else n2words(N))
