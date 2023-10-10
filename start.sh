#!/bin/bash

# um tempo para garantir que o banco de dados e outros serviços estejam prontos (opcional)
sleep 15
# Executa o seu script principal em segundo plano
python __main__.py &

# Mantém o contêiner em execução indefinidamente
tail -f /dev/null
