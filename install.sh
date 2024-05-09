#!/usr/bin/env bash

DEPENDENCIES="nmap nikto dirsearch git python3-pip"

# Vérifier que le système d'exploitation est Kali Linux
if [ "$(grep 'Kali' /etc/issue)" ]; then
    sudo apt-get update
    sudo apt-get install $DEPENDENCIES -y
    
    # Décompression de la wordlist rockyou
    if [ -f /usr/share/wordlists/rockyou.txt.gz ]; then
        sudo gunzip -k /usr/share/wordlists/rockyou.txt.gz
        echo "rockyou.txt a été décompressé avec succès."
    else
        echo "Le fichier rockyou.txt.gz n'a pas été trouvé."
    fi
else
    echo "Ce script est uniquement destiné à être exécuté sur Kali Linux"
    exit 1
fi

pip3 install --user -r conf/requirements.txt
sudo ln -s "$(pwd)"/MohaJustTestMe.py /usr/local/bin/MohaJustTestMe
git clone --depth 1 https://github.com/maurosoria/dirsearch.git ~/.local/share/dirsearch
curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh -o ~/.local/share/linpeas.sh

