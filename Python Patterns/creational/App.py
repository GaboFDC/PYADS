import FactoryMethod

def LoggerTest():
    factory = FactoryMethod.LoggerFactory()
    logger = factory.getLogger()
    logger.log("This is a log message")

LoggerTest()