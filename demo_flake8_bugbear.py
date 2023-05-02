import socket


def printer_is_available(printer_host: str, printer_port: int) -> bool:
    """Check if printer is available."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            sock.connect((printer_host, printer_port))
            return True
    except socket.error:
        return False


def batch_check_printer(printers) -> list:
    """Check each printer in a list for availability."""
    return [printer_is_available(*printer) for printer in printers]


class DummyFloat:
    # shouldn't be calling __float__ at all when doing comparisons
    def __float__(self):
        raise AssertionError("__float__ should not be invoked for comparisons")

    # same goes for subtraction
    def __sub__(self, other):
        raise AssertionError("__sub__ should not be invoked for comparisons")
