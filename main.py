import tkinter
from scapy.all import *
from tkinter import ttk
from tkinter import messagebox

def features_ICMP():
    rootICMP = tkinter.Tk()
    rootICMP.title("ICMP")
    rootICMP.geometry("300x150")
    rootICMP.resizable(False, False)
    label_nr = ttk.Label(rootICMP, text="Numarul de pachete:")
    label_nr.grid(row=0, column=0)
    entry_nr = ttk.Entry(rootICMP, width=30)
    entry_nr.grid(row=0, column=1)
    entry_nr.insert(0, "1")
    label_d = ttk.Label(rootICMP, text="IP destinatie:")
    label_d.grid(row=1, column=0)
    entry_d = ttk.Entry(rootICMP, width=30)
    entry_d.grid(row=1, column=1)
    entry_d.insert(0, "127.0.0.1")
    label_s = ttk.Label(rootICMP, text="IP sursa:")
    label_s.grid(row=2, column=0)
    entry_s = ttk.Entry(rootICMP, width=30)
    entry_s.grid(row=2, column=1)
    entry_s.insert(0, "127.0.0.1")
    label_tip = ttk.Label(rootICMP, text="Tip ICMP:")
    label_tip.grid(row=3, column=0)
    entry_tip = ttk.Entry(rootICMP, width=30)
    entry_tip.grid(row=3, column=1)
    entry_tip.insert(0, "8")
    label_cod = ttk.Label(rootICMP, text="Cod ICMP:")
    label_cod.grid(row=4, column=0)
    entry_cod = ttk.Entry(rootICMP, width=30)
    entry_cod.grid(row=4, column=1)
    entry_cod.insert(0, "0")
    def trimiteICMP():
        icmp_packet = IP(src=entry_s.get(), dst=entry_d.get()) / ICMP(type=int(entry_tip.get()), code=int(entry_cod.get()))
        print(icmp_packet.show())
        for i in range(int(entry_nr.get())):
            send(icmp_packet)
        messagebox.showinfo("!!!","Pachete transmise cu succes!")
    buttonICMP = ttk.Button(rootICMP, text="Trimite pachete", command= trimiteICMP)
    buttonICMP.grid(row=6, column=0)
def features_HTTP():
    rootHTTP = tkinter.Tk()
    rootHTTP.title("HTTP")
    rootHTTP.geometry("300x160")
    rootHTTP.resizable(False, False)
    label_nr = ttk.Label(rootHTTP, text="Numarul de pachete:")
    label_nr.grid(row=0, column=0)
    entry_nr = ttk.Entry(rootHTTP, width=30)
    entry_nr.grid(row=0, column=1)
    entry_nr.insert(0, "1")
    label_d = ttk.Label(rootHTTP, text="IP destinatie:")
    label_d.grid(row=1, column=0)
    entry_d = ttk.Entry(rootHTTP, width=30)
    entry_d.grid(row=1, column=1)
    entry_d.insert(0, "127.0.0.1")
    label_s = ttk.Label(rootHTTP, text="IP dursa:")
    label_s.grid(row=2, column=0)
    entry_s = ttk.Entry(rootHTTP, width=30)
    entry_s.grid(row=2, column=1)
    entry_s.insert(0, "127.0.0.1")
    label_pd = ttk.Label(rootHTTP, text="Port destinatie:")
    label_pd.grid(row=3, column=0)
    entry_pd = ttk.Entry(rootHTTP, width=30)
    entry_pd.grid(row=3, column=1)
    entry_pd.insert(0, "80")
    label_ps = ttk.Label(rootHTTP, text="Port sursa:")
    label_ps.grid(row=4, column=0)
    entry_ps = ttk.Entry(rootHTTP, width=30)
    entry_ps.grid(row=4, column=1)
    entry_ps.insert(0, "80")
    label_f = ttk.Label(rootHTTP, text="Flags:")
    label_f.grid(row=5, column=0)
    entry_f = ttk.Entry(rootHTTP, width=30)
    entry_f.grid(row=5, column=1)
    entry_f.insert(0, "S")
    def trimiteTCP_HTTP():
        tcp_http_packet = IP(src=entry_s.get(), dst=entry_d.get()) / TCP(sport=int(entry_ps.get()), dport=int(entry_pd.get()),flags=entry_f.get())
        for i in range(int(entry_nr.get())):
            send(tcp_http_packet)
        messagebox.showinfo("!!!", "Pachete transmise cu succes!")
    buttonTCP_HTTP = ttk.Button(rootHTTP, text="Trimite pachete", command=trimiteTCP_HTTP)
    buttonTCP_HTTP.grid(row=6, column=0)
def features_FTP():
    rootFTP = tkinter.Tk()
    rootFTP.title("FTP")
    rootFTP.geometry("300x160")
    rootFTP.resizable(False, False)
    label_nr = ttk.Label(rootFTP, text="Numarul de pachete:")
    label_nr.grid(row=0, column=0)
    entry_nr = ttk.Entry(rootFTP, width=30)
    entry_nr.grid(row=0, column=1)
    entry_nr.insert(0, "1")
    label_d = ttk.Label(rootFTP, text="Destinatie:")
    label_d.grid(row=1, column=0)
    entry_d = ttk.Entry(rootFTP, width=30)
    entry_d.grid(row=1, column=1)
    entry_d.insert(0, "127.0.0.1")
    label_d = ttk.Label(rootFTP, text="Sursa:")
    label_d.grid(row=2, column=0)
    entry_s = ttk.Entry(rootFTP, width=30)
    entry_s.grid(row=2, column=1)
    entry_s.insert(0, "127.0.0.1")
    label_pd = ttk.Label(rootFTP, text="Port destinatie:")
    label_pd.grid(row=3, column=0)
    entry_pd = ttk.Entry(rootFTP, width=30)
    entry_pd.grid(row=3, column=1)
    entry_pd.insert(0, "20")
    label_ps = ttk.Label(rootFTP, text="Port sursa:")
    label_ps.grid(row=4, column=0)
    entry_ps = ttk.Entry(rootFTP, width=30)
    entry_ps.grid(row=4, column=1)
    entry_ps.insert(0, "21")
    label_f = ttk.Label(rootFTP, text="Flags:")
    label_f.grid(row=5, column=0)
    entry_f = ttk.Entry(rootFTP, width=30)
    entry_f.grid(row=5, column=1)
    entry_f.insert(0, "S")
    def trimiteTCP_FTP():
        tcp_ftp_packet = IP(src=entry_s.get(), dst=entry_d.get()) / TCP(sport=int(entry_ps.get()), dport=int(entry_pd.get()),flags=entry_f.get())
        for i in range(int(entry_nr.get())):
            send(tcp_ftp_packet)
        messagebox.showinfo("!!!", "Pachete transmise cu succes!")
    buttonTCP_FTP = ttk.Button(rootFTP, text="Trimite pachete", command=trimiteTCP_FTP)
    buttonTCP_FTP.grid(row=6, column=0)
def features_DNS():
    rootDNS = tkinter.Tk()
    rootDNS.title("DNS")
    rootDNS.geometry("300x180")
    rootDNS.resizable(False, False)
    label_nr = ttk.Label(rootDNS, text="Numarul de pachete:")
    label_nr.grid(row=0, column=0)
    entry_nr = ttk.Entry(rootDNS, width=30)
    entry_nr.grid(row=0, column=1)
    entry_nr.insert(0, "1")
    label_d = ttk.Label(rootDNS, text="Destinatie:")
    label_d.grid(row=1, column=0)
    entry_d = ttk.Entry(rootDNS, width=30)
    entry_d.grid(row=1, column=1)
    entry_d.insert(0, "127.0.0.1")
    label_d = ttk.Label(rootDNS, text="Sursa:")
    label_d.grid(row=2, column=0)
    entry_s = ttk.Entry(rootDNS, width=30)
    entry_s.grid(row=2, column=1)
    entry_s.insert(0, "127.0.0.1")
    label_pd = ttk.Label(rootDNS, text="Port destinatie:")
    label_pd.grid(row=3, column=0)
    entry_pd = ttk.Entry(rootDNS, width=30)
    entry_pd.grid(row=3, column=1)
    entry_pd.insert(0, "53")
    label_ps = ttk.Label(rootDNS, text="Port sursa:")
    label_ps.grid(row=4, column=0)
    entry_ps = ttk.Entry(rootDNS, width=30)
    entry_ps.grid(row=4, column=1)
    entry_ps.insert(0, "53")
    label_pl = ttk.Label(rootDNS, text="Payload:")
    label_pl.grid(row=5, column=0)
    entry_pl = ttk.Entry(rootDNS, width=30)
    entry_pl.grid(row=5, column=1)
    entry_pl.insert(0, "Hello, UDP!")
    def trimiteUDP_DNS():
        payload = entry_pl.get().encode()
        udp_dns_packet = IP(src=entry_s.get(), dst=entry_d.get()) / UDP(sport=int(entry_ps.get()), dport=int(entry_pd.get())) / payload
        for i in range(int(entry_nr.get())):
            send(udp_dns_packet)
        messagebox.showinfo("!!!", "Pachete transmise cu succes!")
    buttonUDP_DNS = ttk.Button(rootDNS, text="Trimite pachete", command=trimiteUDP_DNS)
    buttonUDP_DNS.grid(row=6, column=0)
def features_RTP():
    rootRTP = tkinter.Tk()
    rootRTP.title("RTP")
    rootRTP.geometry("300x180")
    rootRTP.resizable(False, False)
    label_nr = ttk.Label(rootRTP, text="Numarul de pachete:")
    label_nr.grid(row=0, column=0)
    entry_nr = ttk.Entry(rootRTP, width=30)
    entry_nr.grid(row=0, column=1)
    entry_nr.insert(0, "1")
    label_d = ttk.Label(rootRTP, text="Destinatie:")
    label_d.grid(row=1, column=0)
    entry_d = ttk.Entry(rootRTP, width=30)
    entry_d.grid(row=1, column=1)
    entry_d.insert(0, "127.0.0.1")
    label_d = ttk.Label(rootRTP, text="Sursa:")
    label_d.grid(row=2, column=0)
    entry_s = ttk.Entry(rootRTP, width=30)
    entry_s.grid(row=2, column=1)
    entry_s.insert(0, "127.0.0.1")
    label_pd = ttk.Label(rootRTP, text="Port destinatie:")
    label_pd.grid(row=3, column=0)
    entry_pd = ttk.Entry(rootRTP, width=30)
    entry_pd.grid(row=3, column=1)
    entry_pd.insert(0, "5004")
    label_ps = ttk.Label(rootRTP, text="Port sursa:")
    label_ps.grid(row=4, column=0)
    entry_ps = ttk.Entry(rootRTP, width=30)
    entry_ps.grid(row=4, column=1)
    entry_ps.insert(0, "5004")
    label_pl = ttk.Label(rootRTP, text="Payload:")
    label_pl.grid(row=5, column=0)
    entry_pl = ttk.Entry(rootRTP, width=30)
    entry_pl.grid(row=5, column=1)
    entry_pl.insert(0, "Hello, UDP!")
    def trimiteUDP_RTP():
        payload = entry_pl.get().encode()
        udp_dns_packet = IP(src=entry_s.get(), dst=entry_d.get()) / UDP(sport=int(entry_ps.get()), dport=int(entry_pd.get())) / payload
        for i in range(int(entry_nr.get())):
            send(udp_dns_packet)
        messagebox.showinfo("!!!", "Pachete transmise cu succes!")
    buttonUDP_RTP = ttk.Button(rootRTP, text="Trimite pachete", command=trimiteUDP_RTP)
    buttonUDP_RTP.grid(row=6, column=0)
def new_IP():
    rootIP = tkinter.Tk()
    rootIP.title("Selecteaza tipul de pachet IP")
    rootIP.geometry("350x100")
    rootIP.resizable(False, False)
    rootIP.columnconfigure(0, weight=1)
    rootIP.rowconfigure(0, weight=1)
    buttonIP = ttk.Button(rootIP, text="ICMP", command=features_ICMP)
    buttonIP.grid(row=0, column=0)


def new_TCP():
    rootTCP = tkinter.Tk()
    rootTCP.title("Selecteaza tipul de pachet TCP")
    rootTCP.geometry("350x100")
    rootTCP.resizable(False, False)
    rootTCP.columnconfigure(0, weight=1)
    rootTCP.rowconfigure(0, weight=1)
    buttonTCP_HTTP = ttk.Button(rootTCP, text="HTTP", command=features_HTTP)
    buttonTCP_HTTP.grid(row=0, column=0)
    buttonTCP_FTP = ttk.Button(rootTCP, text="FTP", command=features_FTP)
    buttonTCP_FTP.grid(row=1, column=0)

def new_UDP():
    rootUDP = tkinter.Tk()
    rootUDP.title("Selecteaza tipul de pachet UDP")
    rootUDP.geometry("350x100")
    rootUDP.resizable(False, False)
    rootUDP.columnconfigure(0, weight=1)
    rootUDP.rowconfigure(0, weight=1)
    buttonUDP_DNS = ttk.Button(rootUDP, text="DNS", command=features_DNS)
    buttonUDP_DNS.grid(row=0, column=0)
    buttonUDP_RTP = ttk.Button(rootUDP, text="RTP", command=features_RTP)
    buttonUDP_RTP.grid(row=1, column=0)


root = tkinter.Tk()
root.title("Generator de pachete")
packet_type_frame = ttk.LabelFrame(root, text="Tipul de pachete")
packet_type_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
buttonIP = ttk.Button(packet_type_frame, text="IP", command=new_IP)
buttonIP.grid(row=1, column=0, padx=10, pady=10)
buttonTCP = ttk.Button(packet_type_frame, text="TCP", command=new_TCP)
buttonTCP.grid(row=1, column=1, padx=10, pady=10)
buttonUDP = ttk.Button(packet_type_frame, text="UDP", command=new_UDP)
buttonUDP.grid(row=1, column=2, padx=10, pady=10)

root.mainloop()

