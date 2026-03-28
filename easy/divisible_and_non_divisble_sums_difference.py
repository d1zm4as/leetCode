n = 10
m = 3

soma_n = 0

soma_m = 0

for x in range(n+1):
    if x%m==0:
        soma_m+=x
    else:
        soma_n+=x
    