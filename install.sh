#!/usr/bin/env bash

DEPENDENCIES="nmap nikto git python3-pip"

# Vérifier que le système d'exploitation est Kali Linux
if [ "$(grep 'Kali' /etc/issue)" ]; then
    sudo apt-get update
    sudo apt-get install $DEPENDENCIES -y
else
    echo "Ce script est uniquement destiné à être exécuté sur Kali Linux"
    exit 1
fi

pip3 install --user -r conf/requirements.txt
sudo ln -s "$(pwd)"/MohaJustTestMe.py /usr/local/bin/MohaJustTestMe
git clone --depth 1 https://github.com/maurosoria/dirsearch.git ~/.local/share/dirsearch
