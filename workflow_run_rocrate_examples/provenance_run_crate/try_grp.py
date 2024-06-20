try:
    import grp
except ImportError:
    # Handle the absence of the grp module on Windows
    grp = None

