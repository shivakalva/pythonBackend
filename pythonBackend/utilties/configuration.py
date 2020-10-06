import configparser


def getconfig():
    config = configparser.ConfigParser()
    config.read("utilties/properties.ini")
    print(config)
    return config
