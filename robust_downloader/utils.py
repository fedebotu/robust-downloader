import colorlog

from colorlog import ColoredFormatter


def get_pylogger(name=__name__):
    """Make Hydra-like color logging
    https://hydra.cc/docs/plugins/colorlog/
    """
    formatter = ColoredFormatter(
        "[%(cyan)s%(asctime)s%(reset)s][%(log_color)s%(levelname)s%(reset)s] - %(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
        secondary_log_colors={},
        style="%",
    )
    handler = colorlog.StreamHandler()
    handler.setFormatter(formatter)
    logger = colorlog.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel("DEBUG")

    return logger
