import os,sys
from PIL import Image
import io
import numpy as np 
from typing import List
import time

class ImageSender:
    def __init__(self):
        pass


    def SendingImage(self,image_path,s,file_name_wth_extension):
        try:
            with open(image_path,'rb') as file:
                data = file.read()

        # >>>>>>>>>>>> TO RESIZE THE IMAGE   <<<<<<<<<<<<<<<<<<<<<
                # file_name , extension = file_name_wth_extension.split('.')
                # image = Image.open(io.BytesIO(data))
                # new_size = (950, 670)  # Replace with your desired dimensions
                # resized_image = image.resize(new_size)
                # resized_data = io.BytesIO()
                # resized_image.save(resized_data, format=extension)  # Adjust format as needed
                # resized_data = resized_data.getvalue()

        # >>>>>>>>>> ADDING LABEL WITH DATA  <<<<<<<<<<<<<<
                label_tag = '2'+file_name_wth_extension+'|'
                data_with_tag = label_tag.encode('ascii')+data
                # data_with_tag = label_tag.encode('ascii')+resized_data        

                print(len(data_with_tag))
                s.send(data_with_tag)      #  <-- IMAGE SENT




        # >>>>>>>>>> CODE TO SENDING IMAGE IN DATA PACKETS    <<<<<<<<<<<<<<<<<<
                # sent_packets = 0
                # cost_mul = 20000
                # total_pack = len(data_with_tag)
                # i = 0
                # while sent_packets <= total_pack:
                #     if i == 0:
                #         s.send(data_with_tag[0:cost_mul],destination)
                #         sent_packets += cost_mul
                #         i+=1
                #         time.sleep(1)
                #     else:
                #         remaining = len(data_with_tag[cost_mul:])
                #         difference = total_pack - remaining

                #         if difference >= 20000:
                #             s.send(data_with_tag[cost_mul:cost_mul*2],destination)
                #             cost_mul = cost_mul * 2 
                #             sent_packets = cost_mul
                #             time.sleep(1)
                #         else:
                #             last_remaining = len(data_with_tag[cost_mul:])
                #             s.send(data_with_tag[cost_mul:],destination)
                #             sent_packets += last_remaining
                #             time.sleep(1)

        except Exception as e:
            print(e)

    def Img_to_array_single(self,image_path:str):
        try:
            file_name_with_extension = os.path.basename(image_path)
            file_name ,  extension = file_name_with_extension.split('.')
            image = Image.open(image_path)
            arr_img = np.array(image)
            label_list = [2,file_name_with_extension,file_name,extension]
            return arr_img,label_list

        except Exception as e:
            print(e)



    def Array_to_img_single(self,img_array, saving_img_path:str,labels:list):
        try:
            image = Image.fromarray(img_array)
            image_saving_file_path = os.path.join(saving_img_path,labels[1])
            image.save(image_saving_file_path)
        except Exception as e:
            print(e)





    