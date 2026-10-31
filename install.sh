
#!/data/data/com.termux/files/usr/bin/bash

clear

echo "================================"
echo "       KEME INSTALLER"
echo "================================"

pkg update -y
pkg install python -y

pip install requests

echo ""
echo "[+] KEME installation completed!"
echo "[+] Starting KEME..."

python keme.py
