import os
import time

#*********************INSTALLATION AND UPDATES*************************

def install_and_update():
    print("Checking for youtube-dl and FFMpeg...")
    time.sleep(3)

    os.system("cd /usr/local/bin")
    if not os.path.exists('/usr/local/bin/youtube-dl'):

        print("youtube-dl is not installed. Installing now.")
        time.sleep(3)

        os.system("sudo wget https://yt-dl.org/downloads/2015.03.09/youtube-dl -O /usr/local/bin/youtube-dl")
        os.system("sudo chmod a+x /usr/local/bin/youtube-dl")
        os.system("sudo chmod rwx /usr/local/bin/youtube-dl")
        print("youtube-dl has been installed.")

        print("Now updating youtube-dl...")
        # -U updates program to latest version
        os.system("sudo /usr/local/bin/youtube-dl -U")

    else:

        print("Checking for update to youtube-dl...")
        os.system("sudo /usr/local/bin/youtube-dl -U")

    if not os.path.exists('/usr/local/bin/ffmpeg'):

        print("FFMpeg not installed. Installing now...")
        time.sleep(3)

        os.system("sudo wget http://ffmpeg.gusari.org/static/32bit/ffmpeg.static.32bit.latest.tar.gz -O /usr/local/bin/ffmpeg.tar.gz")
        os.system("sudo tar -zxvf /usr/local/bin/*.tar.gz -C /usr/local/bin")
        os.system("sudo chmod a+x /usr/local/bin/ffmpeg")
        os.system("sudo chmod a+x /usr/local/bin/ffprobe")
        os.system("sudo rm ffmpeg.tar.gz")
        print("FFMpeg has been installed")

    else:

        print("FFMpeg has already been installed.")


#******************DOWNLOADING VIDEOS/CONVERTING TO MP3******************

def convert_to_mp3():

    urls = []
    current_url = "1"

    while current_url != "":

        current_url = input('Enter URL(s) and double hit ENTER to start: ')

        urls.append(current_url)

    print("Done with query entry. Downloading videos from YouTube...")
    time.sleep(3)

    for i in urls:

        os.system("/usr/local/bin/youtube-dl --extract-audio --audio-format mp3 -o '%(title)s.%(ext)s' " + i)

    print("Finished.")


if __name__ == "__main__":

    install_and_update()
    convert_to_mp3()
