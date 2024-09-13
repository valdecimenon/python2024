# Função recursiva: é aquela que chama ela mesma
# Toda função recursiva deve ter uma condição de parada

def fatal(a):
    print(a)
    a += 1
    fatal(a)

# fatal(1)

# exemplo: fatorial(5)
# 5 * 4 * 3 * 1 = 120
def fatorial(n):
    if n == 0: 
        return 1   # sai da função 
    else:
        return n * fatorial(n - 1)
    
print(fatorial(10))
