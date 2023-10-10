# Use a imagem Python 3.8 como base
FROM python:3.8 AS base

# Instale o Chromium
RUN apt-get update && apt-get install -y chromium

# Instale o ChromeDriver
RUN apt-get install -y chromium-driver

# Instale o Xvfb
RUN apt-get update && apt-get install -y xvfb

# Defina a variável de ambiente PATH para incluir o diretório do Chromium
ENV PATH="/usr/lib/chromium-browser:${PATH}"

ENV DISPLAY=:99


# Define o diretório de trabalho como /app
WORKDIR /app

# Copie os arquivos do seu aplicativo para o contêiner
COPY . /app

# Instale as dependências Python a partir do requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o arquivo start.sh para o contêiner
COPY start.sh /app/start.sh

# Dê permissões de execução para o arquivo start.sh
RUN chmod +x /app/start.sh

# Defina o comando principal do seu aplicativo (substitua CMD com o comando apropriado)
CMD ["/app/start.sh"]
