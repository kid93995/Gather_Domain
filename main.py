from termcolor import colored
from scripts.ex_js import Extract_Json




def Main ():
    file_json = Extract_Json()
    file_json.Open_Json()
    file_json.Ex_Json()

    print(colored('Extract json Successful!', 'black', 'on_green'))

if __name__ == "__main__":
    Main()



# /home/kali/web_pentesting/verisk.com/recon/verisk.com subdomains.json
# 