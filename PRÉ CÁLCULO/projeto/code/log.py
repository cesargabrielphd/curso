def log(logaritimando, base):
    """
    log o logaritimando pela base
    """
    if logaritimando <= 0 or base in [0, 1]:
        return "Seu burro! O logaritimando deve ser maior que 0 e a base maior que 1."
    else:
        indice = 0 
        while logaritimando >= base:
            logaritimando = logaritimando / base
            indice = indice + 1
            decomposto = indice
        return decomposto

print(  log(32, 2) )

# Referência:
#  - copilot in VSCode
#  - google
#  - Eu mesmo
