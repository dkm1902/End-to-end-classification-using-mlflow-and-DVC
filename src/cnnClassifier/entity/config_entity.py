from dataclasses import dataclass
from pathlib import Path

#same variables which were definded in config/config.yaml
#Entity = return type of functions
@dataclass(frozen= True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path 
    unzip_dir: Path