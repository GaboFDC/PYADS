class Logger():
    """Abstract logger"""

    def log(self, message):
        pass

class ConsoleLogger(Logger):
    """Concrete logger to the console"""

    def log(self, message):
        print(message)

class FileLogger(Logger):
    """Concrete logger to a file"""

    def log(self, message):
        with open('factory.log', 'a') as logfile:
            logfile.write(message+"\n")

import ConfigParser

class LoggerFactory():
    """Factory that creates the appropiate logger based on the config file"""

    def getLogConfig(self):
        config = ConfigParser.RawConfigParser()
        config.read('factory.cfg')
        logging_type = config.get("logging", "type")
        return logging_type

    def getLogger(self):
        logging_type = self.getLogConfig()
        print("logging type: "+logging_type)
        if logging_type == "File":
            logger = FileLogger()
        elif logging_type == "Console":
            logger = ConsoleLogger()

        return logger
