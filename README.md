# 🔎 Recon Total - Shodan + Nmap

> **Ferramenta completa de reconnaissance que combina a poderosa API do Shodan com a versatilidade do Nmap**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Shodan](https://img.shields.io/badge/Shodan-API-red.svg)](https://www.shodan.io/)
[![Nmap](https://img.shields.io/badge/Nmap-Compatible-orange.svg)](https://nmap.org/)

**Desenvolvido por:** Pentester Caio | CHDEVSEC

---

## 📋 Sobre o Projeto

O **Recon Total** é uma ferramenta de reconnaissance automatizada que combina duas das mais poderosas ferramentas de descoberta de informações: **Shodan** e **Nmap**. Esta solução oferece uma análise completa de alvos através de:

- 🌐 **Consulta Shodan**: Informações detalhadas sobre serviços expostos publicamente
- 🔍 **Scan Nmap**: Verificação local de portas e serviços ativos
- 📊 **Relatório Unificado**: Compilação automática dos resultados em arquivo texto

## ✨ Características

- **Interface simples**: Execução via linha de comando com um único parâmetro
- **Dupla verificação**: Combina dados do Shodan com scan local do Nmap
- **Saída organizada**: Resultados salvos automaticamente com timestamp
- **Tratamento de erros**: Gerenciamento robusto de timeouts e falhas de conexão
- **Informações detalhadas**: Organização, país, OS, portas e serviços identificados

## 🛠️ Pré-requisitos

### Dependências do Sistema
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install nmap python3 python3-pip

# CentOS/RHEL
sudo yum install nmap python3 python3-pip

# Arch Linux
sudo pacman -S nmap python python-pip
```

### Dependências Python
```bash
pip3 install requests
```

### API do Shodan
1. Crie uma conta em [shodan.io](https://www.shodan.io/)
2. Obtenha sua chave API gratuita
3. Configure no script substituindo `SEU_TOKEN_API`

## 🚀 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/recon-total.git

# Entre no diretório
cd recon-total

# Torne o script executável
chmod +x recon_total.py

# Configure sua API key do Shodan
nano recon_total.py
# Substitua "SEU_TOKEN_API" pela sua chave real
```

## 💻 Uso

### Sintaxe Básica
```bash
python3 recon_total.py <IP_ALVO>
```

### Exemplos de Uso
```bash
# Análise de um IP específico
python3 recon_total.py 8.8.8.8

# Análise de servidor web
python3 recon_total.py 192.168.1.100

# Análise com redirecionamento de saída
python3 recon_total.py 10.0.0.1 | tee analise.log
```

### Saída Esperada
```
============================================================
 🔎 RECON TOTAL - SHODAN + NMAP
 By Pentester Caio | CHDEVSEC
============================================================

[+] Consultando Shodan para o IP: 8.8.8.8...

Organização: Google LLC
País: United States
Sistema Operacional: N/A

Portas encontradas no Shodan:
 - Porta 53 | Serviço: Google Public DNS
 - Porta 443 | Serviço: HTTPS

[+] Rodando Nmap no IP: 8.8.8.8...

[Resultados do Nmap...]

[+] Resultado salvo em: recon_8_8_8_8_20240614_143022.txt
```

## 📁 Estrutura dos Arquivos de Saída

Os resultados são salvos automaticamente no formato:
```
recon_[IP_COM_UNDERSCORES]_[TIMESTAMP].txt
```

**Exemplo:** `recon_192_168_1_1_20240614_143022.txt`

### Conteúdo do Arquivo
```
============================================================
RECON TOTAL - SHODAN + NMAP
By Pentester Caio | CHDEVSEC
============================================================

IP Alvo: 192.168.1.1

[ SHODAN RESULTADO ]
[Dados do Shodan...]

[ NMAP RESULTADO ]
[Dados do Nmap...]
```

## ⚙️ Configurações Avançadas

### Timeout do Nmap
O script inclui timeout de 3 minutos para scans Nmap. Para ajustar:
```python
timeout=180  # Altere para o valor desejado em segundos
```

### Parâmetros do Nmap
Por padrão usa `-Pn -sV`. Para personalizar:
```python
["nmap", "-Pn", "-sV", ip]  # Modifique os parâmetros aqui
```

## 🔧 Solução de Problemas

### Erro de API Key
```
[!] Erro na API do Shodan: 401 - {"error": "Invalid API key"}
```
**Solução:** Verifique se sua chave API está correta no script.

### Timeout do Nmap
```
[!] Timeout: O Nmap demorou demais pra responder o IP X.X.X.X.
```
**Solução:** Aumente o valor do timeout ou verifique conectividade com o alvo.

### Nmap não encontrado
```
[!] Erro ao rodar Nmap: [Errno 2] No such file or directory: 'nmap'
```
**Solução:** Instale o Nmap através do gerenciador de pacotes do seu sistema.

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Changelog

### v1.0.0
- ✅ Integração inicial Shodan + Nmap
- ✅ Salvamento automático de resultados
- ✅ Tratamento de erros e timeouts
- ✅ Interface CLI intuitiva

## 📜 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## ⚠️ Disclaimer

**IMPORTANTE: Esta ferramenta é destinada exclusivamente para fins educacionais e testes de segurança autorizados.**

- ✅ **Use apenas** em sistemas que você possui ou tem permissão explícita para testar
- ✅ **Respeite** todas as leis locais e internacionais de cibersegurança
- ✅ **Obtenha autorização** por escrito antes de usar em redes corporativas
- ❌ **NÃO use** para atividades maliciosas, ilegais ou não autorizadas
- ❌ **NÃO assume responsabilidade** por uso inadequado desta ferramenta

### Responsabilidade Legal

O desenvolvedor não se responsabiliza por qualquer uso inadequado desta ferramenta. O usuário é totalmente responsável por garantir que o uso esteja em conformidade com todas as leis aplicáveis e políticas organizacionais.

### Ética em Segurança Cibernética

Esta ferramenta segue os princípios de **Ethical Hacking** e **Responsible Disclosure**:
- Sempre obtenha permissão antes de testar
- Reporte vulnerabilidades de forma responsável
- Respeite a privacidade e integridade dos dados
- Use conhecimentos de segurança para proteger, não para prejudicar

---

## 👨‍💻 Autor

**Pentester Caio | CHDEVSEC**

- 🔗 GitHub: github.com/CHDevSec

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!** ⭐
