from tkinter import*
from tkinter import ttk
from scanner import scan_ports
import re
from tkinter import messagebox

class ScannerP:
    def __init__(self, root):
        self.root = root
        self.root.title("Port Scanner")
        self.root.minsize(490, 260)
        self.root.maxsize(490, 260)

        # variables
        self.var_ip = StringVar()
        self.var_startPort = IntVar()
        self.var_endPort = IntVar()

        # title
        lbl_title = Label(self.root, text="Port Scanner", font=(
            "times new roman", 30, "bold"), bg="black", fg="silver", anchor="center")
        lbl_title.place(x=0, y=0, width=490, height=50)


        # label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Scanner", font=(
            "times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=475, height=200)

        #########labels and enteries
        # hostname
        lbl_hostname = Label(labelframeleft, text="IP/Hostname:", font=(
            "arial", 13, "bold"), padx=2, pady=6)
        lbl_hostname.grid(row=0, column=0, sticky=W)

        entry_hostname = ttk.Entry(
            labelframeleft, textvariable=self.var_ip, width=18, font=("arial", 13, "bold"))
        entry_hostname.grid(row=0, column=1, sticky=W)

        # startport
        startPort = Label(labelframeleft, text="Start port:",
                          font=("arial", 13, "bold"), padx=2, pady=6)
        startPort.grid(row=1, column=0, sticky=W)

        txtstartPort = ttk.Entry(
            labelframeleft, textvariable=self.var_startPort, width=25, font=("arial", 13, "bold"))
        txtstartPort .grid(row=1, column=1)

        # endPort
        endPort = Label(
            labelframeleft, text="End port:", font=("arial", 13, "bold"), padx=2, pady=6)
        endPort.grid(row=2, column=0, sticky=W)

        txtendPort = ttk.Entry(
            labelframeleft, textvariable=self.var_endPort, width=25, font=("arial", 13, "bold"))
        txtendPort.grid(row=2, column=1)

        # scan port button
        btnScanPort = Button(labelframeleft, text="Scan", command=self.open_port, font=(
            "arial", 13, "bold"), bg="black", fg="silver", width=8)
        btnScanPort.grid(row=10, column=0, padx=(20, 5), pady=5)
        
        # reset button
        btnReset = Button(labelframeleft, text="Reset", command=self.reset,  font=(
            "arial", 13, "bold"), bg="black", fg="silver", width=8)
        btnReset.grid(row=10, column=1, padx=5, pady=5)

        # exit button
        btnExit = Button(labelframeleft, text="Exit", command=self.exit, font=(
            "arial", 13, "bold"), bg="black", fg="silver", width=8)
        btnExit.grid(row=10, column=2, padx=(5, 20), pady=5)

    def reset(self):
        self.var_ip.set(""),
        self.var_startPort.set(""),
        self.var_endPort.set("")

    def open_port(self):
        host = self.var_ip.get()
        start = self.var_startPort.get()
        end = self.var_endPort.get()
        
        ipv4_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'

        if not re.match(ipv4_pattern, host):
            messagebox.showerror("Error", "Please enter a valid IPv4 address", parent=self.root)
            return

        parts = host.split('.')
        for part in parts:
            if not (0 <= int(part) <= 255):
                messagebox.showerror("Error", "Please enter a valid port range", parent=self.root)
                return

        if start < 0 or end > 65353:
            if start < 0:
                messagebox.showerror("Error", "Please enter a valid start port", parent=self.root)
            if end > 65353:
                messagebox.showerror("Error", "Please enter a valid end port", parent=self.root)
        else:
            scan_ports(host, start, end)

    def exit(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = ScannerP(root)
    root.mainloop()
