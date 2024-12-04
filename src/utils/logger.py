import logging
from rich.logging import RichHandler
from rich.console import Console

def setup_logger(name: str, console):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Remove any existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    handler = RichHandler(console=console, show_time=True, show_level=True, show_path=False)
    formatter = logging.Formatter("%(message)s")

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger