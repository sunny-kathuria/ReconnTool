from domain_name import *
from general import *
from get_ip_address import *
from nmap import *
from robots import *
from whois import *
import sys
ROOT_DIR = 'companies'
create_dir(ROOT_DIR)

def gather_info(name,url):
    robots_txt=get_robots(url)
    domain_name=get_domain_name(url)
    ip_address =get_ip_address(domain_name)
    nmap=nmap_results("-F", ip_address)
    whois=get_whois(domain_name)

    create_reports(name, url, domain_name, nmap,robots_txt, whois)
def create_reports(name, url, domain_name, nmap,robots_txt, whois):
    project_dir= ROOT_DIR+'/'+name
    create_dir(project_dir)
    write_file(project_dir + "/full_name.txt",url)
    write_file(project_dir + "/domain_name.txt", domain_name)
    write_file(project_dir + "/nmap.txt", nmap)
    write_file(project_dir + "/robots.txt", robots_txt)
    write_file(project_dir + "/whois.txt", whois)

    print("Scan Completed of "+domain_name)

company_name=sys.argv[1]
company_url=sys.argv[2]

if __name__== "__main__":
    company_url2="https://www."+company_url
    gather_info(company_name,company_url2)
    #gather_info('facebook','https://www.facebook.com')