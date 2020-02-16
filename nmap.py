import os
def nmap_results(options,ip):
    command= 'nmap '+ options + ' '+ ip
    process=os.popen(command)
    results= str(process.read())
    print("Nmap Done!")
    return results

#print(nmap_results('-F','216.58.203.206'))