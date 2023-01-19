import tkinter
import customtkinter  # <- import the CustomTkinter module
from pytube import YouTube # <- import Pytube

# def Download(link):
#     youtubeObject = YouTube(link)
#     youtubeObject = youtubeObject.streams.get_highest_resolution()
#     try:
#         youtubeObject.download()
#     except:
#         print("An error has occurred")
#     print("Download is completed successfully")


# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    # Set size
    WIDTH = 400
    HEIGHT = 240

    def __init__(self):

        super().__init__()

        # app window title
        self.title("YouTube Video Downloader")
        # app window width & height
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # call .on_closing() when app gets closed
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        # on page load
        self.home()

    def home(self):

        # vars that hold links
        self.link_var = tkinter.StringVar()

        # Insert Link Label
        self.insert_link_label = customtkinter.CTkLabel(master=self,
                                              text="Insert Link Below:",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.insert_link_label.pack(pady=10, padx=10)

        # Insert Link Entry
        self.link_entry = customtkinter.CTkEntry(master=self,
                                            width=250,
                                            textvariable=self.link_var,
                                            placeholder_text="YouTube Video Link...")
        self.link_entry.pack(padx=10, pady=10)

        # Download Button
        self.download_button = customtkinter.CTkButton(master=self,
                                                text="Download",
                                                corner_radius=10,
                                                command=self.test(str(self.link_var)))
        self.download_button.pack(padx=10, pady=10)

    # ALL FUNCTIONS HERE

    # YouTube Video Download
    def download(link):
        youtube = YouTube(link)
        youtube = youtube.streams.get_highest_resolution()
        try:
            youtube.download()
        except:
            print("An error has occurred, please try again")
        print("Download has completed successfully!")

    def test(self, link):
        print(self.link_var.set(link))

    # On close
    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()