

class AdminRequiredError(Exception):
    """Raised when administrator/root privileges are required."""
    def __init__(self, *args):
        super().__init__(*args)