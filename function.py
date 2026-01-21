

try:

        import  tkinter as tk
        import customtkinter as cu
        from tkinter import ttk,messagebox as msg
        from PIL import Image
        import mysql.connector
        from connection import database_data
        import pandas as pd
        import openpyxl
        
        

       
        
except ModuleNotFoundError:
        msg.showerror("Module Not Found","Please! Check the module ...........")
                  
 









try:

        db=mysql.connector.connect(
        host=database_data[0],
        user=database_data[1],
        password=database_data[2],
        database=database_data[3]
        )
except (mysql.connector.errors.OperationalError,
        mysql.connector.errors.ProgrammingError,
        mysql.connector.errors.IntegrityError,
        mysql.connector.errors.ConnectionTimeoutError,
        ):
             msg.showerror("Database Not Found","Please! Check the connection of your database...........")
                                       






def getting_data():
        try:
                cursor=db.cursor()
                quarry="SELECT * FROM admin"
                cursor.execute(quarry)
                data=cursor.fetchall()
                return data
                
                db.commit()
                cursor.close() 
        except (mysql.connector.errors.OperationalError,
        mysql.connector.errors.ProgrammingError,
        mysql.connector.errors.IntegrityError,
        mysql.connector.errors.ConnectionTimeoutError,
        ):
                        msg.showerror("Database Not Found","Please! Check the connection of database...........")

       





def Employees(big_frame):

                        # Making table area=================================================
        tb_frame=cu.CTkFrame(big_frame,corner_radius=20,height=250,width=1500) # pyright: ignore[reportUndefinedVariable]
        tb_frame.grid(row=0,column=0)
        table_frame = tk.Frame(tb_frame, bg="#000000", bd=2, relief="ridge")
        table_frame.place(x=5,y=10,width=1350,height=220,)
        scroll_x=tk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=tk.Scrollbar(table_frame,orient="vertical")
        col_names=("id","name","skill","phone","address","hiring_date")
        col_heading_names=("Employee ID","Name","Profession","Phone No","Address","Hiring Date")
        Customer_table=ttk.Treeview(table_frame,columns=(col_names),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="left",fill="y")
        scroll_x.config(command=Customer_table.xview)
        scroll_y.config(command=Customer_table.yview)
        for x,y in zip(col_names,col_heading_names):
              Customer_table.heading(x,text=y)
        Customer_table['show']='headings'

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                background="#313030",  
                fieldbackground="#363636", 
                foreground="#ffffff",   
                ) 
        style.configure("Treeview.Heading",
                background="#4a4a4a",
                #foreground="#FFFFFF",
                )
        style.configure("Treeview.Heading", font=("Times New Roman", 15, "bold"))
        style.configure("Treeview", font=("Times New Roman", 15),rowheight=25)
        Customer_table.pack(fill="both",expand=1)
        # Data insert area=================================
        try:
                cursor=db.cursor()
                quarry="SELECT * FROM employees "
                cursor.execute(quarry)
                data=cursor.fetchall()
                for row in data:
                        Customer_table.insert("","end",values=row)
                db.commit()
                cursor.close() 
        except (mysql.connector.errors.OperationalError,
        mysql.connector.errors.ProgrammingError,
        mysql.connector.errors.IntegrityError,
        mysql.connector.errors.ConnectionTimeoutError,
        ):
                        msg.showerror("Database Not Found","Please! Check the connection of database...........")



        def refresh():
                for rows in Customer_table.get_children():
                        Customer_table.delete(rows)
                
                try:
                        cursor=db.cursor()
                        quarry="SELECT * FROM employees"
                        cursor.execute(quarry)
                        data=cursor.fetchall()
                        for row in data:
                                Customer_table.insert("","end",values=row)
                        db.commit()
                        cursor.close() 
                except (mysql.connector.errors.OperationalError,
                mysql.connector.errors.ProgrammingError,
                mysql.connector.errors.IntegrityError,
                mysql.connector.errors.ConnectionTimeoutError,
                ):
                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
        




       
        Form =cu.CTkFrame(big_frame,corner_radius=20 )
        Form.grid(row=1,column=0,padx=10,pady=10)




        cu.CTkLabel(Form, text="Registration Form", font=("Arial Rounded MT Bold",50),
           ).grid(row=0, column=0, columnspan=10, pady=10)
        Name_lab=cu.CTkLabel(Form,text="Name:",font=("Arial Rounded MT Bold",22,"bold")).grid(row=1,column=0)
        prof_lab=cu.CTkLabel(Form,text="Profession:",anchor="ne",font=("Arial Rounded MT Bold",22,"bold")).grid(row=1,column=3)
        phone_lab=cu.CTkLabel(Form,text=" Phone No:",font=("Arial Rounded MT Bold",22,"bold")).grid(row=2,column=0)
        address_lab=cu.CTkLabel(Form,text="Address:",anchor="ne",font=("Arial Rounded MT Bold",22,"bold")).grid(row=2,column=3)

        st_name_ent=cu.CTkEntry(Form,placeholder_text="Hussain Raza",width=250,font=("Cambria (Headings)", 20))
        st_name_ent.grid(row=1,column=1,padx=15,pady=5)
        st_prof_ent=cu.CTkEntry(Form,placeholder_text="Python developer",width=250,font=("Cambria (Headings)", 20))
        st_prof_ent.grid(row=1,column=4,padx=10,pady=5)
        address_ent=cu.CTkEntry(Form,placeholder_text="Sukkur Sindh Pakistan",width=250,font=("Cambria (Headings)", 20))
        address_ent.grid(row=2,column=4,pady=5,padx=10)
        phone_ent=cu.CTkEntry(Form,placeholder_text="+923473228701",width=250,font=("Cambria (Headings)", 20))
        phone_ent.grid(row=2,column=1,pady=5,padx=10)

        def booking():
                customer_data_list=[st_name_ent.get().title().strip(),st_prof_ent.get().title().strip(),address_ent.get().title().strip(),phone_ent.get().strip()]
                
                def data_verify(data_list):
                        data_list=list(data_list)
                        for element in data_list:
                                if element=="":
                                        msg.showerror("Missing Fields Error","Please! Fill out all required fields.\nThis will help us process your request.\nYou have some missing information.\nPlease! Review and complete the form. ")
                                        return  None
                                
                                        
                        import re               
                        
                        phone_pattern=re.compile(r"^(\+92|0)?3\d{9}$")
                        if phone_pattern.match(str(data_list[-1])):
                                
                                return data_list
                                
                        else:
                                msg.showerror("Data Validation Error","Please! Fill out all required fields with correct data.\nThis will help us process your request.\nYou have entered some wrong information.\nPlease! Review and complete the form with correct data. ")
                                return  None        
                verify_data=data_verify(customer_data_list)
                
                        
                if verify_data != None:
                              
                                import datetime
                                current_date=datetime.datetime.now()
                                current_Time=current_date.strftime(f"%d-%m-%Y")
                                verify_data=list(verify_data)
                                verify_data.append(current_Time)
                                verify_data=tuple(verify_data)
                                
                                try:
                                                cursor=db.cursor()
                                                cursor.execute(f"insert into employees(Name , Skill,Address,Phone,Hire_date)  values{verify_data} ")
                                                db.commit()
                                                cursor.close()
                                                refresh()
                                                msg.showinfo("Form Submitted Successfully","Congratulations! Your registration form has been submitted successfully. ")
                                                st_name_ent.delete(0, "end")
                                                st_prof_ent.delete(0, "end")
                                                phone_ent.delete(0, "end")
                                                address_ent.delete(0, "end") 
                                except (mysql.connector.errors.OperationalError,
                                        mysql.connector.errors.ProgrammingError,
                                        mysql.connector.errors.IntegrityError,
                                        mysql.connector.errors.ConnectionTimeoutError,
                                        ):
                                          msg.showerror("Database Not Found","Please! Check the connection of database...........")
                                       


        def B_delete():
                selected=Customer_table.selection()
                if selected:
                        qti=msg.askquestion("Delete!",f"Do you want to delete this employee data?")
                        if qti=="yes":
                        
                                for item in selected:
                                     values= Customer_table.item(item,"values")
                                val=list(values)
                                selected_cnic=val[0]
                                try:
                                        
                                        cursor=db.cursor()
                                        quarry="DELETE FROM employees where Id=%s"
                                        cursor.execute(quarry,(selected_cnic,))                                                                                                                       
                                
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                 mysql.connector.errors.ProgrammingError,
                                                 mysql.connector.errors.IntegrityError,
                                                 mysql.connector.errors.ConnectionTimeoutError,
                                                 ):
                                               msg.showerror("Database Not Found","Please! Check the connection of database...........")
    
                                
                                msg.showinfo("Registration canceled Successfully!",f"Registration Detail\n\n1.Order Id {values[0]}\n2.Order Name: {values[1]}\n3.Client Name: {values[2]}")
                                for item2 in selected:
                                   Customer_table.delete(item2)
                else:
                                 msg.showinfo("Not Selected!",f"Please! Select employee data for deleting that employee")
        


        delete_btn=cu.CTkButton(Form,text="Delete❌",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#8D0707",command=B_delete)
        delete_btn.grid(row=5,column=3,pady=30,ipadx=28,columnspan=40,padx=10)

        register_btn=cu.CTkButton(Form,text="Register!",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#1F6AA5",command=booking)
        register_btn.grid(row=5,column=0,padx=10,ipadx=20,pady=30,columnspan=3)

         














def home(big_frame):
                # Making table area=================================================
        tb_frame=cu.CTkFrame(big_frame,corner_radius=20,height=250,width=1500) # pyright: ignore[reportUndefinedVariable]
        tb_frame.grid(row=1,column=1)
        table_frame = tk.Frame(tb_frame, bg="#000000", bd=2, relief="ridge")
        table_frame.place(x=5,y=10,width=1350,height=220,)
        scroll_x=tk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=tk.Scrollbar(table_frame,orient="vertical")
        col_names=("Order Id","Order Name","Client Name","Order description","Price","Assigned Id")
        col_heading_names=("Order Id","Order Name","Client Name","Order description","Price","Employee Id")
        Customer_table=ttk.Treeview(table_frame,columns=(col_names),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="left",fill="y")
        scroll_x.config(command=Customer_table.xview)
        scroll_y.config(command=Customer_table.yview)
        for x,y in zip(col_names,col_heading_names):
              Customer_table.heading(x,text=y)
        Customer_table['show']='headings'

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                background="#313030",  
                fieldbackground="#363636", 
                foreground="#ffffff",   
                ) 
        style.configure("Treeview.Heading",
                background="#4a4a4a",
                #foreground="#FFFFFF",
                )
        style.configure("Treeview.Heading", font=("Times New Roman", 15, "bold"))
        style.configure("Treeview", font=("Times New Roman", 15),rowheight=25)
        Customer_table.pack(fill="both",expand=1)
        # Data insert area=================================
        try:
                cursor=db.cursor()
                quarry="SELECT * FROM orders"
                cursor.execute(quarry)
                data=cursor.fetchall()
                for row in data:
                        Customer_table.insert("","end",values=row)
                db.commit()
                cursor.close() 
        except (mysql.connector.errors.OperationalError,
        mysql.connector.errors.ProgrammingError,
        mysql.connector.errors.IntegrityError,
        mysql.connector.errors.ConnectionTimeoutError,
        ):
                        msg.showerror("Database Not Found","Please! Check the connection of database...........")




        def refresh():
                for rows in Customer_table.get_children():
                        Customer_table.delete(rows)
                
                try:
                        cursor=db.cursor()
                        quarry="SELECT * FROM orders"
                        cursor.execute(quarry)
                        data=cursor.fetchall()
                        for row in data:
                                Customer_table.insert("","end",values=row)
                        db.commit()
                        cursor.close() 
                except (mysql.connector.errors.OperationalError,
                mysql.connector.errors.ProgrammingError,
                mysql.connector.errors.IntegrityError,
                mysql.connector.errors.ConnectionTimeoutError,
                ):
                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
        


        def remove():
                for rows in Customer_table.get_children():
                        Customer_table.delete(rows)
        def search():
                select_by=search_combo.get()
                user_search=search_ent.get().title().strip()
                
                
                match select_by:
                        case "Search By":
                  
                                msg.showinfo("Select Search By","Please! Select option (Order Name, Client Name,Order Id, Employee Id) to find the customer information you are looking for.")
                
                        case "Employee Id":
                                        # home_table_data=[Customer_table1.item(row,"values") for row in Customer_table1.get_children()]
                                        # print(home_table_data)
                                try:
                                        remove()
                                        cursor=db.cursor()
                                        quarry="select * from orders  where assign_id=%s"
                                        cursor.execute(quarry,(user_search,))                                                                                                                       
                                        data=cursor.fetchall()
                                        for row in data:
                                                Customer_table.insert("","end",values=row)
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                        mysql.connector.errors.ProgrammingError,
                                                        mysql.connector.errors.IntegrityError,
                                                        mysql.connector.errors.ConnectionTimeoutError,
                                                        ):
                                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
                        case "Order Id":
                                try:
                                        remove()
                                        cursor=db.cursor()
                                        quarry="select * from orders  where Id=%s"
                                        cursor.execute(quarry,(user_search,))                                                                                                                       
                                        data=cursor.fetchall()
                                        for row in data:
                                                Customer_table.insert("","end",values=row)
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                        mysql.connector.errors.ProgrammingError,
                                                        mysql.connector.errors.IntegrityError,
                                                        mysql.connector.errors.ConnectionTimeoutError,
                                                        ):
                                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
                        case "Order Name":
                                try:
                                        remove()
                                        cursor=db.cursor()
                                        quarry="select * from orders  where order_Name=%s"
                                        cursor.execute(quarry,(user_search,))                                                                                                                       
                                        data=cursor.fetchall()
                                        for row in data:
                                                Customer_table.insert("","end",values=row)
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                        mysql.connector.errors.ProgrammingError,
                                                        mysql.connector.errors.IntegrityError,
                                                        mysql.connector.errors.ConnectionTimeoutError,
                                                        ):
                                                msg.showerror("Database Not Found","Please! Check the connection of database...........")

                        case "Client Name":
                                try:
                                        remove()
                                        cursor=db.cursor()
                                        quarry="select * from orders  where client_Name=%s"
                                        cursor.execute(quarry,(user_search,))                                                                                                                       
                                        data=cursor.fetchall()
                                        for row in data:
                                                Customer_table.insert("","end",values=row)
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                        mysql.connector.errors.ProgrammingError,
                                                        mysql.connector.errors.IntegrityError,
                                                        mysql.connector.errors.ConnectionTimeoutError,
                                                        ):
                                                msg.showerror("Database Not Found","Please! Check the connection of database...........")







        def B_delete():
                selected=Customer_table.selection()
                if selected:
                        qti=msg.askquestion("Delete!",f"Do you want to delete assigned order of this employee.")
                        if qti=="yes":
                        
                                for item in selected:
                                     values= Customer_table.item(item,"values")
                                val=list(values)
                                selected_cnic=val[0]
                                try:
                                        
                                        cursor=db.cursor()
                                        quarry="DELETE FROM orders WHERE Id=%s"
                                        cursor.execute(quarry,(selected_cnic,))                                                                                                                       
                                
                                        db.commit()
                                        cursor.close() 
                                except (mysql.connector.errors.OperationalError,
                                                 mysql.connector.errors.ProgrammingError,
                                                 mysql.connector.errors.IntegrityError,
                                                 mysql.connector.errors.ConnectionTimeoutError,
                                                 ):
                                               msg.showerror("Database Not Found","Please! Check the connection of database...........")
    
                                
                                msg.showinfo("Registration canceled Successfully!",f"Registration Detail\n\n1.Order Id {values[0]}\n2.Order Name: {values[1]}\n3.Client Name: {values[2]}")
                                for item2 in selected:
                                   Customer_table.delete(item2)
                else:
                                 msg.showinfo("Not Selected!",f"Please! Select Order data for deleting order!")
        
           
        def excel_report():


                try:
                        cursor=db.cursor()
                        quarry="SELECT * FROM orders"
                        cursor.execute(quarry)
                        data=cursor.fetchall()
                        whole_data=[]
                        for row in data:
                                whole_data.append(list(row))
                                
                        db.commit()
                        cursor.close() 
                except (mysql.connector.errors.OperationalError,
                mysql.connector.errors.ProgrammingError,
                mysql.connector.errors.IntegrityError,
                mysql.connector.errors.ConnectionTimeoutError,
                ):
                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
                heading_names=["Order Id","Order Name","Client Name","Order description","Price","Employee Id"]
                whole_data_pure=[]
                for n in range(len(whole_data[0])):
                            l=[]
                            for row in whole_data:
                                    l.append(row[n])
                            whole_data_pure.append(l)
                data_ready={}
                for heading, row in zip(heading_names,whole_data_pure):
                           data_ready[heading]=row
                
                df=pd.DataFrame(data_ready)
                df.to_excel('Generated/Orders.xlsx', index=False) 
                msg.showinfo("Data Exported Successfully",f"Please! Check this location 'Generated/Orders.xlsx' for your data.")
        
        def csv_report():


                try:
                        cursor=db.cursor()
                        quarry="SELECT * FROM orders"
                        cursor.execute(quarry)
                        data=cursor.fetchall()
                        whole_data=[]
                        for row in data:
                                whole_data.append(list(row))
                                
                        db.commit()
                        cursor.close() 
                except (mysql.connector.errors.OperationalError,
                mysql.connector.errors.ProgrammingError,
                mysql.connector.errors.IntegrityError,
                mysql.connector.errors.ConnectionTimeoutError,
                ):
                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
                heading_names=["Order Id","Order Name","Client Name","Order description","Price","Employee Id"]
                whole_data_pure=[]
                for n in range(len(whole_data[0])):
                            l=[]
                            for row in whole_data:
                                    l.append(row[n])
                            whole_data_pure.append(l)
                data_ready={}
                for heading, row in zip(heading_names,whole_data_pure):
                           data_ready[heading]=row
                
                df=pd.DataFrame(data_ready)
                df.to_csv('Generated/Orders.csv', index=False) 
                msg.showinfo("Data Exported Successfully",f"Please! Check this location 'Generated/Orders.csv' for your data.")
                        
        










        op_big_frame=cu.CTkFrame(big_frame,corner_radius=20)
        op_big_frame.grid(row=10,column=1,pady=20)

        op_frame=cu.CTkFrame(op_big_frame,corner_radius=20)
        op_frame.grid(row=0,column=0,pady=20,padx=10)


                                                              

        # Search options=============
        search_lab=cu.CTkLabel(op_frame,text="Manage your orders",font=("Arial Rounded MT Bold",22,"bold"))
        search_lab.grid(row=0,column=0,pady=10,columnspan=2)
        search_ent=cu.CTkEntry(op_frame,placeholder_text="Search!🔍",width=250,font=("Cambria (Headings)", 20),corner_radius=30)
        search_ent.grid(row=1,column=0,pady=10,padx=10)
        search_combo=cu.CTkOptionMenu(op_frame,values=["Search By","Employee Id","Order Id","Order Name","Client Name"],width=200,dropdown_hover_color="#1F6AA5",fg_color="#4B4948",button_color="#4B4948",font=("Cambria (Headings)", 20))
        search_combo.grid(row=1,column=1,padx=20,pady=10,)
        search_btn=cu.CTkButton(op_frame,text="Search🔎",corner_radius=100,font=("Cambria (Headings)",20),command=search)
        search_btn.grid(row=2,column=0,pady=10,ipadx=35)
        
        delete_btn=cu.CTkButton(op_frame,text="Delete❌",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#8D0707",command=B_delete)
        delete_btn.grid(row=2,column=1,pady=10,ipadx=28)
        refresh_btn=cu.CTkButton(op_frame,text="Refresh🔃",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#106100",command=refresh)
        refresh_btn.grid(row=3,column=0,pady=10,ipadx=35)
        update_btn=cu.CTkButton(op_frame,text="Update📅",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#410A88",)
        update_btn.grid(row=3,column=1,pady=10,ipadx=30)
      

        op_frame2=cu.CTkFrame(op_big_frame,corner_radius=20)
        op_frame2.grid(row=0,column=1,pady=20,padx=120)






        search_lab=cu.CTkLabel(op_frame2,text="Export the data of orders",font=("Arial Rounded MT Bold",22,"bold"))
        search_lab.grid(row=0,column=0,pady=10,columnspan=2)
        logo_excel_image=cu.CTkImage(dark_image=Image.open("images/logo_excel.png"),light_image=Image.open("images/logo_excel.png"),size=(80,80))
        logo_excel_label=cu.CTkLabel(op_frame2,text="",image=logo_excel_image)
        logo_excel_label.place(x=0,y=40)

        logo_csv_image=cu.CTkImage(dark_image=Image.open("images/logo_csv.png"),light_image=Image.open("images/logo_csv.png"),size=(80,80))
        logo_csv_label=cu.CTkLabel(op_frame2,text="",image=logo_csv_image)
        logo_csv_label.place(x=0,y=130)




        

        excel_btn=cu.CTkButton(op_frame2,text="Excel",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#106100",command=excel_report)
        excel_btn.grid(row=2,column=1,ipadx=35,padx=100,pady=30)
        csv_btn=cu.CTkButton(op_frame2,text="CSV",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#106100",command=csv_report)
        csv_btn.grid(row=3,column=1,ipadx=35,padx=100,pady=30)



def Orders(big_frame):
        
        # Making table area=================================================
        tb_frame=cu.CTkFrame(big_frame,corner_radius=20,height=250,width=1500) # pyright: ignore[reportUndefinedVariable]
        tb_frame.grid(row=0,column=0)
        table_frame = tk.Frame(tb_frame, bg="#000000", bd=2, relief="ridge")
        table_frame.place(x=5,y=10,width=1350,height=220,)
        scroll_x=tk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=tk.Scrollbar(table_frame,orient="vertical")
        col_names=("id","name","skill","phone","address","hiring_date")
        col_heading_names=("Employee ID","Name","Profession","Phone No","Address","Hiring Date")
        Customer_table=ttk.Treeview(table_frame,columns=(col_names),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="left",fill="y")
        scroll_x.config(command=Customer_table.xview)
        scroll_y.config(command=Customer_table.yview)
        for x,y in zip(col_names,col_heading_names):
              Customer_table.heading(x,text=y)
        Customer_table['show']='headings'

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                background="#313030",  
                fieldbackground="#363636", 
                foreground="#ffffff",   
                ) 
        style.configure("Treeview.Heading",
                background="#4a4a4a",
                #foreground="#FFFFFF",
                )
        style.configure("Treeview.Heading", font=("Times New Roman", 15, "bold"))
        style.configure("Treeview", font=("Times New Roman", 15),rowheight=25)
        Customer_table.pack(fill="both",expand=1)
        # Data insert area=================================
        try:
                cursor=db.cursor()
                quarry="SELECT * FROM employees "
                cursor.execute(quarry)
                data=cursor.fetchall()
                for row in data:
                        Customer_table.insert("","end",values=row)
                db.commit()
                cursor.close() 
        except (mysql.connector.errors.OperationalError,
        mysql.connector.errors.ProgrammingError,
        mysql.connector.errors.IntegrityError,
        mysql.connector.errors.ConnectionTimeoutError,
        ):
                        msg.showerror("Database Not Found","Please! Check the connection of database...........")


        Form =cu.CTkFrame(big_frame,corner_radius=20 )
        Form.grid(row=1,column=0,padx=10,pady=10)

        cu.CTkLabel(Form, text="Assign Your Orders", font=("Arial Rounded MT Bold",50),
           ).grid(row=0, column=0, columnspan=10, pady=10)
        order_Name_lab=cu.CTkLabel(Form,text="Order Name:",font=("Arial Rounded MT Bold",22,"bold")).grid(row=1,column=0)
        order_des_lab=cu.CTkLabel(Form,text="Order description:",anchor="ne",font=("Arial Rounded MT Bold",22,"bold")).grid(row=1,column=3)
        client_name_lab=cu.CTkLabel(Form,text=" Client Name:",font=("Arial Rounded MT Bold",22,"bold")).grid(row=2,column=0)
        price_lab=cu.CTkLabel(Form,text="Price:",anchor="ne",font=("Arial Rounded MT Bold",22,"bold")).grid(row=2,column=3)

        order_name_ent=cu.CTkEntry(Form,placeholder_text="Edit Video",width=250,font=("Cambria (Headings)", 20))
        order_name_ent.grid(row=1,column=1,padx=15,pady=5)
        order_des_ent=cu.CTkEntry(Form,placeholder_text="Edit one scene for my new movie",width=250,font=("Cambria (Headings)", 20))
        order_des_ent.grid(row=1,column=4,padx=10,pady=5)
        price_ent=cu.CTkEntry(Form,placeholder_text="5000$",width=250,font=("Cambria (Headings)", 20))
        price_ent.grid(row=2,column=4,pady=5,padx=10)
        client_name_ent=cu.CTkEntry(Form,placeholder_text="Jhon doe",width=250,font=("Cambria (Headings)", 20))
        client_name_ent.grid(row=2,column=1,pady=5,padx=10)


        def booking():
                customer_data_list=[order_name_ent.get().title().strip(),client_name_ent.get().title().strip(),order_des_ent.get().title().strip(),price_ent.get().title().strip()]
                
                def data_verify(data_list):
                        data_list=list(data_list)
                        for element in data_list:
                                if element=="":
                                        msg.showerror("Missing Fields Error","Please! Fill out all required fields.\nThis will help us process your request.\nYou have some missing information.\nPlease! Review and complete the form. ")
                                        return  None
                                
                                        
                       
        
                        if str(data_list[-1]).isdigit():
                                
                                return data_list
                                
                        else:
                                msg.showerror("Data Validation Error","Please! Fill out all required fields with correct data.\nThis will help us process your request.\nYou have entered some wrong information.\nPlease! Review and complete the form with correct data. ")
                                return  None        
                verify_data=data_verify(customer_data_list)
                
                
                        
                if verify_data != None:
                        selected=Customer_table.selection()
                        if selected:
                                    qti=msg.askquestion("Processing.....",f"Do you want to assign order to this employee ?")
                                    if qti=="yes":
                                        for item in selected:
                                                        values= Customer_table.item(item,"values")
                                        val=list(values)
                                        verify_data=list(verify_data)
                                        verify_data.append(val[0])
                                        verify_data=tuple(verify_data)
                                        try:
                                                cursor=db.cursor()
                                                cursor.execute(f"insert into orders(order_name,client_name,order_des,price,assign_id)  values{verify_data} ")
                                                db.commit()
                                                cursor.close()
                                                
                                                msg.showinfo("Form Submitted Successfully","Congratulations! Your order has been assigned successfully. ")
                                                order_name_ent.delete(0, "end")
                                                order_des_ent.delete(0, "end")
                                                price_ent.delete(0, "end")
                                                client_name_ent.delete(0, "end")

                                                
                                        except (mysql.connector.errors.OperationalError,
                                                mysql.connector.errors.ProgrammingError,
                                                mysql.connector.errors.IntegrityError,
                                                mysql.connector.errors.ConnectionTimeoutError,
                                                ):
                                                msg.showerror("Database Not Found","Please! Check the connection of database...........")
                                        

                                        
                                        
                        else:
                                 msg.showinfo("Not Selected!",f"Please! Select Employee data for assigning order!")
        
                              
                              
                               
                
                                
                

        register_btn=cu.CTkButton(Form,text="Assign Order!",corner_radius=100,font=("Cambria (Headings)",20),fg_color="#1F6AA5",command=booking)
        register_btn.grid(row=5,column=0,padx=10,ipadx=20,columnspan=10,pady=30)

         
 





































































































































































































































































































































































































