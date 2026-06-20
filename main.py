import customtkinter
import logic
import threading
import quotes

#Windows
app = customtkinter.CTk()
app.after(0, lambda: app.state("zoomed"))
app.geometry("600x500")
app.title("FocTime")

#Label Judul
label = customtkinter.CTkLabel(app, text="Foctime", fg_color="transparent", font=("Georgia", 30, "bold"))
label.pack(pady=20)

#Label Timer
label_timer = customtkinter.CTkLabel(app, text="25:00", fg_color="transparent", font=("Gill Sans", 70, "bold"))
label_timer.pack()

#Button start
button_start = customtkinter.CTkButton(app, text="Start", font=("Gill Sans", 20, "bold"), hover=True, fg_color="Blue", hover_color="#00008B", command=lambda: threading.Thread(target=logic.mulai_timer, args=(label_timer,)).start())
button_start.pack(pady=20)

#Button Reset
button_reset =customtkinter.CTkButton(app, text="Reset", font=("Gill Sans", 20, "bold"), hover=True, hover_color="#8B0000", fg_color="Red", command=lambda: logic.reset_timer(label_timer))
button_reset.pack(pady = 0)

#Button Stop
button_stop = customtkinter.CTkButton(app, text="Stop", fg_color="orange", hover=True, hover_color="#FF8C00", font=("Gill Sans", 20, "bold"), command=lambda: logic.stop_timer(label_timer))
button_stop.pack(pady = 10)

# label Quotes
quotes = quotes.random_quotes()

label_quotes = customtkinter.CTkLabel(app, text=quotes, fg_color="transparent", font=("Gill Sans", 20, "bold"), text_color="White", wraplength=500)
label_quotes.pack(pady = 20)

app.mainloop()