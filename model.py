import os
import time
import subprocess
import sys

class NotepadModel:
    def __init__(self):
        self.folder_path = ""
        self.base_filename = ""
        self.file_count = 1
        self.initial_content = ""
        
    def validate_inputs(self):
        """Validates all input parameters before file creation"""
        if not os.path.isdir(self.folder_path):
            return False, "Please select a valid folder."
            
        if not self.base_filename or any(char in '/\\:*?"<>|' for char in self.base_filename):
            return False, "Invalid base filename. Avoid special characters."
            
        try:
            count = int(self.file_count)
            if not 1 <= count <= 1000:
                return False, "File count must be between 1 and 1000."
        except ValueError:
            return False, "Please enter a valid number for file count."
            
        return True, ""

    def create_files(self):
        """Creates multiple text files with specified content"""
        created_files = []
        for i in range(1, int(self.file_count) + 1):
            file_name = f"{self.base_filename}{i}.txt"
            file_path = os.path.join(self.folder_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.initial_content)
            created_files.append(file_path)
            time.sleep(0.1)
        return created_files

    def open_files(self, file_paths):
        """Opens files using system's default text editor"""
        for file_path in file_paths:
            try:
                if os.name == 'nt':
                    os.startfile(file_path)
                elif os.name == 'posix':
                    subprocess.call(('open' if sys.platform == 'darwin' else 'xdg-open', file_path))
            except Exception as e:
                print(f"Error opening {file_path}: {str(e)}")

    def process_files(self):
        """Main workflow for file creation and opening"""
        success, message = self.validate_inputs()
        if not success:
            return False, message

        try:
            created_files = self.create_files()
            self.open_files(created_files)
            return True, f"Successfully created and opened {self.file_count} files."
        except Exception as e:
            return False, f"Error: {str(e)}"
