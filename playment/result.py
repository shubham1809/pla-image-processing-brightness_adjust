'''
This module is used to save processed video in specific folder
'''
import cv2
import numpy as np
import download
import config
import logging
import transformer

logger=logging.getLogger(__name__)



def get_video_writer(fps, frame_size):
    '''
     this method create video writer object with same frame size and fps rate
     Input: fps(No of frame per second)
            frame_size( width and height of frame)
     output:  video writer object
    '''
    try:
        logging.debug("frame size : %s, FPS rate: %s",frame_size, fps)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        output_file = config.get_conf_value('video','OutputFolder') + "/output.mp4"
        logging.debug("output file path : %s", output_file )
        video_writer = cv2.VideoWriter(output_file,fourcc, fps, frame_size)
        return video_writer
    except Exception as e:
        logger.error("oops: ", e)
        raise Exception("Oops: something went wrong while getting  video object")
