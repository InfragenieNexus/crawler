import datetime


def create_cronjob(data_hora):
    try:
        data_hora_obj = datetime.datetime.strptime(data_hora, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Formato de data e hora inválido. Use o formato 'YYYY-MM-DD HH:MM'.")
        return

    cron_expr = f"{data_hora_obj.minute} {data_hora_obj.hour} {data_hora_obj.day} {data_hora_obj.month} *"
    comando = f"{cron_expr} root /usr/local/bin/python3 /app/job.py >> /var/log/cron_job.log 2>&1"

    with open("/etc/cron.d/cronjob", "w") as file:
        file.write(comando)

    print(f"Cron job agendado para executar job.py em {data_hora}.")


if __name__ == "__main__":
    data_hora = input(
        "Digite a data e hora para agendar a consulta (no formato 'YYYY-MM-DD HH:MM'): "
    )
    create_cronjob(data_hora)
