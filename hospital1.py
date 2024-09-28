from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        # Variables
        self.nameoftablets = StringVar()
        self.ref = StringVar()
        self.dose = StringVar()
        self.nooftablets = StringVar()
        self.lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.Dailydose = StringVar()
        self.sideEffect = StringVar()
        self.furtherInformation = StringVar()
        self.storageadvice = StringVar()
        self.drivingusMachine = StringVar()
        self.howtousemedicine = StringVar()
        self.nhsnumber = StringVar()
        self.pid = StringVar()
        self.pname = StringVar()
        self.dob = StringVar()
        self.patientaddress = StringVar()

        # Title Label
        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="Hospital Management System", fg="red", bg="white", font=("Times New Roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # Dataframe
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        dataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("arial", 12, "bold"), text="Patient Information")
        dataframeLeft.place(x=0, y=5, width=980, height=350)

        dataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("arial", 12, "bold"), text="Prescription")
        dataframeRight.place(x=990, y=5, width=460, height=350)

        # Buttons
        buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        buttonframe.place(x=0, y=530, width=1530, height=70)

        # Details Frame
        detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        detailsframe.place(x=0, y=600, width=1530, height=190)

        # DataframeLeft
        lblnametablet = Label(dataframeLeft, text="Names of Tablet", font=("arial", 12, "bold"), padx=2, pady=6)
        lblnametablet.grid(row=0, column=0)

        # Combobox
        comnametablet = ttk.Combobox(dataframeLeft, textvariable=self.nameoftablets, state='readonly', font=("arial", 12, "bold"), width=33)
        comnametablet['values'] = ('Pantaprazole DSR', 'Corona Vaccine', 'Tetanus Vaccine', 'Refresh Tears', 'Paracetamol', 'Amoxycilin', 'Azithromycin', 'Moxifloxacin', 'Levocetrizine', 'Norfloxacin and Tinidazole combo', 'Neomycin')
        comnametablet.current(0)
        comnametablet.grid(row=0, column=1)

        lblref = Label(dataframeLeft, font=('arial', 12, 'bold'), text="Reference Number:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(dataframeLeft, textvariable=self.ref, font=('arial', 13, 'bold'), width=35)
        txtref.grid(row=1, column=1)

        lbldose = Label(dataframeLeft, font=('arial', 12, 'bold'), text='Dose:', padx=2, pady=4)
        lbldose.grid(row=2, column=0, sticky=W)
        txtdose = Entry(dataframeLeft, textvariable=self.dose, font=('arial', 13, 'bold'), width=35)
        txtdose.grid(row=2, column=1)

        # No of Tablets
        lblnumberoftablet = Label(dataframeLeft, font=('arial', 12, 'bold'), text='No. of Tablets:', padx=2, pady=6)
        lblnumberoftablet.grid(row=3, column=0, sticky=W)
        txtnooftablets = Entry(dataframeLeft, textvariable=self.nooftablets, font=('arial', 13, 'bold'), width=35)
        txtnooftablets.grid(row=3, column=1)

        # Lot
        lblLot = Label(dataframeLeft, font=('arial', 12, 'bold'), text='Lot:', padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(dataframeLeft, textvariable=self.lot, font=('arial', 13, 'bold'), width=35)
        txtLot.grid(row=4, column=1)

        # Date of Issue
        lbldoi = Label(dataframeLeft, font=('arial', 12, 'bold'), text='Date of Issue:', padx=2, pady=6)
        lbldoi.grid(row=5, column=0, sticky=W)
        txtdoi = Entry(dataframeLeft, textvariable=self.IssueDate, font=('arial', 13, 'bold'), width=35)
        txtdoi.grid(row=5, column=1)

        # Date of Expiry
        lbldoexp = Label(dataframeLeft, font=('arial', 12, 'bold'), text='Date of Expiry:', padx=2, pady=6)
        lbldoexp.grid(row=6, column=0, sticky=W)
        txtdoep = Entry(dataframeLeft, textvariable=self.ExpDate, font=('arial', 13, 'bold'), width=35)
        txtdoep.grid(row=6, column=1)

        # Daily Doses
        lbldailydose = Label(dataframeLeft, font=('arial', 12, 'bold'), text='Daily Dose:', padx=2, pady=4)
        lbldailydose.grid(row=7, column=0, sticky=W)
        txtdailydose = Entry(dataframeLeft, textvariable=self.Dailydose, font=('arial', 13, 'bold'), width=35)
        txtdailydose.grid(row=7, column=1)

        # Side Effect
        lblsideEffect = Label(dataframeLeft, font=('arial', 12, 'bold'), text='Side Effect:', padx=2, pady=6)
        lblsideEffect.grid(row=8, column=0, sticky=W)
        txtsideEffect = Entry(dataframeLeft, textvariable=self.sideEffect, font=('arial', 13, 'bold'), width=35)
        txtsideEffect.grid(row=8, column=1)

        # Further Information
        lblinfo = Label(dataframeLeft, font=('arial', 12, 'bold'), text='Further Information:', padx=2)
        lblinfo.grid(row=0, column=2, sticky=W)
        txtinfo = Entry(dataframeLeft, textvariable=self.furtherInformation, font=('arial', 13, 'bold'), width=35)
        txtinfo.grid(row=0, column=3)

        # Driving Us Machine
        lblbp = Label(dataframeLeft, font=('arial', 12, 'bold'), text='Driving Us Machine:', padx=2, pady=6)
        lblbp.grid(row=1, column=2, sticky=W)
        txtbp = Entry(dataframeLeft, textvariable=self.drivingusMachine, font=('arial', 13, 'bold'), width=35)
        txtbp.grid(row=1, column=3)

        # Storage Advice
        lblStorage = Label(dataframeLeft, font=('arial', 12, 'bold'), text='Storage Advice:', padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtstorage = Entry(dataframeLeft, textvariable=self.storageadvice, font=('arial', 13, 'bold'), width=35)
        txtstorage.grid(row=2, column=3)

        # Medication
        lblmedication = Label(dataframeLeft, font=('arial', 12, 'bold'), text='Medication:', padx=2, pady=6)
        lblmedication.grid(row=3, column=2, sticky=W)
        txtmedication = Entry(dataframeLeft, textvariable=self.howtousemedicine, font=('arial', 13, 'bold'), width=35)
        txtmedication.grid(row=3, column=3)

        # Patient Id
        lblPid = Label(dataframeLeft, font=('arial', 12, 'bold'), text='Patient Id:', padx=2, pady=6)
        lblPid.grid(row=4, column=2, sticky=W)
        txtPid = Entry(dataframeLeft, textvariable=self.pid, font=('arial', 13, 'bold'), width=35)
        txtPid.grid(row=4, column=3)

        # NHS Number
        lblnhs = Label(dataframeLeft, font=('arial', 12, 'bold'), text='NHS Number:', padx=2, pady=6)
        lblnhs.grid(row=5, column=2, sticky=W)
        txtnhs = Entry(dataframeLeft, textvariable=self.nhsnumber, font=('arial', 13, 'bold'), width=35)
        txtnhs.grid(row=5, column=3)

        # Patient Name
        lblname = Label(dataframeLeft, font=('arial', 12, 'bold'), text='Patient Name:', padx=2, pady=6)
        lblname.grid(row=6, column=2, sticky=W)
        txtname = Entry(dataframeLeft, textvariable=self.pname, font=('arial', 13, 'bold'), width=35)
        txtname.grid(row=6, column=3)

        # Date of Birth
        lbldob = Label(dataframeLeft, font=('arial', 12, 'bold'), text='Date of Birth:', padx=2, pady=6)
        lbldob.grid(row=7, column=2, sticky=W)
        txtdob = Entry(dataframeLeft, textvariable=self.dob, font=('arial', 13, 'bold'), width=35)
        txtdob.grid(row=7, column=3)

        # Address
        lbladdress = Label(dataframeLeft, font=('arial', 12, 'bold'), text='Patient Address:', padx=2, pady=6)
        lbladdress.grid(row=8, column=2, sticky=W)
        txtaddress = Entry(dataframeLeft, textvariable=self.patientaddress, font=('arial', 13, 'bold'), width=35)
        txtaddress.grid(row=8, column=3)

        # DataframeRight
        self.txtPrescription = Text(dataframeRight, font=('arial', 12, 'bold'), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # Buttons
        btnPrescription = Button(buttonframe, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6, command=self.iPrescription)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(buttonframe, text="Prescription Data", bg="sky blue", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6, command=self.iPrescriptionData)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(buttonframe, text="Update", bg="yellow", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6, command=self.update_data)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(buttonframe, text="Delete", bg="light green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6, command=self.delete_data)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(buttonframe, text="Clear", bg="magenta", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6, command=self.clear)
        btnClear.grid(row=0, column=4)

        btnExit = Button(buttonframe, text="Exit", bg="cyan", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6, command=self.iExit)
        btnExit.grid(row=0, column=5)

        # Table
        scroll_x = ttk.Scrollbar(detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailsframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(detailsframe, column=("nameoftablets", "ref", "dose", "nooftablets", "lot", "IssueDate", "ExpDate", "Dailydose", "storage", "nhsnumber", "pname", "dob", "patientaddress"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets", text="Names of Tablet")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("IssueDate", text="Issue Date")
        self.hospital_table.heading("ExpDate", text="Exp Date")
        self.hospital_table.heading("Dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("patientaddress", text="Patient Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("nameoftablets", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("IssueDate", width=100)
        self.hospital_table.column("ExpDate", width=100)
        self.hospital_table.column("Dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("patientaddress", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # Functions for the buttons
    def iPrescription(self):
        self.txtPrescription.insert(END, "Name of Tablets:\t\t\t" + self.nameoftablets.get() + "\n")
        self.txtPrescription.insert(END, "Reference Number:\t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + self.dose.get() + "\n")
        self.txtPrescription.insert(END, "No of Tablets:\t\t\t" + self.nooftablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t" + self.lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.IssueDate.get() + "\n")
        self.txtPrescription.insert(END, "Exp Date:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END, "Daily Dose:\t\t\t" + self.Dailydose.get() + "\n")
        self.txtPrescription.insert(END, "Storage Advice:\t\t\t" + self.storageadvice.get() + "\n")
        self.txtPrescription.insert(END, "NHS Number:\t\t\t" + self.nhsnumber.get() + "\n")
        self.txtPrescription.insert(END, "Patient Name:\t\t\t" + self.pname.get() + "\n")
        self.txtPrescription.insert(END, "Date of Birth:\t\t\t" + self.dob.get() + "\n")
        self.txtPrescription.insert(END, "Patient Address:\t\t\t" + self.patientaddress.get() + "\n")

    def iPrescriptionData(self):
        if self.ref.get() == "" or self.pname.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="Mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into Hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                        self.nameoftablets.get(),
                                                                                        self.ref.get(),
                                                                                        self.dose.get(),
                                                                                        self.nooftablets.get(),
                                                                                        self.lot.get(),
                                                                                        self.IssueDate.get(),
                                                                                        self.ExpDate.get(),
                                                                                        self.Dailydose.get(),
                                                                                        self.storageadvice.get(),
                                                                                        self.nhsnumber.get(),
                                                                                        self.pname.get(),
                                                                                        self.dob.get(),
                                                                                        self.patientaddress.get()
                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="Mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Hospital")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content['values']
        self.nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.dose.set(row[2])
        self.nooftablets.set(row[3])
        self.lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.Dailydose.set(row[7])
        self.storageadvice.set(row[8])
        self.nhsnumber.set(row[9])
        self.pname.set(row[10])
        self.dob.set(row[11])
        self.patientaddress.set(row[12])


    def update_data(self):
        conn= mysql.connector.connect(host='localhost', username='root', password='1234',database='Mydata')
        m_cursor= conn.cursor()
        m_cursor.execute("update hospital set nameoftablets=%s,dose=%s,nooftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,dob=%s,patientaddress=%s where reference_number=%s", (
                                                                                                                self.nameoftablets.get(),
                                                                                                                self.dose.get(),
                                                                                                                self.nooftablets.get(),
                                                                                                                self.lot.get(),
                                                                                                                self.IssueDate.get(),
                                                                                                                self.ExpDate.get(),
                                                                                                                self.Dailydose.get(),
                                                                                                                self.storageadvice.get(),
                                                                                                                self.nhsnumber.get(),
                                                                                                                self.pname.get(),
                                                                                                                self.dob.get(),
                                                                                                                self.patientaddress.get(),
                                                                                                                self.ref.get()
                                                                                                            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update", "Patient details have been updated successfully")

    def delete_data(self):
        conn= mysql.connector.connect(host='localhost', username='root', password='1234',database='Mydata')
        m_cursor= conn.cursor()
        query = "delete from hospital where reference_number=%s"
        value = (self.ref.get(),)
        m_cursor.execute(query, value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete", "Patient details have been deleted successfully")
    def clear(self):
        self.nameoftablets.set("")
        self.ref.set("")
        self.dose.set("")
        self.nooftablets.set("")
        self.lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.Dailydose.set("")
        self.sideEffect.set("")
        self.furtherInformation.set("")
        self.storageadvice.set("")
        self.drivingusMachine.set("")
        self.howtousemedicine.set("")
        self.nhsnumber.set("")
        self.pid.set("")
        self.pname.set("")
        self.dob.set("")
        self.patientaddress.set("")
        self.txtPrescription.delete("1.0", END)

    def iExit(self):
        exit_confirm = messagebox.askyesno("Hospital Management System", "Do you want to exit?")
        if exit_confirm > 0:
            root.destroy()
            return


root = Tk()
ob = Hospital(root)
root.mainloop()
