# this script calculates saturation water pressure

from math import e
import tkinter as tk


def buck(t):
    # t - temperature in C
    # calculate saturation VP based on
    # Buck equation, source - wiki
    a, b, c = 0.61094, 17.625, 243.04
    return round(10 * a * e**(b * t / (t + c)), 3)


def antoine(t):
    # t - temperature in C
    # calculate saturation VP based on
    # Antoine equation, source - wiki
    if 1 <= t <= 99:
        A, B, C = 8.07131, 1730.63, 233.426
    elif 100 <= t <= 374:
        A, B, C = 8.14019, 1810.94, 244.485
    else:
        return 'Out of temperature range'
    return round(10 ** (A - B / (C + t)) * 1.333, 3)
    
    
def change_ps(*args):
    # updates pressure labels
    try:
        p_s = buck(float(T.get()))
        p_need = p_s * float(RH.get()) / 100
        pressure.configure(text=f'Saturated water pressure, mBar: {p_s}')
        RH_label.configure(text=f'Pressure to rich given RH, mBar: {round(p_need, 3)}')
    except ValueError:
        pressure.configure(text=f'Saturated water pressure, mBar:')
        RH_label.configure(text=f'Pressure to rich given RH, mBar:')


# create app window
window = tk.Tk()
window.geometry('300x150')

# create pressure label
pressure = tk.Label(text=f'Saturated water vapor pressure, mBar: ')
pressure.pack()

# create RH label
RH_label = tk.Label(text='Pressure to rich given RH, mBar:')
RH_label.pack()

# request temperature
T = tk.StringVar()
tk.Label(text='Temperature, °C').pack()
tk.Entry(window, textvariable=T).pack()

# request RH
RH = tk.StringVar()
tk.Label(text='Required RH, %').pack()
RH_entry = tk.Entry(window, textvariable=RH)
RH_entry.pack()
RH_entry.insert(0, string='100') # 100% relative humidity set by default

# trace changes in temperature and RH
T.trace('w', change_ps)
RH.trace('w', change_ps)

# show window
window.mainloop()