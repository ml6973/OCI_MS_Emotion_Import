import ConfigParser
import os


def init():
    get_config()

    global url
    url = config.get('GlobalInformation', 'url')

    global subKey
    subKey = config.get('GlobalInformation', 'subKey')

    global dbIP
    dbIP = config.get('GlobalInformation', 'dbIP')

    global dbUser
    dbUser = config.get('GlobalInformation', 'dbUser')

    global dbPass
    dbPass = config.get('GlobalInformation', 'dbPass')
   
def get_config():
    global config
    config = ConfigParser.RawConfigParser()
    package_directory = os.path.dirname(os.path.abspath(__file__))
    config.read(os.path.join(package_directory, 'config.txt'))
