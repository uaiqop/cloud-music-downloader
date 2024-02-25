from configparser import ConfigParser

def download_dir():
    config = ConfigParser()
    config.read("./config", "utf-8")
    return config["Download"]["DownloadDir"]