# Usa uma imagem oficial do Python
FROM python:3.12-slim

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia arquivos de dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código para dentro do container
COPY . .

# Comando para rodar o app
CMD ["python", "main.py"]
