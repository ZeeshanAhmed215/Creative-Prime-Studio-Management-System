
try:
        import  tkinter as tk
        import customtkinter as cu
        from tkinter import ttk,messagebox as msg
        from PIL import Image
        import mysql.connector
        from function import home,Orders,Employees
except ModuleNotFoundError:
        msg.showerror("Module Not Found","Please! Check the module ...........")
 

cu.set_appearance_mode("dark")
cu.set_default_color_theme("dark-blue")

def switch_option(switch_to):
    match switch_to:
        case "Home":
                for wed in big_frame.winfo_children():
                        wed.destroy()
                home(big_frame)
                home_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # ============
                register_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
                view_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
               

                
        case "Registration":
                for wed in big_frame.winfo_children():
                        wed.destroy()
                Employees(big_frame)
                register_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # ================
                home_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
                view_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
                

                
        case "View":
                for wed in big_frame.winfo_children():
                        wed.destroy()
                Orders(big_frame)
                view_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # ===============
                home_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
                register_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
                






Windows=cu.CTk()
Windows.title("Creative Prime Studio")
Windows.geometry("1500x650")
tabs_frame=cu.CTkFrame(Windows)
tabs_frame.pack(pady=20)
big_frame=cu.CTkFrame(Windows,width=1300,height=600,corner_radius=20,)
big_frame.pack(pady=20,fill="both",expand=1)



home(big_frame)



home_tab=cu.CTkButton(tabs_frame,text="Home",border_width=3,border_color="#FFFFFF",corner_radius=10,font=("Times",25),fg_color="#1F6AA5",command=lambda: switch_option("Home"))
home_tab.grid(row=0,column=0,padx=10)
register_tab=cu.CTkButton(tabs_frame,text="Employees",border_width=3,border_color="#FFFFFF",corner_radius=10,font=("Times",25),fg_color="#1F6AA5",command=lambda: switch_option("Registration"))
register_tab.grid(row=0,column=1,padx=10)
view_tab=cu.CTkButton(tabs_frame,text="Orders",border_width=3,border_color="#FFFFFF",corner_radius=10,font=("Times",25),fg_color="#1F6AA5",command=lambda: switch_option("View"))
view_tab.grid(row=0,column=2,padx=10,)


Windows.mainloop()















































































































































































































































































































    # if switch_to=="Home":
    #     home_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # ============
    #     register_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     view_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     setting_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    
    
    # elif switch_option=="Registration":
    #     register_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # ================
    #     home_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     view_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     setting_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    
    # elif switch_option=="View":
    #     view_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # ===============
    #     home_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     setting_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     register_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")

    
    # elif switch_option=="Setting":
    #     setting_tab.configure(fg_color="#1F6AA5",border_color="#FFFFFF")
    #     # =================
    #     home_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     view_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")
    #     register_tab.configure(fg_color="#4B4948",border_color="#FFFFFF")


# try:

#         db=mysql.connector.connect(
#         host="your host name",
#         user="your user name",
#         password="your password of Mysql",
#         database="your name of database"
#         )
# except (mysql.connector.errors.OperationalError,
#         mysql.connector.errors.ProgrammingError,
#         mysql.connector.errors.IntegrityError,
#         mysql.connector.errors.ConnectionTimeoutError,
#         ):
#              msg.showerror("Database Not Found","Please! Check the connection of your database...........")
                                       

# cursor=db.cursor()
# cursor.execute(f"select * from admin")
# data=cursor.fetchall()
# for result in data:
#         print(result)
        


# db.commit()
# cursor.close()
# db.close()