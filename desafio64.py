def blackjack(x,y,z):
    soma = x + y + z

    if soma <= 21:
        return soma
    
    if soma > 21 and (x == 11 or y == 11 or z == 11):
        soma -= 10
    if soma <= 21:
        return soma
    else:
        return -1

print(blackjack(6,1,10))