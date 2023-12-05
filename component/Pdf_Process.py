import os 


class PdfSender:
    def __init__(self):
        pass

    def SendPdf(self,pdf_path,client_socket,file_wth_ext):
        try:
            with open(pdf_path,'rb') as pdf:
                data = pdf.read()

        # >>>>>>>>>> ADDING LABEL WITH DATA  <<<<<<<<<<<<<<
            label_tag = '3'+file_wth_ext+'|'
            data_with_tag = label_tag.encode('ascii')+data
            client_socket.send(data_with_tag)
            print('Your Pdf has been sent 😍😊')

            
        except Exception as e:
            print(e)