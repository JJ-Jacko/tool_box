from pathlib import Path


__all__ = [
    # Path
    "INPUT_DIR",
    "OUTPUT_DIR",
    
    # Extensions
    "EXTENSION"
]


# Path
INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

# Extensions
class EXTENSION:
    COMPRESSED_FILE = frozenset(["tar", "gz", "xz", "7z", "zip", "rar"])
    IMAGE = frozenset(["jpg", "png"])
    MEDIA = frozenset(["mp4", "mov", "flv", "avi"])
    
# Initialization
INPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
