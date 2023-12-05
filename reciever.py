from component.chat_message import ChatMessage
from component.Text_file_Process import TextFileProcess
from component import utils
import os,sys,socket,time

#creating Instance of the classes
Chat_msg_obj = ChatMessage()
current_path = os.getcwd()
artifact_dir_path = os.path.join(current_path,'Artifact')
textfile_class_obj = TextFileProcess()


# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

my_ip="0.0.0.0"
my_port=1122
my_address=(my_ip,my_port)
server_socket.bind(my_address)
server_socket.listen()

client_socket, client_address = server_socket.accept()
while True :

    recieved_data = client_socket.recv(1000000)
    message , ip_address , port = Chat_msg_obj.filter_message_address(RecieveDat=recieved_data , client_add=client_address)
    Data_label = utils.Data_identifier(Recieve_data_message=message) # to identifie the data

    if Data_label == "message":
        try:
            #file handling to save the Data of messaging
            message_artifact_path_with_ip = os.path.join(artifact_dir_path,ip_address,'chat_message')
            os.makedirs(message_artifact_path_with_ip, exist_ok=True)

            message_file_path = os.path.join(message_artifact_path_with_ip , 'inbox.txt')
            with open(message_file_path,'a+') as message_file:
                message_file.write('\n'+message[1:].decode('ascii'))

        except Exception as e:
            print(e)


    elif Data_label == "text-file":


        text_file_artifact_path_with_ip = os.path.join(artifact_dir_path,ip_address,'Text-files')
        os.makedirs(text_file_artifact_path_with_ip, exist_ok=True)

        textfile_class_obj.Data_resampling_write(Recieve_data=message, base_path=text_file_artifact_path_with_ip)
        print('Successfully Test-file Has Recieved !')
        break
    elif Data_label == "image":
        # FILE PATH HANDLING
        image_artifact_path_with_ip = os.path.join(artifact_dir_path,ip_address,'Images')
        os.makedirs(image_artifact_path_with_ip, exist_ok=True)

        # <<<<<<<<<< GET FILE NAME FROM FIRST PACKET OF DATA   >>>>>>>>>>>
        Data_label = recieved_data[0:1]
        file_name_with_extension = recieved_data[1:recieved_data.find(b'|')]
        file_name_with_extension = file_name_with_extension.decode('ascii')


        Data = recieved_data[recieved_data.find(b'|')+1:]
        image_file_path = os.path.join(image_artifact_path_with_ip,str(file_name_with_extension))          # <<<<<<<< FILE NAME DECODING ERROR

         
        with open(image_file_path,'ab') as file:
            file.write(Data)
        
        remaining = True
        while remaining:
            remaining_data = client_socket.recv(1000000)

            if remaining_data:
                # write remaining packets
                with open(image_file_path,'ab') as file:
                    file.write(remaining_data)            
            else:
                break
        print('Successfully an image Has Recieved 😍')
        break
    elif Data_label == "pdf-file":
        # FILE PATH HANDLING
        Pdf_artifact_path_with_ip = os.path.join(artifact_dir_path,ip_address,'Pdfs')
        os.makedirs(Pdf_artifact_path_with_ip, exist_ok=True)

        # <<<<<<<<<< GET FILE NAME FROM FIRST PACKET OF DATA   >>>>>>>>>>>
        Data_label = recieved_data[0:1]
        file_name_with_extension = recieved_data[1:recieved_data.find(b'|')]
        file_name_with_extension = file_name_with_extension.decode('ascii')


        Data = recieved_data[recieved_data.find(b'|')+1:]
        pdf_file_path = os.path.join(Pdf_artifact_path_with_ip,str(file_name_with_extension))          # <<<<<<<< FILE NAME DECODING ERROR

         
        with open(pdf_file_path,'ab') as file:
            file.write(Data)
        
        remaining = True
        while remaining:
            remaining_data = client_socket.recv(1000000)

            if remaining_data:
                # write remaining packets
                with open(pdf_file_path,'ab') as file:
                    file.write(remaining_data)            
            else:
                break
        print('Successfully a Pdf Has Recieved 😍')
        break
    else:
        break

