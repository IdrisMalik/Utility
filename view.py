import flet as ft

class NotepadView:
    def __init__(self, controller):
        self.controller = controller
        self._init_components()

    def _init_components(self):
        """Initializes all UI components"""
        self.folder_display = ft.Text("No folder selected")
        self.filename_field = ft.TextField(
            label="Base Filename",
            hint_text="Enter name for files (e.g., 'note')",
            tooltip="Files will be named: name1.txt, name2.txt, etc."
        )
        self.count_field = ft.TextField(
            label="Number of Files",
            value="1",
            hint_text="Enter number (1-1000)",
            keyboard_type=ft.KeyboardType.NUMBER,
            tooltip="How many files to create"
        )
        self.content_field = ft.TextField(
            label="Initial Content",
            multiline=True,
            min_lines=3,
            max_lines=5,
            hint_text="Optional: Enter content for the files"
        )
        self.create_button = ft.ElevatedButton(
            "Create and Open Files",
            on_click=self.controller.create_files
        )
        self.status_message = ft.Text()
        self.folder_picker = ft.FilePicker(
            on_result=self.controller.folder_picked
        )

    def build(self):
        """Builds and returns the main UI layout"""
        return ft.Column(
            width=400,
            controls=[
                self._build_folder_section(),
                self._build_settings_section(),
                self.create_button,
                self.status_message,
            ],
        )

    def _build_folder_section(self):
        """Builds the folder selection section"""
        return ft.Column([
            ft.Text(weight=ft.FontWeight.BOLD, value="Output Folder"),
            ft.Row([
                ft.ElevatedButton(
                    "Select Folder",
                    icon=ft.Icons.FOLDER_OPEN,
                    on_click=lambda _: self.folder_picker.get_directory_path()
                ),
            ], alignment=ft.MainAxisAlignment.START),
            self.folder_display,
            ft.Divider(),
        ])

    def _build_settings_section(self):
        """Builds the file settings section"""
        return ft.Column([
            ft.Text(weight=ft.FontWeight.BOLD, value="File Settings"),
            self.filename_field,
            self.count_field,
            self.content_field,
            ft.Divider(),
        ])
