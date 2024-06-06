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
    rv = x ** y
    return(rv)

getDomains("https://geo-data-support.sites.uu.nl")