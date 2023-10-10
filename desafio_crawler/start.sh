#!/bin/bash
# Inicializa o seu script principal em segundo plano
python __main__.py &

# Mantém o contêiner em execução indefinidamente
tail -f /dev/null
