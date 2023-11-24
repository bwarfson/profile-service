import getpass


def get_username() -> str:
    try:
        return getpass.getuser().replace('.', '-')
    except Exception:
        return 'github'