import configparser

confg=configparser.RawConfigParser()
confg.read(".\\Configurations\\config.ini")

class readConfig:
    @staticmethod
    def getApplicationUrl():
        url=confg.get('login_detaols','baseUrl')

    @staticmethod
    def getUsername():
        username=confg.get('login_details','username')
        return username

    @staticmethod
    def getPassword():
        password=confg.get('login_details','password')
        return password