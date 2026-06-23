import customtkinter
import logic
import threading
import quotes

#Fungsi Pindah Menu
def timer():
    halaman_stats.pack_forget()
    halaman_timer.pack(expand=True)

def stats():
    halaman_timer.pack_forget()
    halaman_stats.pack(expand=True)

#Windows
app = customtkinter.CTk()
app.after(0, lambda: app.state("zoomed"))
app.geometry("600x500")
app.title("FocTime")

#Logo
app.iconbitmap("img/icon.ico")

#Sidebar
sidebar = customtkinter.CTkFrame(app, fg_color="#1E1E1E", width=300)
sidebar.pack_propagate(False)
sidebar.pack(side="left", fill="y")

#Label Judul
label = customtkinter.CTkLabel(sidebar, text="Foctime", fg_color="transparent", font=("Georgia", 30, "bold"))
label.pack(pady=20)

#Menu Timer
menu_timer = customtkinter.CTkButton(sidebar, text="Menu Timer", anchor="w" ,font=("Gill Sans", 20, "bold"), fg_color="#2C2C2C", hover=True, hover_color="#3A3A3A", command=timer)
menu_timer.pack(fill="x", padx=20)

#Menu Stats
menu_stats = customtkinter.CTkButton(sidebar, text="Menu Stats", anchor="w" ,font=("Gill Sans", 20, "bold"), fg_color="#2C2C2C", hover=True, hover_color="#3A3A3A", command=stats)
menu_stats.pack(fill="x", padx=20, pady= 10)

#Content - Main
content = customtkinter.CTkFrame(app, fg_color="#121212")
content.pack(side="right", fill="both", expand=True)

#Content 1 - Halaman Timer
halaman_timer = customtkinter.CTkFrame(content, fg_color="transparent")
halaman_timer.pack(expand=True)

#Content 1 - Label Timer
label_timer = customtkinter.CTkLabel(halaman_timer, text="25:00", fg_color="transparent", font=("Gill Sans", 70, "bold"))
label_timer.pack()

#Content 1 - Button start
button_start = customtkinter.CTkButton(halaman_timer, text="Start", font=("Gill Sans", 20, "bold"), hover=True, fg_color="Blue", hover_color="#00008B", command=lambda: threading.Thread(target=logic.mulai_timer, args=(label_timer,)).start())
button_start.pack(pady=20)

#Content 1 - Button Reset
button_reset =customtkinter.CTkButton(halaman_timer, text="Reset", font=("Gill Sans", 20, "bold"), hover=True, hover_color="#8B0000", fg_color="Red", command=lambda: logic.reset_timer(label_timer))
button_reset.pack(pady = 0)

#Content 1 - Button Stop
button_stop = customtkinter.CTkButton(halaman_timer, text="Stop", fg_color="orange", hover=True, hover_color="#FF8C00", font=("Gill Sans", 20, "bold"), command=lambda: logic.stop_timer(label_timer))
button_stop.pack(pady = 10)

#Content 1 - label Quotes
quotes = quotes.random_quotes()
label_quotes = customtkinter.CTkLabel(halaman_timer, text=quotes, fg_color="transparent", font=("Gill Sans", 20, "bold"), text_color="White", wraplength=500)
label_quotes.pack(pady = 20)

#Content 2 - Halaman Stats
halaman_stats = customtkinter.CTkFrame(content, fg_color="transparent")

#Content 2 - Label Stats
label_stats = customtkinter.CTkLabel(halaman_stats, text="Sedang dalam pengerjaan!", fg_color="transparent", font=("Gill Sans", 30, "bold"), text_color="red")
label_stats.pack(pady=50)

app.mainloop()