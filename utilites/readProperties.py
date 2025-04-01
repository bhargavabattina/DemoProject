import configparser


config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url=config.get('info','baseURL')
        return url

    @staticmethod
    def getUserName():
        username = config.get('login', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('login', 'password')
        return password

