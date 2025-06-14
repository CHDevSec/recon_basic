#!/usr/bin/env python3
# Recon Total - Shodan + Nmap
# By Pentester Caio | CHDEVSEC

import subprocess
import requests
import sys
import json
from datetime import datetime

# === CONFIGURAÇÃO ===
SHODAN_API_KEY = "SEU_TOKEN_API"  #Insira sua chave da API do Shodan aqui

# === FUNÇÕES ===

def banner():
    print("\n" + "=" * 60)
    print(" 🔎 RECON TOTAL - SHODAN + NMAP")
    print(" By Pentester Caio | CHDEVSEC")
    print("=" * 60 + "\n")

def assinatura_final():
    print("\n" + "=" * 60)
    print(" Script finalizado.")
    print(" Desenvolvido por: Pentester Caio | CHDEVSEC")
    print("=" * 60 + "\n")

def shodan_lookup(ip):
    print(f"[+] Consultando Shodan para o IP: {ip}...\n")
    url = f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"[!] Erro na API do Shodan: {response.status_code} - {response.text}")
            return f"Falha ao consultar Shodan. Código: {response.status_code}"

        data = response.json()

        result = []
        result.append(f"Organização: {data.get('org', 'N/A')}")
        result.append(f"País: {data.get('country_name', 'N/A')}")
        result.append(f"Sistema Operacional: {data.get('os', 'N/A')}\n")

        result.append("Portas encontradas no Shodan:")
        for item in data.get("data", []):
            port = item.get('port', 'N/A')
            service = item.get('product', 'Desconhecido')
            result.append(f" - Porta {port} | Serviço: {service}")
        
        output = "\n".join(result)
        print(output)
        return output

    except Exception as e:
        print(f"[!] Erro ao consultar Shodan: {e}")
        return f"Erro ao consultar Shodan: {e}"

def local_nmap_scan(ip):
    print(f"\n[+] Rodando Nmap no IP: {ip}...\n")
    try:
        nmap_result = subprocess.run(
            ["nmap", "-Pn", "-sV", ip],
            capture_output=True,
            text=True,
            timeout=180  # ← Aumentei para 3 minutos
        )
        print(nmap_result.stdout)
        return nmap_result.stdout
    except subprocess.TimeoutExpired:
        print(f"[!] Timeout: O Nmap demorou demais pra responder o IP {ip}.")
        return f"Timeout: O Nmap demorou mais de 3 minutos para o IP {ip}."
    except Exception as e:
        print(f"[!] Erro ao rodar Nmap: {e}")
        return f"Erro ao rodar Nmap: {e}"

def save_results(ip, shodan_data, nmap_data):
    filename = f"recon_{ip.replace('.', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    try:
        with open(filename, "w") as f:
            f.write("=" * 60 + "\n")
            f.write(f"RECON TOTAL - SHODAN + NMAP\n")
            f.write(f"By Pentester Caio | CHDEVSEC\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"IP Alvo: {ip}\n\n")
            f.write("[ SHODAN RESULTADO ]\n")
            f.write(shodan_data if shodan_data else "Falha ao consultar Shodan.\n")
            f.write("\n\n[ NMAP RESULTADO ]\n")
            f.write(nmap_data if nmap_data else "Falha ao executar Nmap.\n")
        
        print(f"\n[+] Resultado salvo em: {filename}")
    except Exception as e:
        print(f"[!] Erro ao salvar o resultado: {e}")

# === MAIN ===

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\n[!] Uso correto:")
        print(f"python3 {sys.argv[0]} <IP>\n")
        assinatura_final()
        sys.exit(1)

    ip = sys.argv[1]
    banner()

    shodan_data = shodan_lookup(ip)
    nmap_data = local_nmap_scan(ip)

    if shodan_data or nmap_data:
        save_results(ip, shodan_data, nmap_data)
    else:
        print("\n[!] Nenhum resultado válido para salvar.")

    assinatura_final()
