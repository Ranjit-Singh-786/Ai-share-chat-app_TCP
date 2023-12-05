import os, sys, socket
from component.Text_file_Process import TextFileProcess
from component.Image_Process import ImageSender
from component.Pdf_Process import PdfSender
from PIL import Image
import numpy as np 
from component import utils

textfile_processObj = TextFileProcess()
img_sender_obj = ImageSender()
pdf_sender_obj = PdfSender()

cleint_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    


# target_ip = "127.0.0.1"
target_ip = "192.168.1.3"
target_port = 1122

final_target=(target_ip,target_port)
cleint_socket.connect(final_target)

title_message = """
What do you want to share ?
0    ---->  MESSAGE
1    ---->  FILE"""
print(title_message)
task_choice = input('Plz enter your choice :- ')
print()

if task_choice == '0':
    try:
        break_condition = True
        while break_condition:
            msg=input("Plz enter your message : ")
            if msg :
                msg = '0'+msg
                encrepted_message=msg.encode('ascii')
                cleint_socket.send(encrepted_message)
            else:
                break_condition = False
    except Exception as e:
        print(e)



else:
    #FILE SHARING
    file_path = input('Plz enter file path :- ')
    file_label , file_name_with_ext = utils.file_type_identifier(file_path)
    img_extension = ['jpg','jpeg','png']

    if file_label == 'image':
        # writing code for image forwarding
        img_sender_obj.SendingImage(image_path=file_path,s=cleint_socket,file_name_wth_extension=file_name_with_ext)
        print('Your file successfully sent 😉')


    elif file_label == 'text-file':
        # writing code for text-file
        encrypted_file_data_with_label = textfile_processObj.Data_sampling(file_path=file_path,file_name=file_name_with_ext)
        cleint_socket.send(encrypted_file_data_with_label)
        print("Successfully sent your file :- ",file_name_with_ext)

    elif file_label == 'pdf-file':

        pdf_sender_obj.SendPdf(pdf_path=file_path,client_socket=cleint_socket,file_wth_ext=file_name_with_ext)
 


    else:
        print('ye kya he Bsdk 🤬')


