import os,sys

def Data_identifier(Recieve_data_message):
    try:
        chunk = Recieve_data_message[0:2]
        decoded_data = chunk.decode('ascii')
        Data_label = decoded_data[0]

        # There are Data label
        # 0   --->  Message
        # 1   --->  Text file
        # 2   --->  Image 
        # 3   --->  Pdf File
        if Data_label == '0':
            return 'message'
        elif Data_label == '1':
            return 'text-file'
        elif Data_label=='2':
            return 'image'
        else:
            return 'pdf-file'

    except Exception as e:
        print(e)


def file_type_identifier(file_path):
    file_name_with_ext = os.path.basename(file_path)
    filename, extension = os.path.splitext(file_name_with_ext)

    if extension.lower() == '.txt':
        try:
            with open(file_path, 'r') as text_file:
                content = text_file.read()
                return 'text-file', file_name_with_ext
        except UnicodeDecodeError:
            pass  # If there's a UnicodeDecodeError, it's not a text file

    # Check for image files
    image_extensions = ['.jpg', '.jpeg', '.png']
    if extension.lower() in image_extensions:
        try:
            from PIL import Image
            image = Image.open(file_path)
            return 'image', file_name_with_ext
        except Exception as e:
            pass  # If there's an exception, it's not an image file

    # Check for PDF files
    if extension.lower() == '.pdf':
        try:
            return 'pdf-file', file_name_with_ext
        except Exception as e:
            pass  # If there's an exception, it's not a PDF file

    return 'Unsupported file type', file_name_with_ext

