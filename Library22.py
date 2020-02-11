from tkinter import *
from tkinter import ttk
import random
import datetime

from tkinter import messagebox
from datetime import datetime
import tkinter.messagebox

class Library:
    def __init__(self,root):
        self.root = root
        self.root.title("Library management system")
        self.root.geometry("900x1600+0+0")
        self.root.configure(background = 'powder blue')
        #=============================Declare Variable=============================
        MemberType = StringVar()
        Ref = StringVar()
        Title = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address1 = StringVar()
        Address2 = StringVar()
        PostCode = StringVar()
        MobileNo = StringVar()
        BookID = StringVar()
        BookTitle = StringVar()
        BookType = StringVar()
        Author = StringVar()
        DateBorrowed = StringVar()
        DateDue = StringVar()
        SellingPrice = StringVar()
        LateReturnFine = StringVar()
        DateOverDue = StringVar()
        DaysOnLoan = StringVar()
        Prescription = StringVar()
        def iReset():
            MemberType.set("")  
            Ref.set("")  
            Title.set("")  
            Firstname.set("")  
            Surname.set("")   
            Address1.set("")  
            Address2.set("")  
            PostCode.set("")  
            MobileNo.set("")  
            BookID.set("")  
            BookTitle.set("")  
            BookType.set("")  
            Author.set("")  
            DateBorrowed.set("")  
            DateDue.set("") 
            SellingPrice.set("")  
            LateReturnFine.set("") 
            DateOverDue.set("") 
            DaysOnLoan.set("") 
            Prescription.set("")
            self.TextDisplayRight.delete("1.0",END)

        def iDelete():
            iReset()
            self.TextDisplayRight.delete("1.0",END)
            

        def iExit():
            iExit = tkinter.messagebox.askyesno("Library Management System","Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return
        def iDisplay():
            self.TextDisplayRight.insert(END,"\t"+MemberType.get()+"\t\t"+Ref.get()+"\t"+Title.get()+"\t"+  BookID.get()+"\t"+Firstname.get()+"\t"+Surname.get()+"\t\t"+Address1.get()+"\t\t"+Address2.get()+"\t"+PostCode.get()+"\t"+BookTitle.get()+"\t\t"+BookTitle.get()+"\t\t"+DateBorrowed.get()+"\t\t"+DaysOnLoan.get()+"\n")
        def iReceipt():
                    self.TextDisplayRight.insert(END,"MemberType: \t\t"+MemberType.get()+"\n")
                    self.TextDisplayRight.insert(END,"Ref No. : \t\t"+ Ref.get()+"\n")
                    self.TextDisplayRight.insert(END,"Title: \t\t"+Title.get()+"\n")
                    self.TextDisplayRight.insert(END,"Firstname: \t\t"+Firstname.get()+"\n")
                    self.TextDisplayRight.insert(END,"Surname: \t\t"+Surname.get()+"\n")
                    self.TextDisplayRight.insert(END,"Address1: \t\t"+Address1.get()+"\n")
                    self.TextDisplayRight.insert(END,"Address2: \t\t"+Address2.get()+"\n")
                    self.TextDisplayRight.insert(END,"PostCode: \t\t"+PostCode.get()+"\n")
                    self.TextDisplayRight.insert(END,"MobileNo: \t\t"+MobileNo.get()+"\n")
                    self.TextDisplayRight.insert(END,"BookID: \t\t"+BookID.get()+"\n")
                    self.TextDisplayRight.insert(END,"BookTitle: \t\t"+BookTitle.get()+"\n")
                             #self.TextDisplayRight.insert(END," BookType: \t\t"+  BookType.get()+"\n")
                    self.TextDisplayRight.insert(END,"Author: \t\t"+Author.get()+"\n")
                    self.TextDisplayRight.insert(END,"DateBorrowed: \t\t"+DateBorrowed.get()+"\n")
                                #self.TextDisplayRight.insert(END," DateDue: \t\t"+  DateDue.get()+"\n")
                                 #self.TextDisplayRight.insert(END," SellingPrice: \t\t"+ SellingPrice.get()+"\n")
                                  #self.TextDisplayRight.insert(END,"LateReturnFine: \t\t"+ LateReturnFine.get()+"\n")
                                  #self.TextDisplayRight.insert(END," DateOverDue: \t\t"+ DateOverDue.get()+"\n")
                                  #self.TextDisplayRight.insert(END,"DaysOnLoan: \t\t"+DaysOnLoan.get()+"\n")
                    


        #=============================FrameWork=============================
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width = 1600 ,padx =20,bd= 20 ,relief = RIDGE)
        TitleFrame.pack(side = TOP)
        self.lblTitle = Label(TitleFrame, width = 47,font = ('arial',40, 'bold'),text = "\t Library Management System\t" ,padx =12)
        self.lblTitle.grid()
        
        
        ButtonFrame = Frame(MainFrame ,bd = 20 , width =1600,height = 50 ,padx =100 ,relief = RIDGE )
        ButtonFrame.pack(side = BOTTOM)

        FrameDetail = Frame(MainFrame, bd=20, width=1600,height = 100, padx=100,  relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=20, width=1600, height=400, padx=40, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame( DataFrame, bd=10, width=910, height=300, padx=36, relief=RIDGE ,font =('arial',12,'bold'),text = "Library Membership Info : ")
        DataFrameLEFT.pack(side=LEFT )

        DataFrameRIGHT = LabelFrame(DataFrame, bd=10, width=610, height=300, padx=46, relief=RIDGE,
                                   font=('arial', 12, 'bold'), text="Book Details  : ")
        DataFrameRIGHT.pack(side=LEFT)


        AdeshDetails = Frame(MainFrame, bd=20, width=1600, height=120, padx=40, relief=RIDGE)
        AdeshDetails.pack(side=BOTTOM)
        self.lblTitle = Label(AdeshDetails, width = 60,font = ('arial',30, 'bold'),text = "\t Project : Adesh Singh\t" ,padx =15)
        self.lblTitle.grid()
        
        
       


        
        #=============================Widget=============================
        self.lblMemberType = Label(DataFrameLEFT , font = ("arial" , 12,"bold"), text = " Member Type : ",padx= 2,pady = 2)
        self.lblMemberType.grid(row = 0,column = 0, sticky = W)


        self.cboMemberType = ttk.Combobox(DataFrameLEFT , font = ('arial',12,'bold'), state = 'readonly',textvariable = MemberType , width= 23)
        self.cboMemberType['value'] = (" ",'Student','Lecturer','Admin Staff','Other')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row =0,column = 1)

        



        self.lblBooKID = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Book ID :', padx=2, pady=2)

        self.lblBooKID.grid(row=0, column=2, sticky=W)

        self.lblBooKID = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = BookID,width= 25 )

        self.lblBooKID.grid(row=0, column=3)
        
        

        self.lblRef = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Reference No:', padx=2, pady=2)

        self.lblRef.grid(row=1, column=0, sticky=W)

        self.lblRef = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),width= 25,textvariable = Ref )

        self.lblRef.grid(row=1, column=1)
        
        
        

        self.lblBookTitle = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Book Title:', padx=2, pady=2)

        self.lblBookTitle.grid(row=1, column=2, sticky=W)

        self.lblBookTitle = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=23,textvariable =BookTitle)

        self.lblBookTitle.grid(row=1, column=3)


        self.lblTitle = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Title:', padx=2, pady=2)

        self.lblTitle.grid(row=2, column=0, sticky=W)



       


        self.cboTitle = ttk.Combobox(DataFrameLEFT , font = ('arial',12,'bold'), state = 'readonly' ,textvariable =Title, width= 25)
        self.cboTitle['value'] = (" ",'Mr.','Miss.','Mrs.','Dr.','Capt.','Ms.')
        self.cboTitle.current(0)
        self.cboTitle.grid(row =2,column = 1)



        self.lblAuthor = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Author:', padx=2, pady=2)

        self.lblAuthor.grid(row=2, column=2, sticky=W)

        self.lblAuthor = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25,textvariable = Author)

        self.lblAuthor.grid(row=2, column=3)



        self.lblFirstName = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='FirstName:', padx=2, pady=2)

        self.lblFirstName.grid(row=3, column=0, sticky=W)

        self.lblFirstName = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25,textvariable =Firstname)

        self.lblFirstName.grid(row=3, column=1)



        self.lblDateBorrowed = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='DateBorrowed:', padx=2, pady=2)

        self.lblDateBorrowed.grid(row=3, column=2, sticky=W)

        self.lblDateBorrowed = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25,textvariable =DateBorrowed)

        self.lblDateBorrowed.grid(row=3, column=3)



        
        self.lblSurname = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Surname:', padx=2, pady=2)

        self.lblSurname.grid(row=4, column=0, sticky=W)

        self.lblSurname = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25,textvariable =Surname)

        self.lblSurname.grid(row=4, column=1)


        self.lbladdress1 = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Address 1:', padx=2, pady=2)

        self.lbladdress1.grid(row=5, column=0, sticky=W)

        self.lbladdress1 = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25,textvariable =Address1)

        self.lbladdress1.grid(row=5, column=1)


        self.lbladdress2 = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Address 2:', padx=2, pady=2)

        self.lbladdress2.grid(row=6, column=0, sticky=W)

        self.lbladdress2 = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25,textvariable =Address2)

        self.lbladdress2.grid(row=6, column=1)


        self.lblPostCode = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='PostCode:', padx=2, pady=2)

        self.lblPostCode.grid(row=7, column=0, sticky=W)

        self.lblPostCode = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25,textvariable =PostCode)

        self.lblPostCode.grid(row=7, column=1)




        self.lblMobileNo = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='MobileNo:', padx=2, pady=2)

        self.lblMobileNo.grid(row=8, column=0, sticky=W)

        self.lblMobileNo = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25,textvariable =MobileNo)

        self.lblMobileNo.grid(row=8, column=1)


        
        self.lblBookDue = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='BookDue:', padx=2, pady=2)

        self.lblBookDue.grid(row=4, column=2, sticky=W)

        self.lblBookDue = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25,textvariable =DateDue)

        self.lblBookDue.grid(row=4, column=3)



        self.lblDaysOnLoan = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Days On Loan:', padx=2, pady=2)

        self.lblDaysOnLoan.grid(row=5, column=2, sticky=W)

        self.lblDaysOnLoan = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25,textvariable =DaysOnLoan)

        self.lblDaysOnLoan.grid(row=5, column=3)


        
        self.lblLateReturnFine = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Late Return Fine:', padx=2, pady=2)

        self.lblLateReturnFine.grid(row=6, column=2, sticky=W)

        self.lblLateReturnFine = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25,textvariable =LateReturnFine)

        self.lblLateReturnFine.grid(row=6, column=3)



        
        self.lblDateOverDue = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Date Over Due:', padx=2, pady=2)

        self.lblDateOverDue.grid(row=7, column=2, sticky=W)

        self.lblDateOverDue = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25,textvariable =DateOverDue)

        self.lblDateOverDue.grid(row=7, column=3)


        self.lblSellingPrice = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Selling Price:', padx=2, pady=2)

        self.lblSellingPrice.grid(row=8, column=2, sticky=W)

        self.lblSellingPrice = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=25,textvariable =SellingPrice)

        self.lblSellingPrice.grid(row=8, column=3)
          #=============================Widget2=============================
        
        self.TextDisplayRight = Text(DataFrameRIGHT, font=('arial', 12, 'bold'), width=32,height=13,padx =8,pady =20)

        self.TextDisplayRight.grid(row=0, column=2)
          #=============================List Box=============================
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row = 0,column = 1,sticky = 'ns')
       


        ListOfBooks = ['Cinderella','Game Design','Ancient Rome','Made in Africa','Sleeping beauty','London','Nigeria','Snow white','Shreik 3','London Street','I love Lagos','Love Kenya','Hello India']

        def SelectedBook(evt):
            value = str(booklist.get(booklist.curselection()))
            w= value
            if (w =='Cinderella'):
                BookID.set("ISBN 358653256")
                BookTitle.set("The Art Of Living")
                Author.set("Adesh singh")
                import datetime
                d1=datetime.date.today()
                d2 = datetime.timedelta(days = 14)
                d3 = d1 + d2
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")
        
                        
                    
        booklist = Listbox(DataFrameRIGHT,width = 20,height = 12,font=('arial', 12, 'bold'))
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        booklist.grid(row = 0,column = 0,padx = 8)
        scrollbar.config(command = booklist.yview)               

        for items in ListOfBooks:
            booklist.insert(END,items)
        #===================================Button==================================================================
        self.lblLabel = Label(FrameDetail,font=('arial', 12, 'bold'),pady = 8,text = 'Member Type \t Reference No.\tTitle \tSurname \tAddress 1\tAddress 2\tPost Code\tBook Title\t Date Borrow\t Days To Loan')    
        self.lblLabel.grid(row =0,column = 0)


           
        self.TextDisplayRight = Text(FrameDetail, font=('arial', 12, 'bold'), width=141,height=4,padx =2,pady =4)

        self.TextDisplayRight.grid(row=1, column=0)


            
        #===================================Button==================================================================
        self.btnDisplayData = Button(ButtonFrame,text='Display Data', font=('arial', 12, 'bold'), width=32, bd =4,command=iDisplay,padx =2,pady =4)
        self.btnDisplayData.grid(row=0,column=0)

        self.btnDelete = Button(ButtonFrame, text='Delete', font=('arial', 12, 'bold'), width=32, bd=4,command=iDelete,padx =2,pady =4)
        self.btnDelete.grid(row=0, column=1)

        self.btnReset = Button(ButtonFrame, text='Reset', font=('arial', 12, 'bold'), width=32, bd=4,command = iReset,padx =2,pady =4)
        self.btnReset.grid(row=0, column=2)

        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 12, 'bold'), width=32, bd=4,command = iExit,padx =2,pady =4)
        self.btnExit.grid(row=0, column=3)


if __name__ =='__main__':
    root  = Tk()
    application = Library(root)
    root.mainloop()
