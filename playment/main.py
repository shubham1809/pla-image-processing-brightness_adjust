'''
This is starting point of script execution
'''
import config
import logging
import processing

logger=logging.getLogger(__name__)


if __name__ == '__main__':
    '''
    set config values and run main fuction
    '''
    try:
        logger.info("Script Execution started")
        print("Running.......................")
        config.set_log_config()
        processing.main()
        print("Completed")
        logger.info("Script Execution finished")
    except Exception as e:
        logger.error("oops: ", e)
