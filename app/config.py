import os
from pathlib import Path


class Config:
    KEY_FILE = Path('./key.txt')
    TASKS_PATH = './tasks.json'

    @property
    def SECRET_KEY(self):
        def sanitize(s: str):
            return s.strip()
        if (key := os.environ.get('SECRET_KEY')):
            return sanitize(key)
        if self.KEY_FILE.exists():
            with self.KEY_FILE.open() as f:
                return sanitize(f.read())
        return None
