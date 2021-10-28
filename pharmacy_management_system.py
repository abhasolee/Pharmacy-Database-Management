from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

# Configuring main window
root = Tk()
root.title('Pharmacy Management System')
root.geometry('800x750')
root.iconbitmap('images/pharmacyicon.icns')

# Defining the admin name
global admin_name
admin_name="Abhas Oli"

# Create or connect a database
conn = sqlite3.connect('pharmacy.db')

# Create a cursor
c = conn.cursor()

# Create table
try:
    c.execute("""CREATE TABLE employees(
            first_name text,
            last_name text,
            email text,
            password text,
            gender text,
            experience text,
            education text)""")

except sqlite3.OperationalError:
    pass


# Commit changes to database
conn.commit()

# Close the connection
conn.close()

# Function to update records in database
def update_record_db():

    if update_password_box==update_confirm_password_box:

        # Create or connect a database
        conn = sqlite3.connect('pharmacy.db')

        # Create a cursor
        c = conn.cursor()

        # Updating records
        c.execute('''UPDATE employees SET
            first_name=:fname,
            last_name=:lname,
            email=:username,
            password=:password,
            gender=:gender,
            experience=:experience,
            education=:education
            WHERE oid=:oid''',
            {
            'fname':update_fname_box.get(),
            'lname':update_lname_box.get(),
            'username':update_username_box.get(),
            'password':update_password_box.get(),
            'gender':update_gender.get(),
            'experience':update_experience.get(),
            'education':update_education.get(),
            'oid':select_box.get()
            })

        # Commit the changes to databse
        conn.commit()

        # Close the connection
        conn.close()

        response=messagebox.showinfo('Updated','Your Record is Updated')
        if response=='ok':
            update_records_window.destroy()

    else:
        # Delete the contents of the box
        update_confirm_password_box.delete(0,END)

        # Display error message in the boxe
        update_confirm_password_box.config(bg="red")
        update_confirm_password_box.insert(0,'Password Not Matched')



# Function to view records of employees
def view_records():
    # Create a new window
    view_records_window = Toplevel()
    view_records_window.title("View Records of Employess")
    view_records_window.geometry('600x400')

    # Creating a frame for the title
    title_frame = Frame(view_records_window, padx=45, pady=10)
    title_frame.grid(row=0, column=0, pady=10)

    # Creating the title label
    title_label = Label(title_frame, text="NAGATO'S  PHARMACY",
                        font=('Anurati', 30), fg='#107896')
    title_label.config(anchor=CENTER)
    title_label.pack()

    # Create or connect a database
    conn = sqlite3.connect('pharmacy.db')

    # Create a cursor
    c = conn.cursor()

    # Fetching all the records
    c.execute("SELECT oid,first_name,last_name,email,gender,experience,education FROM employees")
    records = c.fetchall()

    # Create a body frame
    body_frame = Frame(view_records_window, width=450, height=300)
    body_frame.grid(row=2, column=0, pady=10)

    # Displaying the title for the body
    title_list=['S.N.','First Name','Last Name','Username','Gender','Experience','Education']
    for k,item in enumerate(title_list):
        body_title_label=Label(body_frame,text=item,font=('Milkshake',18,'underline'),fg="#6ed3cf")
        body_title_label.grid(row=0,column=k)

    # Displaying the records on the screen
    for i, record in enumerate(records,1):
        for j, data in enumerate(record):
            display_label = Label(body_frame, text=data)
            display_label.grid(row=i, column=j)

    # Create exit button
    exit_button=Button(view_records_window,text="Exit",font=(
            'Anna', 20), fg="#51d0de",width=8, command=view_records_window.destroy)
    exit_button.grid(row=3,column=0)


# Function to display update records window
def update_records():
    global update_records_window
    update_records_window=Toplevel()
    update_records_window.title('Update Records')
    update_records_window.geometry('500x500')

    # Create or connect a database
    conn = sqlite3.connect('pharmacy.db')

    # Create a cursor
    c = conn.cursor()

    # Fetching the data and storing them
    c.execute("SELECT * FROM employees WHERE oid=:oid",
        {
        "oid":select_box.get()
        })
    records=c.fetchall()
    for record in records:
        fname=record[0]
        lname=record[1]
        username=record[2]
        password=record[3]
        gender=record[4]
        experience=record[5]
        education=record[6]

    # Commit changes to the database
    conn.commit()

    # Close the connection
    conn.close()

    # Creating a frame for the title
    title_frame = Frame(update_records_window, padx=45, pady=10)
    title_frame.grid(row=0, column=0, pady=10)

    # Creating the title label
    title_label = Label(title_frame, text="NAGATO'S  PHARMACY",
                        font=('Anurati', 30), fg='#107896')
    title_label.config(anchor=CENTER)
    title_label.pack()

    # Create title for this particular window
    update_title_label=Label(update_records_window,text="Update Record",font=(
            'Adrenaline', 25, 'bold', 'underline'), fg="#5cbdb9")
    update_title_label.grid(row=1,column=0)

    # Create frame for the body
    body_frame = Frame(update_records_window, width=450, height=400)
    body_frame.grid(row=2, column=0)

    # Create labels
    update_fname_label = Label(body_frame, text="First Name")
    update_fname_label.grid(row=0, column=0)

    update_lname_label = Label(body_frame, text="Last Name")
    update_lname_label.grid(row=1, column=0)

    update_username_label = Label(body_frame, text="UserName")
    update_username_label.grid(row=2, column=0)

    update_password_label = Label(body_frame, text="Password")
    update_password_label.grid(row=3, column=0)

    update_confirm_password_label = Label(body_frame, text="Confirm Password")
    update_confirm_password_label.grid(row=4, column=0)

    update_gender_label = Label(body_frame, text="Gender")
    update_gender_label.grid(row=5, column=0)

    update_experience_label = Label(body_frame, text="Experience")
    update_experience_label.grid(row=7, column=0)

    update_education_label = Label(body_frame, text="Education")
    update_education_label.grid(row=8, column=0)

    # Create entry boxes
    global update_fname_box
    update_fname_box = Entry(body_frame, width=25)
    update_fname_box.insert(0,fname)
    update_fname_box.grid(row=0, column=1)

    global update_lname_box
    update_lname_box = Entry(body_frame, width=25)
    update_lname_box.insert(0,lname)
    update_lname_box.grid(row=1, column=1)

    global update_username_box
    update_username_box = Entry(body_frame, width=25)
    update_username_box.insert(0,username)
    update_username_box.grid(row=2, column=1)

    global update_password_box
    update_password_box = Entry(body_frame, width=25)
    update_password_box.insert(0,password)
    update_password_box.grid(row=3, column=1)

    global update_confirm_password_box
    update_confirm_password_box = Entry(body_frame, width=25)
    update_confirm_password_box.insert(0,password)
    update_confirm_password_box.grid(row=4, column=1)

    # Create radio buttons
    global update_gender
    update_gender = StringVar()
    update_gender.set(gender)
    male = Radiobutton(body_frame, text="Male",
                       value="Male", variable=update_gender)
    male.grid(row=5, column=1, sticky=W)
    female = Radiobutton(body_frame, text="Female",
                         value="Female", variable=update_gender)
    female.grid(row=6, column=1, sticky=W)

    # Create dropdown menus
    global update_experience
    update_experience = StringVar()
    experience_options = ['None', '1 Year', '2 Years', 'More than 2 years']
    global update_education
    update_education = StringVar()
    education_options = ['High School', 'Undergraduate',
                         'Graduate', 'Post Graduate', 'Doctoral']

    update_experience.set(experience)
    update_education.set(education)

    experience_menu = OptionMenu(body_frame, update_experience, *experience_options)
    experience_menu.grid(row=7, column=1, sticky=W)

    education_menu = OptionMenu(body_frame, update_education, *education_options)
    education_menu.grid(row=8, column=1, sticky=W)

    # Create buttons
    update_button = Button(body_frame, text="Update Account", font=(
        'Anna', 20), fg="#51d0de", width=15,command=update_record_db)
    update_button.grid(row=9, column=0, pady=20)

    exit_button = Button(body_frame, text="Exit", font=(
        'Anna', 20), fg="#51d0de",width=6,
        command=update_records_window.destroy)
    exit_button.grid(row=9, column=1, pady=20)


# Function to select records of employees to update
def update_records_selection():
    if admin_name==name:
        # Create selection frame
        selection_frame=Frame(logged_in_window,width=400,height=200)
        selection_frame.grid(row=3,column=0)

        # Create label, entry box and button to select record
        select_oid_label=Label(selection_frame,text="Select oid")
        select_oid_label.grid(row=0,column=0)

        global select_box
        select_box=Entry(selection_frame,width=25)
        select_box.grid(row=0,column=1,sticky=W)

        ok_button=Button(selection_frame,text="Ok",font=(
            'Anna', 20), fg="#51d0de",width=8,command=update_records)
        ok_button.grid(row=1,column=0,columnspan=2,pady=10)

    else:
        not_admin_label=Label(logged_in_window,text="Sorry, You're not the admin",font=(
            'Noteworthy', 20), fg="#5cbdb9")
        not_admin_label.grid(row=3,column=0)


# Function to delete records
def delete_records():
    # Connect to database
    conn = sqlite3.connect('pharmacy.db')

    # Create a cursor
    c = conn.cursor()

    #Deleteing records
    c.execute("DELETE from employees WHERE oid=:oid",
        {
        'oid':select_box.get()
        })

    # Commit changes to database
    conn.commit()

    # Close the connection
    conn.close()

    # Showing a message
    messagebox.showinfo('Delete Records','Your Record is successfully deleted')


# Function to delete records of employees
def delete_records_selection():
    if admin_name==name:
        # Create selection frame
        selection_frame=Frame(logged_in_window,width=400,height=200)
        selection_frame.grid(row=3,column=0)

        # Create label, entry box and button to select record
        select_oid_label=Label(selection_frame,text="Select oid")
        select_oid_label.grid(row=0,column=0)

        global select_box
        select_box=Entry(selection_frame,width=25)
        select_box.grid(row=0,column=1,sticky=W)

        ok_button=Button(selection_frame,text="Ok",font=(
            'Anna', 20), fg="#51d0de",width=8,command=delete_records)
        ok_button.grid(row=1,column=0,columnspan=2,pady=10)

    else:
        not_admin_label=Label(logged_in_window,text="Sorry, You're not the admin",font=(
            'Noteworthy', 20), fg="#5cbdb9")
        not_admin_label.grid(row=3,column=0)


# Create function for window after logged in
def login():
    username = login_username_box.get()
    password = login_password_box.get()

    # Connect to database
    conn = sqlite3.connect('pharmacy.db')

    # Create a cursor
    c = conn.cursor()

    c.execute("SELECT * FROM employees WHERE email=:username AND password=:password",
              {
                  'username': username,
                  'password': password
              })
    record = c.fetchall()

    conn.commit()

    # Conditions for if the record is present in the table or not
    if record == []:
        # Deleteing the contents of the entry boxes
        login_username_box.delete(0, END)
        login_password_box.delete(0, END)

        # Inserting an error message with a red background
        login_username_box.insert(0, 'Error Try Again')
        login_password_box.insert(0, 'Error Try Again')
        login_username_box.config(bg="red")
        login_password_box.config(bg="red")

    else:
        global logged_in_window
        logged_in_window = Toplevel()
        logged_in_window.title("Welcome to Nagato's Pharmacy")
        logged_in_window.geometry('500x500')

        # Creating a frame for the title
        title_frame = Frame(logged_in_window, padx=45, pady=10)
        title_frame.grid(row=0, column=0, pady=10)

        # Creating the title label
        title_label = Label(title_frame, text="NAGATO'S  PHARMACY",
                            font=('Anurati', 30), fg='#107896')
        title_label.config(anchor=CENTER)
        title_label.pack()

        # Concactenate the first and last name of the record
        global name
        name = record[0][0] + " " + record[0][1]

        # Create welcome label
        welcome_label = Label(logged_in_window, text="Welcome! " + name, font=(
            'Adrenaline', 25, 'bold', 'underline'), fg="#5cbdb9")
        welcome_label.grid(row=1, column=0)

        # Create a body frame
        body_frame = Frame(logged_in_window, width=450, height=300)
        body_frame.grid(row=2, column=0, pady=10)

        # Create several buttons for options
        view_record_button = Button(body_frame, text="View Employess Record", font=(
            'Anna', 20), fg="#51d0de", width=20,command=view_records)
        view_record_button.pack(pady=10)

        update_record_button = Button(body_frame, text="Update Employess Record", font=(
            'Anna', 20), fg="#51d0de",width=20 ,command=update_records_selection)
        update_record_button.pack(pady=10)

        delete_record_button = Button(body_frame, text="Delete Employess Record", font=(
            'Anna', 20), fg="#51d0de", width=20,command=delete_records_selection)
        delete_record_button.pack(pady=10)

        exit_button = Button(body_frame, text="Exit", font=(
            'Anna', 20), fg="#51d0de", width=8,command=logged_in_window.destroy)
        exit_button.pack(pady=10)

        # Creating error label
        error_label = Label(body_frame)
        error_label.pack()

    conn.close()


# Create function to create an account
def create_account():
    # Connect to database
    conn = sqlite3.connect('pharmacy.db')

    # Create a cursor
    c = conn.cursor()

    # Check for password
    if password_box.get() == confirm_password_box.get():
        fname = fname_box.get()
        lname = lname_box.get()
        username = username_box.get()
        password = password_box.get()
        gender_db = gender.get()
        experience_db = experience.get()
        education_db = education.get()

        # Adding records to the table
        c.execute("INSERT INTO employees VALUES(:fname,:lname,:username,:password,:gender,:experience,:education)",
                  {
                      'fname': fname,
                      'lname': lname,
                      'username': username,
                      'password': password,
                      'gender': gender_db,
                      'experience': experience_db,
                      'education': education_db
                  }
                  )

        # Commit the changes
        conn.commit()

        # Showing an message saying you have created an account
        response = messagebox.showinfo(
            "Account Creation", "Your account is created")
        if response == 'ok':
            sign_in_window.destroy()

    else:
        # Deleting the contents of box and displaying text in red background
        confirm_password_box.delete(0, END)
        confirm_password_box.config(bg='red')
        confirm_password_box.insert(0, 'Password not matched')

    # Close the database connection
    conn.close()


# Create function for sign in window
def sign_in():
    # Create new window
    global sign_in_window
    sign_in_window = Toplevel()
    sign_in_window.title('Sign In')
    sign_in_window.geometry('500x500')

    # Creating a frame for the title
    title_frame = Frame(sign_in_window, padx=45, pady=10)
    title_frame.grid(row=0, column=0, pady=10)

    # Creating the title label
    title_label = Label(title_frame, text="NAGATO'S  PHARMACY",
                        font=('Anurati', 30), fg='#107896')
    title_label.config(anchor=CENTER)
    title_label.pack()

    # Creating the title for the window
    title_window = Label(sign_in_window, text="Create Your Account", font=(
        'Coves', 20, 'bold', 'underline'), fg="#5cbdb9")
    title_window.grid(row=1, column=0, pady=10)

    # Create frame for the body
    body_frame = Frame(sign_in_window, width=450, height=400)
    body_frame.grid(row=2, column=0)

    # Create labels
    fname_label = Label(body_frame, text="First Name")
    fname_label.grid(row=0, column=0)

    lname_label = Label(body_frame, text="Last Name")
    lname_label.grid(row=1, column=0)

    username_label = Label(body_frame, text="UserName")
    username_label.grid(row=2, column=0)

    password_label = Label(body_frame, text="Password")
    password_label.grid(row=3, column=0)

    confirm_password_label = Label(body_frame, text="Confirm Password")
    confirm_password_label.grid(row=4, column=0)

    gender_label = Label(body_frame, text="Gender")
    gender_label.grid(row=5, column=0)

    experience_label = Label(body_frame, text="Experience")
    experience_label.grid(row=7, column=0)

    education_label = Label(body_frame, text="Education")
    education_label.grid(row=8, column=0)

    # Create entry boxes
    global fname_box
    fname_box = Entry(body_frame, width=25)
    fname_box.grid(row=0, column=1)

    global lname_box
    lname_box = Entry(body_frame, width=25)
    lname_box.grid(row=1, column=1)

    global username_box
    username_box = Entry(body_frame, width=25)
    username_box.grid(row=2, column=1)

    global password_box
    password_box = Entry(body_frame, width=25)
    password_box.grid(row=3, column=1)

    global confirm_password_box
    confirm_password_box = Entry(body_frame, width=25)
    confirm_password_box.grid(row=4, column=1)

    # Create radio button
    global gender
    gender = StringVar()
    gender.set("Male")
    male = Radiobutton(body_frame, text="Male",
                       value="Male", variable=gender)
    male.grid(row=5, column=1, sticky=W)
    female = Radiobutton(body_frame, text="Female",
                         value="Female", variable=gender)
    female.grid(row=6, column=1, sticky=W)

    # Create dropdown menus
    global experience
    experience = StringVar()
    experience_options = ['None', '1 Year', '2 Years', 'More than 2 years']
    global education
    education = StringVar()
    education_options = ['High School', 'Undergraduate',
                         'Graduate', 'Post Graduate', 'Doctoral']

    experience.set(experience_options[0])
    education.set(education_options[0])

    experience_menu = OptionMenu(body_frame, experience, *experience_options)
    experience_menu.grid(row=7, column=1, sticky=W)

    education_menu = OptionMenu(body_frame, education, *education_options)
    education_menu.grid(row=8, column=1, sticky=W)

    # Create buttons
    create_acc_button = Button(body_frame, text="Create Account", font=(
        'Anna', 20), fg="#51d0de",width=15, command=create_account)
    create_acc_button.grid(row=9, column=0, pady=20)

    exit_button = Button(body_frame, text="Exit", font=(
        'Anna', 20), fg="#51d0de",width=8,
        command=sign_in_window.destroy)
    exit_button.grid(row=9, column=1, pady=20)


# Create function for information window
def information(event):
    # Create new window
    info_window = Toplevel()
    info_window.title('Information Window')
    info_window.geometry('550x580')

    # Creating a frame for the title
    title_frame = Frame(info_window, padx=45, pady=10)
    title_frame.grid(row=0, column=0, pady=10)

    # Creating the title label
    title_label = Label(title_frame, text="NAGATO'S  PHARMACY",
                        font=('Anurati', 30), fg='#107896')
    title_label.config(anchor=CENTER)
    title_label.pack()

    # Creating a title for the info frame
    info_title = Label(title_frame, text="About", font=(
        'Coves', 22, 'bold', 'underline'), fg="#5cbdb9")
    info_title.pack()

    # The text
    info = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam lacus elit, posuere ut justo eget, ornare commodo turpis. Nulla scelerisque cursus turpis, sit amet laoreet diam aliquet quis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed in tempus orci, non hendrerit nisi. Fusce in augue interdum, aliquet purus id, venenatis ipsum. Duis tempus id massa eu aliquam. Integer ac dui nec justo rutrum maximus. Aliquam aliquet, est bibendum lobortis ullamcorper, nulla lectus maximus dui, non ultricies ligula arcu vitae libero. Donec fermentum congue ornare. Nam a dictum velit, sed elementum neque. Nam lobortis accumsan maximus. Aliquam erat volutpat.
            Integer eu tortor cursus, consectetur felis et, tempus sapien. Aenean a imperdiet velit. Praesent et sapien velit. Donec blandit bibendum eros, a pellentesque sapien pretium at. Phasellus mollis lectus magna, sed rutrum urna convallis eget. Integer sapien ante, lacinia nec aliquam eu, ullamcorper quis ante. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Maecenas quis tempus lacus, mattis suscipit quam. Fusce ultrices elementum mi sit amet aliquet. Duis sed efficitur diam. In ut dolor auctor, dignissim velit sit amet, tincidunt felis. Ut convallis mauris sit amet varius placerat. Duis sed porta dolor.

            Praesent velit felis, fringilla eget lorem id, euismod rutrum nibh. Aenean cursus quis tortor eu posuere. Etiam sed sem dolor. Phasellus vel velit sit amet mi pretium auctor sed eget elit. Sed a sem aliquam ligula ultrices tempus. Maecenas congue risus imperdiet, pharetra tellus at, elementum magna. Vestibulum aliquet orci dolor, at auctor enim ornare ut. In hac habitasse platea dictumst. Mauris sollicitudin euismod quam et ultricies. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas elementum facilisis dui, quis hendrerit felis mollis in. Nunc venenatis sem facilisis ultricies tempor. Ut sed ipsum sem.

            Donec rhoncus, leo vitae semper pulvinar, turpis enim suscipit enim, vel eleifend ante risus a nisi. Aenean scelerisque ante sit amet massa aliquet vulputate. Nunc at ante quis erat finibus porta id vitae nisl. Sed dapibus enim id mi consectetur dapibus. Donec elementum magna nec est suscipit maximus. Proin in orci volutpat, commodo nisi quis, sollicitudin risus. Morbi gravida risus vel ligula tristique ultricies. Nullam venenatis bibendum sollicitudin. In tristique, dui id finibus rhoncus, leo magna feugiat ex, in lacinia purus mi at velit. Proin venenatis est a nisi tincidunt dictum. Curabitur at fringilla risus. Aenean placerat, massa ut semper ultricies, libero est molestie sapien, nec maximus lectus nisl vitae purus. Donec a massa et ante gravida rutrum.
            Pellentesque lacinia placerat leo. Integer accumsan, massa et posuere posuere, risus est euismod urna, eu convallis velit risus sit amet nisi.

            Sed lacinia luctus viverra. Aenean tincidunt aliquam felis non consequat. Morbi molestie gravida mauris, quis facilisis nisi ornare et. Proin metus nisi, maximus vel porttitor ac, fringilla quis nibh. Donec finibus risus ante, at sodales libero tristique ut. Quisque sodales purus tellus, et mollis metus luctus vitae. Nam porta risus id erat interdum ullamcorper. Pellentesque a sagittis diam. Curabitur libero lectus, molestie vel nisl et, luctus tincidunt lectus. Donec lobortis sodales tortor, eget rhoncus lectus luctus at. Praesent molestie sodales velit, id vulputate lacus pretium eu. Sed posuere ligula magna, quis convallis tellus egestas ac.
            '''

    # Creating the information frame
    info_frame = Frame(info_window, width=400, height=250)
    info_frame.grid(row=1, column=0)

    # Creating a scrollbar for the frame
    s = Scrollbar(info_frame, orient=VERTICAL)
    s.pack(side=RIGHT, fill=Y)

    # Placing the text
    t = Text(info_frame, height=20, width=50, fg="#494D5F",
             yscrollcommand=s.set, font=('Noteworthy', 12))
    t.pack()
    t.insert(END, info)

    # Creating exit button for this window
    exit_button = Button(info_window, text="Exit", font=(
        'Anna', 22), fg="#51d0de",width=10, command=info_window.destroy)
    exit_button.grid(row=2, column=0, sticky=E)


# Create function for help window
def help_window(event):
    # Create new window
    help_window = Toplevel()
    help_window.title('Help')
    help_window.geometry('500x420')

    # Creating a frame for the title
    title_frame = Frame(help_window, padx=45, pady=10)
    title_frame.grid(row=0, column=0, pady=10)

    # Creating the title label
    title_label = Label(title_frame, text="NAGATO'S  PHARMACY",
                        font=('Anurati', 30), fg='#107896')
    title_label.config(anchor=CENTER)
    title_label.pack()

    # Creating a title for the info frame
    info_title = Label(title_frame, text="About This App", font=(
        'Coves', 20, 'bold', 'underline'), fg="#5cbdb9")
    info_title.pack()

    # Create a frame to put the text
    help_frame = Frame(help_window, width=400, height=250, bg="blue")
    help_frame.grid(row=1, column=0)

    # The text
    help_text = '''This is an GUI app named Pharmacy Management System which allows the users to manage data related to a pharmacy. The users can login using their username and password and they can perform tasks such as adding, updating, viewing or deleting the record of employess and medicines.

                                    Developed by:''' + u'\u00A9' + "Abhas Olee"

    # Create a text widget
    t = Text(help_frame, height=6, width=50, fg="#494D5F",
             font=('Marker Felt', 14))
    t.pack()
    t.insert(END, help_text)

    # Creating exit button for this window
    exit_button = Button(help_window, text="Exit", font=(
        'Anna', 20), fg="#51d0de", command=help_window.destroy)
    exit_button.grid(row=2, column=0, sticky=E)



# Creating a frame for the title
title_frame = Frame(root, padx=200, pady=10)
title_frame.grid(row=0, column=0, pady=20)

# Creating the title label
title_label = Label(title_frame, text="NAGATO'S  PHARMACY",
                    font=('Anurati', 30), fg='#107896')
title_label.config(anchor=CENTER)
title_label.pack()

# Adding an image
my_img = Image.open("images/pharmacy.png")
resized = my_img.resize((250, 250), Image.ANTIALIAS)
new_img = ImageTk.PhotoImage(resized)

image_label = Label(root, image=new_img)
image_label.grid(row=1, column=0)

# Creating a frame for the login
login_frame = Frame(root, width=600, height=300, )
login_frame.grid(row=3, column=0, pady=20)

# Create login box title for login box
login_title_label = Label(login_frame, text="Login",
                          font=(
                              'Milkshake', 30, 'bold', 'underline'), fg="#5cbdb9")
login_title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Create entry boxes for the login box
login_username_box = Entry(login_frame, width=25, bd=3)
login_username_box.grid(row=1, column=1, padx=10)

login_password_box = Entry(login_frame, width=25, bd=3)
login_password_box.grid(row=2, column=1, padx=10)

# Create labels for the login box
username_label = Label(login_frame, text="Username", font=('Book Antiqua', 20))
username_label.grid(row=1, column=0)

password_label = Label(login_frame, text="Password", font=('Book Antiqua', 20))
password_label.grid(row=2, column=0)

# Create submit button in login box
login_submit_button = Button(
    login_frame, text="Login", font=(
        'Anna', 20,'bold'), fg="#51d0de", command=login)
login_submit_button.grid(row=3, column=0, columnspan=2, pady=20)

# Create no account label
no_account_label = Label(
    login_frame, text="Don't have an account?", font=(
        'Milkshake', 22, 'bold', 'underline'), fg="#5cbdb9")
no_account_label.grid(row=4, column=0, columnspan=2, pady=10)

# Create new account button
new_account_button = Button(
    login_frame, text="Sign In", font=(
        'Anna', 22,'bold'), fg="#51d0de", command=sign_in)
new_account_button.grid(row=5, column=0, columnspan=2)

# Creating menus
my_menu = Menu(root)
root.config(menu=my_menu)

about_menu = Menu(my_menu)
my_menu.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Information    "+u'\u2318'+' i', command=information)
about_menu.add_command(label="Help                F1", command=help_window)
about_menu.add_separator()
about_menu.add_command(label="Quit", command=root.quit)

# Binding keyboard events
root.bind("<F1>",help_window)
root.bind("<Command-Key-i>",information)

root.mainloop()
