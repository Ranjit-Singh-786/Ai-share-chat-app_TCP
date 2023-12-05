import subprocess
import platform


def execute_script(script_name):
    try:
        platfrm = platform.system()
        if platfrm == 'Windows':
            subprocess.run(['python', script_name])
        else:
            subprocess.run(['python3',script_name])
    except FileNotFoundError:
        print(f"Error: {script_name} not found.")

if __name__ == "__main__":
    message = """Are you sender, press Y/N : """ 
    user_input = input(message)
    if user_input.lower() == 'y':
        execute_script('sender.py')
    else:
        execute_script('reciever.py')