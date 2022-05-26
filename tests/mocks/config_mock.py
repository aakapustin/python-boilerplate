class ConfigurationMock:
  def __init__(self, fsPath):
    pass

  def __str__(self) -> str:
    return 'Configuration loaded from mock'


  def get_boilerplate_settings(self):
    return {
      'config_option_1': 'mock option',
      'boilerplate_env_1':  'mock env',
    }
