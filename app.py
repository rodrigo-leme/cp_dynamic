def torre_de_hanoi(n, origem, destino, auxiliar):
    """
    Move n discos da haste 'origem' para a haste 'destino' usando a haste 'auxiliar'.
    
    Args:
        n: Número de discos a serem movidos
        origem: Haste de origem
        destino: Haste de destino
        auxiliar: Haste auxiliar
    """
    if n == 1:
        print(f"Mova o disco 1 da haste {origem} para a haste {destino}")
        return
    
    torre_de_hanoi(n-1, origem, auxiliar, destino)
    
    print(f"Mova o disco {n} da haste {origem} para a haste {destino}")
    
    torre_de_hanoi(n-1, auxiliar, destino, origem)

torre_de_hanoi(3, 'A', 'C', 'B')
