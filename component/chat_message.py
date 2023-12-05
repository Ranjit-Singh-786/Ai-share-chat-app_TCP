import os , sys

class ChatMessage:
    def filter_message_address(self,RecieveDat,client_add):
        """Function returns message , ip address , port no"""
        try:
            
            message = RecieveDat[0:]
            ip_address = client_add[0]
            port_no = client_add[1]
            return message , ip_address , port_no
        except Exception as e:
            print(e)