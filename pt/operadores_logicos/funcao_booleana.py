# f(p, q) = ((não p) ou q) e ((não q) ou p)

def f(p, q):

    resultado = ((not p) or q) and ((not q) or p)

    return resultado

print('((não p) ou q) e ((não q) ou p)')
print('Tabela de Verdade')
p = True
q = True
f_pq = f(p, q)
print(p, q, '|', f_pq)
p = True
q = False
f_pq = f(p, q)
print(p, q, '|', f_pq)
p = False
q = True
f_pq = f(p, q)
print(p, q, '|', f_pq)
p = False
q = False
f_pq = f(p, q)
print(p, q, '|', f_pq)
