import os
import configparser

# Get the correct path for both local and CI
config_path = os.path.join(os.path.dirname(__file__), "Configuration", "config.ini")
config = configparser.RawConfigParser()
config.read(config_path)

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        return os.getenv("BASE_URL") or config.get('info', 'baseURL')

    @staticmethod
    def getUserName():
        return os.getenv("USERNAME") or config.get('login', 'username')

    @staticmethod
    def getPassword():
        return os.getenv("PASSWORD") or config.get('login', 'password')