# `utils.py`

```python
import yaml
import os
import logging

def validate_config(config):
    """
    Validates if the necessary keys are present in the configuration.
    
    Args:
        config (dict): Configuration dictionary.

    Raises:
        RuntimeError: If any required keys are missing.
    """
    required_keys = ["schema", "transformations", "missing_threshold"]
    for key in required_keys:
        if key not in config:
            raise RuntimeError(f"Missing required config key: {key}")

def load_config(path="pipeline_config.yml"):
    """
    Load YAML configuration for the data cleaning pipeline.
    
    Args:
        path (str): Path to the YAML config file.
    
    Returns:
        dict: Parsed configuration dictionary.
    
    Raises:
        RuntimeError: If the file cannot be loaded or parsed.
    """
    abs_path = os.path.abspath(path)
    try:
        with open(abs_path, "r") as f:
            config = yaml.safe_load(f)
            validate_config(config)
            logging.info(f"Successfully loaded config from {abs_path}")
            return config
    except FileNotFoundError:
        logging.error(f"Config file not found: {abs_path}")
        raise RuntimeError(f"Config file not found: {abs_path}")
    except yaml.YAMLError as e:
        logging.error(f"Error parsing YAML file {abs_path}: {e}")
        raise RuntimeError(f"Error parsing YAML file {abs_path}: {e}")
    except Exception as e:
        logging.error(f"Failed to load config from {abs_path}: {e}")
        raise RuntimeError(f"Failed to load config from {abs_path}: {e}")
```