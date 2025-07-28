from datetime import timedelta, date, datetime
import time

def add_date():
    """
    Adds 30 days to the current date and returns both
    the resulting date as epoch and formatted string.

    Returns:
        tuple: (epoch_timestamp, 'YYYY-MM-DD' formatted string)
    """
    today = date.today()
    ex_date = today + timedelta(days=30)
    pattern = '%Y-%m-%d'
    epcho = int(time.mktime(time.strptime(str(ex_date), pattern)))
    normal_date = datetime.fromtimestamp(epcho).strftime('%Y-%m-%d')
    return epcho, normal_date


def check_expi(saved_date):
    """
    Checks if the saved date (in epoch) is still valid
    compared to today's date.

    Args:
        saved_date (int): Epoch timestamp of saved/expiry date.

    Returns:
        bool: True if not expired, False otherwise.
    """
    today = date.today()
    pattern = '%Y-%m-%d'
    epcho = int(time.mktime(time.strptime(str(today), pattern)))
    remaining = saved_date - epcho
    print(f"Remaining seconds: {remaining}")
    return remaining > 0
