# Tool Box

## 🚀 Usage
### 👤 User
Install by uv tool manager.
```sh
uv tool install .
```
### 🧑‍💻 Development
Activate Environment
```sh
uv sync --extra dev
```
```sh
source .venv/bin/activate
```
Debug
```sh
uv tool install . --editable
```
### 📦 Compressed-Files Extract
Extract all the compressed files in the `input` folder to the `output` folder.
```sh
tool-box compressed_files_extract
```
### 🌪️ Files Duplicate
Duplicate all the file of spcificed extension in the `input` folder to the `output` folder.
```sh
tool-box files_duplicate
```
### 🏷️ Files Rename
Rename all the file of spcificed extension in the `input` folder to the `output` folder.
```sh
tool-box files_rename
```
### 🗃️ Files Summary
Summary all the file in the `input` folder and its subfolders
to the `output` folder.
```sh
tool-box files_summary
```
### 📄 Images Merge to PDF
Merge all images in the `input` folder to PDF file in the `output` folder.
```sh
tool-box images_to_pdf
```
### 🌗 Images Reverse Color
Reverse the color of all images in the `input` folder to the `output` folder.
```sh
tool-box images_color_reverse
```
### ⏯️ Videos Encoding
Encoding all videos in the `input` folder to the `output` folder.
```sh
tool-box videos_encoding
```
### 🖼️ Videos to GIF
Transform all videos in the `input` folder to the GIF images in the `output` folder.
```sh
tool-box videos_to_gif
```
Specify frame rate.
```sh
tool-box videos_to_gif -fps 8
```
