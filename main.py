import flet as ft
from controller import NotepadController

def main(page: ft.Page):
    """Initializes and runs the application"""
    page.title = "Notepad Launcher"
    page.window.width = 500
    page.window.height = 600
    page.padding = 20
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)
    page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.DEEP_PURPLE)
    NotepadController(page)

if __name__ == "__main__":
    ft.app(target=main)
