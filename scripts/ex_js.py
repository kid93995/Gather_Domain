import json
from scripts.get_info import Get_Info

class Extract_Json (Get_Info) :
    def __init__(self):
        super().__init__()


    # This method used to open json file.
    def Open_Json (self):
        with open(self.Get_File(), 'r', encoding = 'utf-8') as file_json :
            self.sub_domains = json.load(file_json)


    
    # this method extract subdomains from json file.
    def Ex_Json (self):

        self.word = input('Enter the word whose value you want to extract :').strip()
        self.file_name = input('Enter file name :').strip()

        for Sub_Domain in self.sub_domains :
            with open (f'{self.Get_dir()}/{self.file_name}.txt','a', encoding = 'utf-8') as file_domains :
                file_domains.write(f'{Sub_Domain[self.word]}\n')
            
