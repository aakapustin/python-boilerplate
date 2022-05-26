import os
import pytest
from json import JSONDecodeError
from config import Configuration


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
  os.environ['BOILERPLATE_ENV1'] = 'test env'
  yield
  del os.environ['BOILERPLATE_ENV1']


class TestConfig:
  def test_config_create(self):
    """should create config"""
    config_path = os.path.normpath(os.path.join(os.getcwd(), 'tests', 'resources', 'test_config.json'))
    config = Configuration(config_path)
    assert config.get_boilerplate_settings() == {
      'config_option_1': 'test',
      'boilerplate_env_1': 'test env',
    }


  def test_config_file_not_found(self):
    """should raise error if config file not exists"""
    config_path = '/not/exists/path.json'

    with pytest.raises(IOError) as excinfo:
      Configuration(config_path)
    
    assert "No such file or directory" in str(excinfo.value)


  def test_config_file_not_json(self):
    """should raise error if config file is not json"""
    config_path = os.path.normpath(os.path.join(os.getcwd(), 'tests', 'resources', 'test_config.not.json'))

    with pytest.raises(JSONDecodeError) as excinfo:
      Configuration(config_path)
    
    assert "Expecting property name enclosed in double quotes" in str(excinfo.value)


  def test_config_file_not_valid(self):
    """should raise error if config file not contains required keys"""
    config_path = os.path.normpath(os.path.join(os.getcwd(), 'tests', 'resources', 'not_valid_test_config.json'))

    with pytest.raises(KeyError) as excinfo:
      Configuration(config_path)
    
    assert "configOption1" in str(excinfo.value)
  

  def test_config_env_not_valid(self):
    """should raise error if config env not exists"""
    config_path = os.path.normpath(os.path.join(os.getcwd(), 'tests', 'resources', 'test_config.json'))

    tmp = os.environ['BOILERPLATE_ENV1']
    del os.environ['BOILERPLATE_ENV1']

    with pytest.raises(KeyError) as excinfo:
      Configuration(config_path)
    
    assert "BOILERPLATE_ENV1" in str(excinfo.value)
    os.environ['BOILERPLATE_ENV1'] = tmp


  def test_str_config(self):
    """should return string representation of object"""
    config_path = os.path.normpath(os.path.join(os.getcwd(), 'tests', 'resources', 'test_config.json'))
    config = Configuration(config_path)
    assert str(config) == f'Configuration loaded from {config_path}'
    