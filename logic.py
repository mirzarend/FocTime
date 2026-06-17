import time

total_detik = 1500
reset = False

def mulai_timer(komponen_label) :
    global total_detik
    global reset
    if reset == False:

        reset = True

        while total_detik > 0 and reset == True:
        
            menit = total_detik//60

            detik = total_detik%60

            format_waktu = f"{menit:02d}:{detik:02d}"
            #02d agar angka yang ditampilkan selalu 2 digit 

            komponen_label.configure(text=format_waktu)

            time.sleep(1)

            total_detik -= 1

def reset_timer(komponen_label):
    global total_detik

    global reset

    reset = False
    total_detik = 1500
    komponen_label.configure(text="25:00")

def stop_timer(komponen_label):
    global total_detik
    global reset
    reset = False
