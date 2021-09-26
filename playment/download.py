"""
This module contain utility code for downlaod video from youtube url

"""

import pytube
import config
import logging
logger=logging.getLogger()





def save_the_video(url):
    """
    save the video from youtube url into inpur folder

    :returns:
    file path of downlaoded video
    """
    try:   
        logger.info("Downlaod and save the video to directory")       
        youtube = pytube.YouTube(url)
        # check video availablity
        if (youtube.check_availability() == None): 
            
            video = youtube.streams.get_highest_resolution()
            file_name = video.default_filename
            logger.debug("Video file name: %s", file_name)
            # downloaded video will be saved in input folder of root diretory
            output_file_path = config.get_conf_value('video','SaveFolder')
            file_path = video.download(output_path = output_file_path, filename = file_name)
            return file_path
        else:
            raise Exception("video is not available") 
    except Exception as e:
        logger.error("oops: ", e)
        raise Exception("Oops: something went wrong while downloading video") 

         
#save_the_video("https://ww.youtube.cm/watch?v=tFRccV91_Og")
