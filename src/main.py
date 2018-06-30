import logging
import os

import settings
from mighty_nog import MightyNog
from helpers import descriptions

bot = MightyNog(
    command_prefix=os.getenv('NOG_CMD_PREFIX', '!'),
    description=descriptions.main,
    pm_help=True
)


def setup_logging():
    """Me being playful with logging"""
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter_console = logging.Formatter(
        '\033[92m{asctime} \033[0m| '
        '\033[94m{name:>18}.py \033[0m-> '
        '\033[93m{levelname:>8}: \033[0m'
        '{message}',
        "%d.%m.%Y %H:%M:%S",
        style='{'
    )
    console.setFormatter(formatter_console)
    log.addHandler(console)


if __name__ == '__main__':
    setup_logging()
    for extension in settings.extensions:
        bot.load_extension(extension)
    bot.run(os.environ.get('NOG_BOT_TOKEN'))
