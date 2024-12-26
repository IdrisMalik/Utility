# Notepad Launcher

A Python GUI application that creates and opens multiple text files simultaneously. Built with Flet, this tool provides an easy way to generate and manage multiple text files with custom content.

## Features

- Create multiple text files with a custom base filename
- Specify the number of files to generate (1-1000)
- Add initial content to all files
- Automatically open files in your default text editor
- Modern, user-friendly interface
- Dark/Light theme support

## Prerequisites

- Python 3.7 or higher
- Flet library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/IdrisMalik/notepad.git
cd notepad
```

2. Install required packages:
```bash
pip install flet
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Using the interface:
   - Click "Select Folder" to choose where files will be created
   - Enter a base filename (e.g., "note")
   - Specify the number of files to create
   - (Optional) Add content that will be included in each file
   - Click "Create and Open Files"

## Project Structure

```
notepad/
├── main.py         # Application entry point
├── model.py        # Data and file operations
├── view.py         # User interface components
├── controller.py   # Application logic and event handling
└── README.md       # This file
```

## Acknowledgments

- Built with [Flet](https://flet.dev/) - Flutter-like framework for Python
- Follows the MVC (Model-View-Controller) design pattern
