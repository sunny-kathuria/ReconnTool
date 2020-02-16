from tld import get_fld

def get_domain_name(url):
    domain_name = get_fld(url)
    print("Domain Name Done!")
    return domain_name

#print(get_domain_name('https://www.facebook.com'))

#print(get_domain_name('https://www.google.com'))