import logging


def show_logs_until_enter():
    """Shows log file contents until the user presses Enter."""
    log_file = "logger/app.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    handler = logging.FileHandler(log_file, mode="a")
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(handler)

    with open(log_file, "r") as file:
        log_content = file.read()

    print(log_content)

    input("Pressione Enter para continuar...")
