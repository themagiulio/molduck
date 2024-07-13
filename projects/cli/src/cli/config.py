import json
import os
from typing import Any

import platformdirs


class Config:
    _config: dict[str, Any] = {}
    _config_file: str

    def __init__(self):
        self._load_config()

    def _load_config(self):
        config_path = platformdirs.user_config_path(appname="molduck")
        self.config_file = config_path / "config.json"

        try:
            with open(self.config_file, "r") as f_obj:
                content = f_obj.read()
                self._config = json.loads(content)
        except FileNotFoundError:
            if not os.path.exists(config_path):
                os.mkdir(config_path)

            with open(self.config_file, "w") as f_obj:
                f_obj.write("{}")

    def get_config(self, key: str):
        return self._config.get(key)

    def set_config(self, key: str, val: Any):
        self._config[key] = val

        with open(self.config_file, "w") as f_obj:
            f_obj.write(json.dumps(self._config))
