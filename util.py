import functools
import logging

global GLOBAL_LOGGERS
GLOBAL_LOGGERS = {}

def get_logger(
        LOG_FORMAT='%(asctime)s | %(name)-12s | %(levelname)-8s | %(message)s',
        LOG_NAME='',
        LOG_FILE_INFO='logs/app.log',
        LOG_FILE_ERROR='logs/app.err.log'):
    """
    Source: 
    https://stackoverflow.com/questions/18911737/using-python-logging-module-to-info-messages-to-one-file-and-err-to-another-file

    """

    if LOG_NAME in GLOBAL_LOGGERS:
        return GLOBAL_LOGGERS[LOG_NAME]

    GLOBAL_LOGGERS[LOG_NAME] = log = logging.getLogger(LOG_NAME)
    log_formatter = logging.Formatter(LOG_FORMAT)

    # comment this to suppress console output
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    log.addHandler(stream_handler)

    file_handler_info = logging.FileHandler(LOG_FILE_INFO, mode='a')
    file_handler_info.setFormatter(log_formatter)
    file_handler_info.setLevel(logging.INFO)
    log.addHandler(file_handler_info)

    file_handler_error = logging.FileHandler(LOG_FILE_ERROR, mode='a')
    file_handler_error.setFormatter(log_formatter)
    file_handler_error.setLevel(logging.ERROR)
    log.addHandler(file_handler_error)

    log.setLevel(logging.INFO)

    return log


def exception_log(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        logger = get_logger()
        try:
            return function(*args, **kwargs)
        except:
            err  = 'There was an exception in '
            err += function.__name__
            logger.exception(err)
            raise
    return wrapper