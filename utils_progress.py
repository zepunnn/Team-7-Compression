from tqdm import tqdm


def progress(iterable, desc="", unit="item", enable=True):
    """
    Unified progress bar wrapper for all compression processes.

    Parameters:
    - iterable : iterable object (range, list, zip, etc.)
    - desc     : description shown on the progress bar
    - unit     : unit label (char, block, frame, etc.)
    - enable   : toggle progress bar on/off

    Returns:
    - tqdm iterable if enabled, otherwise original iterable
    """
    if enable:
        return tqdm(iterable, desc=desc, unit=unit)
    return iterable