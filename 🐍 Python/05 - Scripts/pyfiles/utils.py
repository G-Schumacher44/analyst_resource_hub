from sklearn.model_selection import train_test_split

def train_test_split_simple(X, y, test_size=0.2, random_state=42):
    """
    Splits the data into training and testing sets.

    Parameters:
    - X: Features
    - y: Target
    - test_size: Proportion of the dataset to include in the test split
    - random_state: Seed used by the random number generator

    Returns:
    - X_train, X_test, y_train, y_test
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

# --- Logger Setup ---


import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        fh = logging.FileHandler(log_file)
        fh.setLevel(level)
        formatter = logging.Formatter('%(asctime)s — %(levelname)s — %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        # 👇 REMOVE or comment out this to suppress notebook output
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.WARNING)
        # ch.setFormatter(formatter)
        # logger.addHandler(ch)

    logger.propagate = False
    return logger


def log_summary_report(df, logger, phase_name=""):
    """
    Logs a summary phase marker for checkpointing.

    Args:
        df (pd.DataFrame): The DataFrame to summarize.
        logger (Logger): Logger instance.
        phase_name (str, optional): Name of the processing phase. Defaults to "".
    """
    import inspect
    if not phase_name:
        try:
            caller = inspect.stack()[1].function
            phase_name = f"Phase: {caller}"
        except Exception:
            phase_name = "Unnamed Phase"
    logger.info(f"\n🧠 Summary Checkpoint Reached: {phase_name} 🧠")
    logger.info("------------------------------------------------------")