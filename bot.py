import subprocess
import time
import os

def start_minecraft_server():
    os.chdir("C:\\mineserver")
    # Replace the following command with the actual command to start your Minecraft server
    command = "java @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.20.1-47.2.30/win_args.txt -nogui %*"
    subprocess.Popen(command)

def main():
    while True:
        start_minecraft_server()
        time.sleep(60 * 60 * 24) # Sleep for 24 hours before restarting the server

if __name__ == "__main__":
    main()