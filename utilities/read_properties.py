import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\Admin\\PycharmProjects\\bankingproject\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('common info', 'url')

    @staticmethod
    def getUsername():
        return config.get('common info', 'username')

    @staticmethod
    def getPassword():
        return config.get('common info', 'password')
