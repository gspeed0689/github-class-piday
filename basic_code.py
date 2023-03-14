def power(x: [int | float], y: [int | float]):
    """Returns x to the y power. 

    Args:
        x (num): number-like object
        y (num): number-like object
    """

    v = x
    for x in range(1, y):
        v = v * x

    return(v)

def get_domains(s: str):
    pass