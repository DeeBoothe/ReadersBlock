#!/usr/bin/env python
# coding: utf-8

# In[1]:


# run the first time to install the custom module
# pip install customtkinter
# https://github.com/TomSchimansky/CustomTkinter

import tkinter.ttk as ttk
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


# In[2]:


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.title("Reader's Block")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Reader's Block",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Sign In",
                                                command=self.sign_in_button)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Register Account",
                                                command=self.register_button)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=4)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")
        
        

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        

        
        

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Welcome to Reader's Block!\n" +
                                                        "\n" +
                                                        "Please sign in to your existing account or register a new account." ,
                                                   height=400,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        

        # set default values
        self.optionmenu_1.set("Dark")
       
    def sign_in_button(self):
        self.destroy()
        if __name__ == "__main__":
            app1 = SignIn()
            app1.mainloop()
    
    def register_button(self):
        self.destroy()
        if __name__ == "__main__":
            app2 = Register()
            app2.mainloop()
               
            
            
    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()
        
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# In[3]:


class SignIn(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.title("Reader's Block")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Reader's Block",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Sign In",
                                                command=self.sign_in_button)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Register Account",
                                                command=self.register_button)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=4)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="         Sign in by entering your\n" +
                                                        "\n" +
                                                        "Username and Password below" ,
                                                   height=400,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        
        self.entry = customtkinter.CTkEntry(master=self.frame_info,
                                            width=120,
                                            placeholder_text="Username")
        self.entry.grid(row=1, column=0, columnspan=2, pady=20, padx=120, sticky="we")
        
        self.entry2 = customtkinter.CTkEntry(master=self.frame_info,
                                            width=120,
                                            placeholder_text="Password")
        self.entry2.grid(row=2, column=0, columnspan=2, pady=20, padx=120, sticky="we")
        
        self.button_1 = customtkinter.CTkButton(master=self.frame_info,
                                                text="Login",
                                                command=self.login_button)
        self.button_1.grid(row=3, column=0, pady=30, padx=30)


        # set default values
        self.optionmenu_1.set("Dark")
       
    def sign_in_button(self):
        self.destroy()
        if __name__ == "__main__":
            app1 = SignIn()
            app1.mainloop()
    
    def register_button(self):
        self.destroy()
        if __name__ == "__main__":
            app2 = Register()
            app2.mainloop()
            
            
    def login_button(self):
        print("Login")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()
        
        
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# In[4]:


class Register(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.title("Reader's Block")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Reader's Block",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Sign In",
                                                command=self.sign_in_button)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Register Account",
                                                command=self.register_button)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=4)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")
        
        self.entry3 = customtkinter.CTkEntry(master=self.frame_info,
                                            width=120,
                                            placeholder_text="First Name")
        self.entry3.grid(row=1, column=0, columnspan=2, pady=10, padx=120, sticky="we")
        
        self.entry4 = customtkinter.CTkEntry(master=self.frame_info,
                                            width=120,
                                            placeholder_text="Last Name")
        self.entry4.grid(row=2, column=0, columnspan=2, pady=10, padx=120, sticky="we")
        
        self.entry5 = customtkinter.CTkEntry(master=self.frame_info,
                                            width=120,
                                            placeholder_text="Email Address")
        self.entry5.grid(row=3, column=0, columnspan=2, pady=10, padx=120, sticky="we")
        
        self.entry6 = customtkinter.CTkEntry(master=self.frame_info,
                                            width=120,
                                            placeholder_text="Password")
        self.entry6.grid(row=4, column=0, columnspan=2, pady=10, padx=120, sticky="we")
        
        
        self.button_2 = customtkinter.CTkButton(master=self.frame_info,
                                                text="Register",
                                                command=self.register_account_button)
        self.button_2.grid(row=7, column=0, pady=30, padx=30)

        


        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Enter the required information\n" +
                                                        "\n" +
                                                        " below to register an account" ,
                                                   height=400,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)


        # set default values
        self.optionmenu_1.set("Dark")
       
    def sign_in_button(self):
        self.destroy()
        if __name__ == "__main__":
            app1 = SignIn()
            app1.mainloop()
    
    def register_button(self):
        self.destroy()
        if __name__ == "__main__":
            app2 = Register()
            app2.mainloop()
            
    def register_account_button(self):
        print("Account Registered")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()
        
        
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# In[ ]:


if __name__ == "__main__":
    app = App()
    app.mainloop()


# In[ ]:




