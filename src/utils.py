import numpy as np
import pandas as pd
import yaml
from sklearn.preprocessing import MinMaxScaler
from typing import Dict

def generate_synthetic_services(num_services: int = 2000, output_file: str = 'data/synthetic_services.csv') -> pd.DataFrame:
    """
    Generate synthetic services with realistic QoS.
    
    Distributions:
    - cost: uniform [1, 100]
    - response_time: normal mean=50, std=20 (clipped >0)
    - availability: uniform [0.9, 0.99]
    - base_energy_kwh: uniform [0.1, 1.0]
    
    :param num_services: Number of services (1000-5000).
    :param output_file: CSV path to save.
    :return: DataFrame of services.
    """
    ids = np.arange(1, num_services + 1)
    costs = np.random.uniform(1, 100, num_services)
    response_times = np.clip(np.random.normal(50, 20, num_services), 0.1, np.inf)
    availabilities = np.random.uniform(0.9, 0.99, num_services)
    base_energies = np.random.uniform(0.1, 1.0, num_services)
    
    df = pd.DataFrame({
        'id': ids,
        'cost': costs,
        'response_time': response_times,
        'availability': availabilities,
        'base_energy_kwh': base_energies
    })
    df.to_csv(output_file, index=False)
    return df

def load_config(config_path: str = 'src/config.yaml') -> Dict:
    """Load YAML config."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def normalize_qos(values: np.ndarray) -> np.ndarray:
    """Min-max normalization."""
    scaler = MinMaxScaler()
    return scaler.fit_transform(values.reshape(-1, 1)).flatten()
