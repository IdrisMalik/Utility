import flet as ft
from model import NotepadModel
from view import NotepadView

class NotepadController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.model = NotepadModel()
        self.view = NotepadView(self)
        self._setup_page()

    def _setup_page(self):
        """Configures the application page"""
        self.page.overlay.append(self.view.folder_picker)
        self.page.add(self.view.build())

    def folder_picked(self, e: ft.FilePickerResultEvent):
        """Handles folder selection event"""
        if e.path:
            self.model.folder_path = e.path
            self.view.folder_display.value = f"Selected: {e.path}"
        else:
            self.model.folder_path = ""
            self.view.folder_display.value = "No folder selected"
        self.page.update()

    def create_files(self, e):
        """Handles file creation event"""
        self.model.base_filename = self.view.filename_field.value
        self.model.file_count = self.view.count_field.value
        self.model.initial_content = self.view.content_field.value

        success, message = self.model.process_files()
        self.view.status_message.value = message
        self.page.update()
