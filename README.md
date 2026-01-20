Um analisador de logs de segurança desenvolvido em Python para detectar possíveis ataques de força bruta 
em servidores Linux a partir de logs de autenticação.

## Funcionalidades
- Leitura e análise de logs de autenticação (`auth.log`)
- Detecção de tentativas excessivas de login por IP
- Geração automática de relatórios em CSV
- Visualização amigável dos resultados no terminal
- Configuração flexível via arquivo `.env`

## Tecnologias Utilizadas
- Python 3
- Rich (output formatado no terminal)
- python-dotenv
- CSV (biblioteca padrão)
- Git

## Futuros Upgrades

- Testes unitários

- Suporte a múltiplos tipos de ataques

- Integração com API ou dashboard