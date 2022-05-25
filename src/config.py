from __future__ import annotations

import os
import json
from typing import TYPE_CHECKING


if TYPE_CHECKING:
  from typing import TypedDict

  class ConfigSettings(TypedDict):
    config_option_1: str
    boilerplate_env_1: str


class Configuration:
  def __init__(self, config_path: str):
    self.__config_path = os.path.normpath(os.path.join(os.getcwd(), config_path))
    with open(self.__config_path, 'r') as f:
      config = json.load(f)

    # Config file processing
    self.__config_option_1 = config['configOption1']

    # Env processing for secrets
    self.__boilerplate_env_1 = os.environ['BOILERPLATE_ENV1']


  def __str__(self) -> str:
    return f'Configuration loaded from {self.__config_path}'


  def get_boilerplate_settings(self) -> ConfigSettings:
    return {
      'config_option_1': self.__config_option_1,
      'boilerplate_env_1': self.__boilerplate_env_1,
    }
