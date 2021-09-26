'''
This module configure loggig detail and used to fetch other application 
configure value

'''
import configparser
import logging
from logging import config

#set config parser
app_config = configparser.ConfigParser()
#set file path of application config
app_config.read('../appconfig_dev.ini')



def get_conf_value(section,key_input):
    '''
    This function return value of configuration from section.
    Input: section (multiple section defined in config file i.e. logging, video)
           key_input (Key paramter which value need to retrieve)
    '''
    try: 
         return app_config[section][key_input]
    except: 
        raise Exception("Config Value did not find")

def set_log_config():
    '''
    This function set configuration of logging module. 
    we are streaimg to file and with specific format.
    log_level can be changed from congiguration file
    '''
    logger=logging.getLogger()
    try:
        log_level = get_conf_value('logging','loglevel')
        file_name = get_conf_value('logging','filename')
        
        logger.debug("filename: %s, log_level: %s", file_name,log_level)
        logging.basicConfig(filename=file_name,
                        format='%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(message)s',
                        filemode='a', level = log_level)
    except Exception as e:
        logger.error("oops: ", e)
        raise Exception("something went wrong while configuraing logging")
