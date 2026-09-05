# Build: 6d445f7937b22ea0f0e7ff08274a8acb

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
