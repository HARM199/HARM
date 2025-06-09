🛡️ HARM - Cybersecurity Hub


![welcome](https://github.com/user-attachments/assets/c9de7075-f268-4f29-8a78-e05363e8c461)


**HARM** is an interactive graphical user interface application built with Tkinter and developed in Python. It aims to gather multiple cybersecurity resources such as videos, tools, articles, leaked courses, artificial intelligence, vulnerability analysis, visual content, and more—all organized in one easy-to-use platform.

## 💡 Key Features

- Organizes content into multiple categories  
- Displays images, descriptions, and links to videos or tools  
- Elegant and user-friendly graphical interface  
- Supports running on Windows and Linux (Kali Linux)  
- Showcases videos, hacking tools, articles, deep web content, threat analysis, and more...

## 📦 Requirements

To run the project on any operating system, make sure you have:

### ✅ Basic Requirements:
- Python 3.8 or newer  
- Tkinter library (usually pre-installed with Python)  
- Pillow library for image display  

✅ On Kali Linux:
The program runs directly if Python is already installed.

      sudo apt update && sudo apt upgrade -y

      sudo apt install python3 python3-pip -y

      sudo apt install python3-tk -y

      pip3 install pillow

      sudo apt install git -y

     git clone https://github.com/HARM199/HARM.git
    
    cd HARM
    
    python3 harm.py


           

✅ On Windows:
If Git is not installed on your system:

Go to this website: https://git-scm.com/downloads

Download the Windows version and install it normally (just like any other program).

After installation, open PowerShell or CMD and check if it works by typing:

    git --version

✅ 2. Install Python

If you don’t have Python:

Download it from: https://www.python.org/downloads/windows/

During installation, make sure to check the option: ✅ “Add Python to PATH”

✅ 3. Install required libraries

Open PowerShell or CMD and run these commands one by one:

     pip install pillow

     python -m pip install tk

✅ 4. Download the HARM project from GitHub

     git clone https://github.com/HARM199/HARM.git
     
     cd HARM

✅ 5. Modify the image path for welcome.png

Open the file harm.py for editing using Notepad:

     notepad harm.py
Then find this line (usually around line 186):

      self.original_bg_image = Image.open("/home/kali/Desktop/HARM/images/welcome.png")
And change it to:

      self.original_bg_image = Image.open("images/welcome.png")

✅ 6. Run the project

After saving the changes run:

    python harm.py

      
     
     

 Social Media Links
Follow me for more projects and content:

https://www.youtube.com/@Harm1903

https://t.me/Harm2890

 With you was HARM Peace, mercy, and blessings of God be upon you

