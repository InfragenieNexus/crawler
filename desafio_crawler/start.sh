#!/bin/bash

# Inicialize o Xvfb
Xvfb :99 -screen 0 1920x1080x16 &
export DISPLAY=:99

# Um tempo para garantir que o Xvfb esteja pronto (opcional)
sleep 5

# Um tempo adicional, se necessário, para garantir que o banco de dados e outros serviços estejam prontos (opcional)
sleep 10

# Executa o seu script principal em segundo plano
python __main__.py &

# Mantém o contêiner em execução indefinidamente
tail -f /dev/null
