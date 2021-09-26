'''
This Module read video file and process each frame.
processed frame again write to new video object file.

'''
import cv2
import numpy as np
import download
import config
import logging
import transformer
import result

logger=logging.getLogger(__name__)



def main():
    '''
    this function downlaod video from youtube and save in specfic folder.
    after this each frame of video is get processed . We are using gamma correction technique
    for pixel transformation.
    
    '''
    try:
        url = config.get_conf_value('video','url')
        input_file_path = download.save_the_video(url)
        
        cap = cv2.VideoCapture(input_file_path)
        # check if url was opened
        if not cap.isOpened():
            logger.error('video can not not opened')
            exit(-1)
            
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        frame_size = (frame_width,frame_height)
        fps = cap.get(cv2.CAP_PROP_FPS)
        
        video_writer = result.get_video_writer(fps,frame_size)

        while True:
            # read frame
            ret, frame = cap.read()

            # check if frame is empty
            if not ret:
                break
            frame = transformer.apply_brightness_adjustment_gamma(frame)
            video_writer.write(frame)
            # display frame
            #cv2.imshow('frame', frame)

            if cv2.waitKey(30)&0xFF == ord('q'):
                break

        # release VideoCapture
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        logger.error("oops: ", e)
        raise Exception("Oops: something went wrong while prcoessing video")
        

