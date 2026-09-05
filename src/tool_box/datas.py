from dataclasses import dataclass
from pathlib import Path


class File:
    hash: str
    path: Path
    times: int
    
    def __init__(
            self,
            hash: str,
            path: Path
    ):
        if not path.is_file():
            raise ValueError
        
        self.hash = hash
        self.path = path
        self.times = 1
        
    def __eq__(self, other):
        if not isinstance(other, File):
            return NotImplemented
        
        return other.hash == self.hash
    
    def increase_times(self):
        self.times += 1


@dataclass
class Command:
    func: function
    help: str
    with_input: bool
    with_output: bool
    with_extension: bool

    with_fps: bool = False
