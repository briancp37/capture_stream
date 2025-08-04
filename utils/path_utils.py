import os


def ensure_dir(path: str):
    """
    Ensure that a directory exists, creating it if necessary.
    
    Args:
        path (str): The directory path to ensure exists
        
    Returns:
        None
    """
    if not os.path.exists(path):
        os.makedirs(path) 