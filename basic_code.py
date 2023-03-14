def get_domains(domain_string):
    s = str(domain_string)
    L = s.split(".")
    print(L)
    return(L)

get_domains("geo-data-support.sites.uu.nl")