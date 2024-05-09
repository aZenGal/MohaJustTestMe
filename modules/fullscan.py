#!/usr/bin/env python3

import conf as conf
from modules.dirbscan import dirb_scan
from modules.bruteforce import read_nmap_result
from modules.audit import main_linpeas

def menu():
    conf.re_open()

def full_scan():
    print("===============================================================================")
    print(conf.colored(conf.text2art("Pentest automatique", "small"), "cyan"))
    print("===============================================================================")

    full_host = input(conf.colored("\nSaisir l'IP/URL cible (ex: www.opensource.com) : ", "green", attrs=["bold"]))
    full_host_clean = full_host.replace('https://', '').replace('http://', '').replace('/','')
    full_output = input(conf.colored(f"Saisir le dossier de sortie - [default: reports/All/{full_host_clean}/]: ", "green", attrs=["bold"],))

    conf.not_valid(full_scan, full_host)
    full_output = conf.dir_output(full_output, "reports/All", full_host_clean)

    conf.create_dir(full_output)

    full_ip = conf.socket.gethostbyname(full_host_clean)

    print("____________________________________________________________________________")
    print(conf.colored("Nmap port scan", "yellow", attrs=["bold"]))
    conf.os.system(f"nmap -v -A {full_ip} -o {full_output}/nmap.txt")

    print("____________________________________________________________________________")
    print(conf.colored("Dirb Enumeration scan", "yellow", attrs=["bold"]))
    #conf.os.system(f"dirb {full_host} /usr/share/wordlists/dirb/common.txt -o {full_output}/dirb.txt")
    dirb_scan(dir_host=full_host,dir_output=full_output)
    
    print("____________________________________________________________________________")
    print(conf.colored("Nikto Vulnerability scan", "yellow", attrs=["bold"]))
    conf.os.system(f"nikto -h {full_host_clean} -output {full_output}/nikto.txt")
    
    print("____________________________________________________________________________")
    print(conf.colored("Hydra Bruteforce", "yellow", attrs=["bold"]))
    nmap_result = f"{full_output}/nmap.txt"
    read_nmap_result(result_path=nmap_result, user=None, output=full_output)
    
    print("____________________________________________________________________________")
    print(conf.colored("LinPEAS Audit ", "yellow", attrs=["bold"]))
    hydra_result = f"{full_output}/hydra.txt"
    main_linpeas(hydra_output_file=hydra_result, host=full_host_clean)
    
    conf.call_def(menu, 0)
    
