#!/usr/bin/env python3

import conf as conf

def Dirb_scan():
    print("===================================================================")
    print(conf.colored(conf.text2art("Dirb Scan", "small"), "cyan"))
    print("===================================================================")

    dir_host = input(conf.colored("\nEntrez une URL (https://www.ec-council.org): ", "green", attrs=["bold"]))
    dir_output = input(conf.colored(f"Saisir le dossier de sortie - [defaut: reports/Dirb/{dir_host}/]: ", "green", attrs=["bold"],))

    conf.not_valid(Dirb_scan, dir_host)
    dir_output = conf.dir_output(dir_output, "reports/Dirb", dir_host)
    conf.create_dir(dir_output)

    conf.os.system(f"dirb {dir_host} /usr/share/wordlists/dirb/common.txt -o {dir_output}/Dirb.txt")

    print("______________________________________________________________________")
