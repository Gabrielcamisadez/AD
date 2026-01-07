#!/bin/bash

for ip in $(cat computers.txt); do
	if ping -c 1 -W 1 $ip > /dev/null; then
		echo "[+] host $ip ativo. ...."
		wait
		nmap -F $ip | grep "/tcp"
	else
		echo "[-] host $ip nada. skip"
	fi
done
