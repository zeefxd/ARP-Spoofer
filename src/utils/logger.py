import logging
from rich.logging import RichHandler
from rich.console import Console

def setup_logger(name: str, console: Console) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = RichHandler(console=console, show_time=True, show_level=True, show_path=False)
    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)

    logger.handlers = []  # Clear existing handlers
    logger.addHandler(handler)

    return logger