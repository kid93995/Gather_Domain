import json
from scripts.get_info import Get_Info

class Extract_Json (Get_Info) :
    def __init__(self):
        super().__init__()

    def Open_Json (self):
        with open(self.Get_File(), 'r', encoding = 'utf-8') as file_json :
            self.sub_domains = json.load(file_json)

    def Ex_Json (self):

        for Sub_Domain in self.sub_domains :
          
            with open (f'{self.Get_dir()}/sub_domain_file.txt',
                       'a', encoding = 'utf-8') as file_domains :
                file_domains.write(f'{Sub_Domain["subdomain"]}\n')
            
