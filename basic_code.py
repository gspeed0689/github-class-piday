def getDomains(domain_string):
    
    """This function should work, but wtf why not

    Args:
        domain_string (string): any url string
    """
    s = str(domain_string)
    L = s.split(".")
    print(L)
    return(L)

def power(x, y):
    """Go go power rangers, mighty morphin power rangers

    Args:
        x (num): base number
        y (num): power value
    """
    rv = x
    for i in range(y):
        rv = rv * x
    return(rv)

getDomains("https://geo-data-support.sites.uu.nl")