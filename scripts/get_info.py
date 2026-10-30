from os import path

class Get_Info :
    def __init__(self):
        super().__init__()

    def Get_File (self):
        self.path_file = input('Please Enter Where Your Json File : ').strip()
        if path.exists(self.path_file):
            return self.path_file
        else :
            print(f'We are sorry this path {self.path_file} is not true, Try Again')
            self.Get_File()

    def Get_dir (self):
        return path.dirname(self.path_file)

    