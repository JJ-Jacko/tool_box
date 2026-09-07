"""Generate password"""

import random
import string

from tool_box.log import get_logger


def run(length: int):
    logger = get_logger("gen_pwd", file=False)

    if length < 6:
        logger.warning(f"length: {length} is too low, default to 8")
        length = 8

    chars = []
    chars_required = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    chars_all = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation
    ]
    chars.extend(chars_required)
    chars.extend(random.choices(chars_required, k=length - len(chars_all)))

    random.shuffle(chars)

    return ''.join(chars)
