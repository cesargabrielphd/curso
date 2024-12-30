def log(logaritimando, base):
    """
    log o logaritimando pela base
    """
    if logaritimando <= 0 and base in [0, 1]:
        return "O logaritimando deve ser maior que 0 e a base deve ser maior que 0 e diferente de 1"        
    if logaritimando <= 0:
        return "O logaritimando deve ser maior que 0"
    if base in [0, 1]:
        return "A base deve ser maior que 0 e diferente de 1"
    else:
        indice = 0 
        while logaritimando >= base:
            logaritimando = logaritimando / base
            indice = indice + 1
            decomposto = indice
        return decomposto

print(log(100, 10))


# Referência: 
#  - copilot in VSCode
#  - google
#  - Eu mesmo
