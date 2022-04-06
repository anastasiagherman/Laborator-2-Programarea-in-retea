import os
import smtplib
import tkinter as tk
from tkinter import END, filedialog
from tkinter import messagebox
from MailOperations import MailOperations
from Page import Page

file_paths = []


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def send_mail():
            recipient = recipient_var.get()
            subject = subject_var.get()
            message = message_text.get('1.0', END)

            if recipient != '' and subject != '' and message != '':
                print(recipient, subject, message)
                server = smtplib.SMTP('smtp.gmail.com', 587)
                MailOperations('testingemailacount@gmail.com', 'testingAccount01').send_email(recipient,
                                                                                      subject,
                                                                                      message,
                                                                                      file_paths)

            recipient_entry.delete(0, END)
            subject_entry.delete(0, END)
            path.delete(0, END)
            message_text.delete('1.0', END)
            file_paths.clear()

        def set_text(text):
            path.insert(END, text)
            return

        def get_path():
            tk.Tk().withdraw()
            new_path = filedialog.askopenfilename()
            print(new_path)
            print(os.path.getsize(new_path))
            if os.path.getsize(new_path) > 2_000_000:
                messagebox.showerror("Error!","The file is too big")
            else:
                file_paths.append(new_path)
            set_text(new_path)

        # Recipient
        label = tk.Label(self, text="Recipient:", bg="light blue")
        label.config(font=("Consolas", 15))
        recipient_var = tk.StringVar()
        recipient_entry = tk.Entry(self, width="35", textvariable=recipient_var)

        # Subject
        label2 = tk.Label(self, text="Subject:", bg="light blue")
        label2.config(font=("Consolas", 15))
        subject_var = tk.StringVar()
        subject_entry = tk.Entry(self, width="50", textvariable=subject_var)

        # Attachments

        # Label
        label3 = tk.Label(self, text="Attachments:", bg="light blue")
        label3.config(font=("Consolas", 15))

        # Entry to display path to file
        path = tk.Listbox(self, width=70, height=5)

        # Button to call file Dialog
        select = tk.Button(self, text="Select File < 2MB", command=get_path)

        # Message
        label4 = tk.Label(self, text="Message:", bg="light blue")
        label4.config(font=("Consolas", 15))
        message_text = tk.Text(self, width="80", height="5")

        # @ Send Button @
        send = tk.Button(self, text="Send E-Mail", command=send_mail)
        send.config(font=("Consolas", 15))

        # Pack
        label.pack(expand=True)
        recipient_entry.pack(expand=True)
        label2.pack(expand=True)
        subject_entry.pack(expand=True)
        label3.pack(expand=True)
        path.pack(expand=True)
        select.pack(expand=True)
        label4.pack(expand=True)
        message_text.pack(expand=True, ipady=30)
        send.pack(expand=True)
