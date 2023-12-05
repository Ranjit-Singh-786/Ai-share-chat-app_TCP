import os ,sys

class TextFileProcess:

    def Data_sampling(self,file_path,file_name):
        """This function returns text data after reading from text file. and label and filename"""
        try:

            with open(file_path,'r',encoding='utf-8') as file:
                file_data = file.read()
                Data_label = "1"
                file_data_with_label = Data_label + file_name + '|' + file_data
                encrypted_file_data_with_label = file_data_with_label.encode('ascii')
            return encrypted_file_data_with_label


        except Exception as e:
            print(e)




    def Data_resampling_write(self,Recieve_data , base_path):
        try:
            Recieve_data = Recieve_data.decode('ascii')
            Data_label = Recieve_data[0]
            file_name_wth_ext = Recieve_data[1:Recieve_data.find('|')]
            Data = Recieve_data[Recieve_data.find('|')+1:]
            file_name = file_name_wth_ext
            file_dir_path = base_path + "\\"+file_name_wth_ext
            with open(file_dir_path ,'w',encoding='utf-8') as text_file:
                text_file.write(Data)
        except Exception as e:
            print(e)