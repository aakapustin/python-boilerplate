import argparse
from config import Configuration


def main(config_path: str) -> None:
  config = Configuration(config_path)
  return config


if __name__ == '__main__':
  from dotenv import load_dotenv
  load_dotenv()

  parser = argparse.ArgumentParser(prog='Python boilerplate', description='It\'s a boilerplate project for quick starting development')
  parser.add_argument("--config_path", help="path to configuration file", default='./config.json')
  args = parser.parse_args()
  main(args.config_path)
