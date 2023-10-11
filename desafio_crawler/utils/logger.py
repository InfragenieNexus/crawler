import logging


# Configuração do logger
def setup_logger() -> None:
    """Função para configurar o logger"""
    logging.basicConfig(
        filename="logger/app.log",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] - %(message)s",
    )
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())
