#!/bin/bash

# horario do cron job
cron_expr="0 1 * * *"

# Cria o arquivo de cronjob com base no parâmetro
comando="echo \"$cron_expr root python3 /app/scheduler.py >> /var/log/cron_job.log  2>&1\" > /etc/cron.d/cronjob"
echo "Criando cronjob: $comando"
echo "$comando" > /app/cronjob.sh
chmod +x /app/cronjob.sh


# Verifica se o servidor Xvfb está em execução no display 99
if ps aux | grep -q '[X]vfb :99'; then
    echo "Servidor Xvfb já está em execução no display 99. Encerrando..."
    pkill Xvfb
fi

# Inicializa o Xvfb
Xvfb :99 -screen 0 1920x1080x16 &
export DISPLAY=:99

# Mantém o contêiner em execução indefinidamente
tail -f /dev/null