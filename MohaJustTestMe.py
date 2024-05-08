#!/usr/bin/env python3

import conf

def main():
    while conf.ans:
        conf.os.system("clear")
        print("===================================================================")
        print(conf.colored(conf.text2art("MohaJustTestMe", "larry3d"), "cyan"))
        print(conf.colored("[>]", "red", attrs=["bold"]) + conf.colored("Créé par : Mohamed-Ali TRABELSI\n", "magenta", attrs=["bold"]))
        # print(conf.colored("[>]", "red", attrs=["bold"]) + conf.colored(f"Version : {conf.version}\n", "magenta", attrs=["bold"]))
        # conf.ver_check()
        print("===================================================================")
        
        print(conf.colored("\n1. Nmap Scan", "yellow", attrs=["bold"]))
        print(conf.colored("2. Dirb Scan", "yellow", attrs=["bold"]))
        print(conf.colored("3. Nikto Scan", "yellow", attrs=["bold"]))
        print(conf.colored("4. Hydra Bruteforce", "yellow", attrs=["bold"]))
        print(conf.colored("A. Test automatise", "yellow", attrs=["bold"]))
        print(conf.colored("E. Quitter\n", "yellow", attrs=["bold"]))
        print("===================================================================")

        conf.ans = input(conf.colored("\nQue souhaitez vous faire ? Entrez votre selection: ", "green")).upper()

        if conf.ans == "1":
            conf.call_def(conf.nmap_scan)
        elif conf.ans == "2":
            conf.call_def(conf.Dirb_scan)
        elif conf.ans == "3":
            conf.call_def(conf.nikto_scan)
        elif conf.ans == "4":
            conf.call_def(conf.menu_bruteforce)
        elif conf.ans == "A":
            conf.call_def(conf.full_scan)
        elif conf.ans == "E":
            conf.call_def(conf.exit)
        else:
            conf.not_valid(main, conf.ans, 0)


try:
    main()
except KeyboardInterrupt:
    print("\n \n Clavier interrompu. ")
    conf.sys.exit()
