import json
import os
import webbrowser
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return []

def open_resource(path):
    if path.startswith("http"):
        webbrowser.open(path)
    else:
        try:
            if os.name == 'nt':
                os.startfile(path)
            elif os.name == 'posix':
                os.system(f"xdg-open '{path}'")
            else:
                messagebox.showerror("Error", "Unsupported OS for opening files.")
        except Exception as e:
            messagebox.showerror("Error", f"Cannot open file: {e}")

def show_content_window(item):
    window = tk.Toplevel()
    window.title(item.get('title', 'بدون عنوان'))
    window.geometry("450x400")
    window.configure(bg="#f5f5f5")

    if 'image' in item and os.path.exists(item['image']):
        img = Image.open(item['image'])
        img = img.resize((300, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        img_label = tk.Label(window, image=photo, bg="#f5f5f5")
        img_label.image = photo
        img_label.pack(pady=10)

    desc = item.get('description', "No description available.")
    desc_label = tk.Label(window, text=desc, wraplength=400, justify="left", bg="#f5f5f5", font=("Arial", 12))
    desc_label.pack(pady=10, padx=10)

    if 'link' in item:
        open_btn = tk.Button(window, text="Open Resource", command=lambda: open_resource(item['link']),
                             bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), relief=tk.FLAT, padx=10, pady=5)
        open_btn.pack(pady=10)

class ToolsWindow(tk.Toplevel):
    def __init__(self, parent, category_name, tools):
        super().__init__(parent)
        self.title(f"Tools - {category_name}")
        self.geometry("600x400")
        self.configure(bg="#e0f7fa")

        label = tk.Label(self, text=f"{category_name} Tools", font=("Arial", 18, "bold"), bg="#006064", fg="white", pady=10)
        label.pack(fill=tk.X)

        frame = tk.Frame(self, bg="#e0f7fa", padx=15, pady=15)
        frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(frame, height=15, font=("Arial", 13), bg="white", fg="#004d40", selectbackground="#004d40", selectforeground="white", bd=0)
        for tool in tools:
            self.listbox.insert(tk.END, tool['title'])
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.selected_index = None
        self.tools = tools

        self.listbox.bind('<<ListboxSelect>>', self.store_selected_index)
        self.listbox.bind('<Return>', self.open_tool_detail)
        self.listbox.bind('<Double-Button-1>', self.open_tool_detail)

    def store_selected_index(self, event):
        selection = event.widget.curselection()
        self.selected_index = selection[0] if selection else None

    def open_tool_detail(self, event):
        if self.selected_index is not None:
            tool = self.tools[self.selected_index]
            show_content_window(tool)

class VideosWindow(tk.Toplevel):
    def __init__(self, parent, course_title, videos):
        super().__init__(parent)
        self.title(f"Videos - {course_title}")
        self.geometry("600x400")
        self.configure(bg="#fff3e0")

        label = tk.Label(self, text=course_title, font=("Arial", 18, "bold"), bg="#ef6c00", fg="white", pady=10)
        label.pack(fill=tk.X)

        frame = tk.Frame(self, bg="#fff3e0", padx=15, pady=15)
        frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(frame, height=15, font=("Arial", 13), bg="white", fg="#bf360c", selectbackground="#bf360c", selectforeground="white", bd=0)
        for video in videos:
            self.listbox.insert(tk.END, video['title'])
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.selected_index = None
        self.videos = videos

        self.listbox.bind('<<ListboxSelect>>', self.store_selected_index)
        self.listbox.bind('<Return>', self.open_video_detail)
        self.listbox.bind('<Double-Button-1>', self.open_video_detail)

    def store_selected_index(self, event):
        selection = event.widget.curselection()
        self.selected_index = selection[0] if selection else None

    def open_video_detail(self, event):
        if self.selected_index is not None:
            video = self.videos[self.selected_index]
            show_content_window(video)

class SectionWindow(tk.Toplevel):
    def __init__(self, parent, section_name, items):
        super().__init__(parent)
        self.title(section_name)
        self.geometry("600x400")
        self.configure(bg="#f0f4c3")

        self.section_name = section_name
        self.items = items

        label = tk.Label(self, text=section_name, font=("Arial", 18, "bold"), bg="#afb42b", fg="white", pady=10)
        label.pack(fill=tk.X)

        frame = tk.Frame(self, bg="#f0f4c3", padx=20, pady=15)
        frame.pack(fill=tk.BOTH, expand=True)

        self.items_listbox = tk.Listbox(frame, height=15, font=("Arial", 13), bg="white", fg="#827717", selectbackground="#827717", selectforeground="white", bd=0)
        self.items_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.items_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.items_listbox.config(yscrollcommand=scrollbar.set)

        for item in items:
            if isinstance(item, dict):
                if 'course_title' in item:
                    title = item['course_title']
                elif 'category' in item:
                    title = item['category']
                else:
                    title = item.get('title', 'No Title')
            else:
                title = str(item)
            self.items_listbox.insert(tk.END, title)

        self.selected_index = None
        self.items_listbox.bind('<<ListboxSelect>>', self.on_select_store)
        self.items_listbox.bind('<Double-Button-1>', self.open_selected_item)
        self.items_listbox.bind('<Return>', self.open_selected_item)

    def on_select_store(self, event):
        selection = event.widget.curselection()
        self.selected_index = selection[0] if selection else None

    def open_selected_item(self, event):
        if self.selected_index is None:
            return
        item = self.items[self.selected_index]

        if isinstance(item, dict):
            if 'course_title' in item and 'videos' in item:
                VideosWindow(self, item['course_title'], item['videos'])
            elif 'category' in item and 'tools' in item:
                ToolsWindow(self, item['category'], item['tools'])
            else:
                show_content_window(item)
        else:
            messagebox.showinfo("Info", str(item))

class HarmApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HARM - Cybersecurity Hub")
        self.geometry("600x400")

        self.original_bg_image = Image.open("/home/kali/Desktop/HARM/images/welcome.png")
        self.bg_image = self.original_bg_image.resize((self.winfo_width(), self.winfo_height()), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.start_button = tk.Button(self, text="START", font=("Arial", 18, "bold"),
                                      fg="white", bg="green", activebackground="darkgreen",
                                      command=self.show_main_ui)
        self.start_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        self.bind("<Configure>", self.resize_bg)

        self.sections = {
            "Leaked courses in every field of cybersecurity": "data/leaked_courses.json",
            "The dark web": "data/dark_web.json",
            "HARM videos": "data/harm_videos.json",
            "The latest vulnerabilities in the field": "data/vulnerabilities.json",
            "News": "data/News.json",
            "ceh_v13_tools" : "data/ceh_v13_tools.json",

        }

        self.selected_section = None

        red_icon_path = "/home/kali/Desktop/HARM/images/red_icon.png"
        if os.path.exists(red_icon_path):
            icon_img = Image.open(red_icon_path).resize((20, 20), Image.Resampling.LANCZOS)
            self.red_icon = ImageTk.PhotoImage(icon_img)
        else:
            self.red_icon = None

    def resize_bg(self, event):
        if event.widget == self:
            new_width = event.width
            new_height = event.height
            resized = self.original_bg_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(resized)
            if hasattr(self, 'bg_label') and self.bg_label.winfo_exists():
                self.bg_label.config(image=self.bg_photo)
                self.bg_label.image = self.bg_photo

    def show_main_ui(self):
        self.start_button.destroy()
        if hasattr(self, 'bg_label') and self.bg_label.winfo_exists():
            self.bg_label.destroy()

        label = tk.Label(self, text="Welcome to HARM", font=("Arial", 22, "bold"), fg="white", bg="#2e7d32")
        label.pack(fill=tk.X)

        frame = tk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.listbox = tk.Listbox(frame, font=("Arial", 14), bg="white", fg="#1b5e20", selectbackground="#1b5e20", selectforeground="white", bd=0)
        for section in self.sections.keys():
            self.listbox.insert(tk.END, section)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.listbox.bind('<<ListboxSelect>>', self.on_section_select)
        self.listbox.bind('<Return>', self.open_selected_section)
        self.listbox.bind('<Double-Button-1>', self.open_selected_section)

        if self.red_icon:
            # add red icon next to first item (optional)
            self.listbox.image_create(0, image=self.red_icon)

    def on_section_select(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            self.selected_section = list(self.sections.keys())[index]
        else:
            self.selected_section = None

    def open_selected_section(self, event):
        if not self.selected_section:
            return
        json_path = self.sections[self.selected_section]
        data = load_json(json_path)

        if self.selected_section == "HARM videos":
            # Open videos window
            videos = data.get('videos', []) if isinstance(data, dict) else data
            VideosWindow(self, self.selected_section, videos)
        elif isinstance(data, list) and data and isinstance(data[0], dict):
            # If it's a list of courses/categories/tools
            SectionWindow(self, self.selected_section, data)
        else:
            messagebox.showinfo("Info", f"No detailed data available for {self.selected_section}")

if __name__ == "__main__":
    app = HarmApp()
    app.mainloop()
                   
