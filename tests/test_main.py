from mock import patch
from mocks.config_mock import ConfigurationMock


with patch('config.Configuration', new=ConfigurationMock):
  from main import main


class TestMain:
  def test_config_create(self):
    """should return default config"""

    assert str(main('some/path')) == 'Configuration loaded from mock'
    assert main('some/path').get_boilerplate_settings() == {
      'config_option_1': 'mock option',
      'boilerplate_env_1':  'mock env',
    }
