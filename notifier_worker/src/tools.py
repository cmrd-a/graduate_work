"""tools for notification worker."""
import random
import string


def generate_promo(len_promo: int) -> str:
    """
    This function generate unique promo code from user.
    :param len_promo: number of characters in the promo code.
    :return: unique format string.
    """
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=len_promo))
