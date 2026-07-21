from configparser  import ConfigParser
import os

config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Configuration", "config.ini")

config = ConfigParser()
config.read(config_path)


class ReadConfig:

    @staticmethod
    def get_application_url():
        return config.get("info", "baseUrl")


