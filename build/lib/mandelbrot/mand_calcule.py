def is_in_Mandelbrot(c, max_iter=50)->bool:
    """Verifier un point apres max_iter fois iteration est dans la suite Mandelbrot

    Args:
        c (complex,optional complex_array): le candidat
        max_iter (int): nombre d'iteration.

    Returns:
        bool: si dans la suite->True; sinon False
    """
    z = 0
    for _ in range(max_iter):
        z = z**2 + c
    return abs(z) <= 2

def is_in_Julia(z,c, max_iter=50)->bool:
    """Verifier un point apres max_iter fois iteration est dans la suite Mandelbrot

    Args:
        c (complex,optional complex_array): le candidat
        max_iter (int): nombre d'iteration.

    Returns:
        bool: si dans la suite->True; sinon False
    """
    for _ in range(max_iter):
        z = z**2 + c
    return abs(z) <= 2
