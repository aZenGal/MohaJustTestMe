#!/usr/bin/env python3

import conf as conf
from modules.bruteforce import read_nmap_result


def full_scan():
    print("===========================================================")
    print(conf.colored(conf.text2art("Test automatisé", "small"), "cyan"))
    print("===========================================================")

    full_host = input(conf.colored("\nSaisir l'URL cible (ex: opensource.com) : ", "green", attrs=["bold"]))
    full_host_clean = full_host.replace('https://', '').replace('http://', '')
    full_output = input(conf.colored(f"Saisir le dossier de sortie - [default: reports/All/{full_host_clean}/]: ", "green", attrs=["bold"],))

    conf.not_valid(full_scan, full_host)
    full_output = conf.dir_output(full_output, "reports/All", full_host_clean)

    conf.create_dir(full_output)

    full_ip = conf.socket.gethostbyname(full_host_clean)

    print("___________________________________________________________________________")

    conf.os.system(f"nmap -v -A {full_ip} -o {full_output}/nmap.txt")

    conf.os.system(f"dirb {full_host} /usr/share/wordlists/dirb/common.txt -o \"{full_output}/dirb.txt")

    conf.os.system(f"nikto -h {full_host_clean} -output {full_output}/nikto.txt")
    
    nmap_result = "{full_output}/nmap.txt"
    read_nmap_result(result_path=nmap_result, user=None)