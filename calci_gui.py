import tkinter as tk

color_digit = {
    'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4',
    'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'
}

multiplier = {
    'black': '1', 'brown': '10', 'red': '100', 'orange': '1k', 'yellow': '10k',
    'green': '100k', 'blue': '1M', 'violet': '10M', 'grey': '100M', 'white': '1G'
}

tolerance = {
    'brown': '+/- 1 %', 'red': '+/- 2 %', 'green': '+/- 0.5 %', 'blue': '+/- 0.25 %',
    'violet': '+/- 0.1 %', 'gold': '+/- 5 %', 'silver': '+/- 10 %', 'none': '+/- 20 %'
}

temperature_coefficient = {
    'brown': '100 ppm/K', 'red': '50 ppm/K', 'orange': '15 ppm/K',
    'yellow': '25 ppm/K', 'blue': '10 ppm/K'
}


# Function to find the resistance using color codes
def findResistance():
    a = color_var1.get()
    b = color_var2.get()
    c = color_var3.get() if num_bands.get() != "4 Bands" else None
    d = color_var4.get()
    e = color_var5.get() 
    f = color_var6.get() if num_bands.get() == "6 Bands" else None

    if a in color_digit and b in color_digit and d in multiplier and (c is None or c in color_digit) and (e in tolerance) and (f is None or f in temperature_coefficient):
        xx = color_digit.get(a)
        yy = color_digit.get(b)
        zz = color_digit.get(c) if c else ""
        aa = multiplier.get(d)
        bb = tolerance.get(e) 
        cc = temperature_coefficient.get(f) if f else ""
        
        if num_bands.get() == "4 Bands":
            resistance = xx + yy + " x " + aa + " ohms" + bb
        elif num_bands.get() == "5 Bands":
            resistance = xx + yy + zz + " x " + aa + " ohms" + bb
        else:
            resistance = xx + yy + zz + " x " + aa + " ohms" + bb + cc
        
        output_label.config(text="Resistance: " + resistance)

        # Update the background color of the color menus
        color_menu1.config(bg=a.lower())
        color_menu2.config(bg=b.lower())
        color_menu3.config(bg=c.lower()) if c else None
        color_menu4.config(bg=d.lower())
        color_menu5.config(bg=e.lower()) 
        color_menu6.config(bg=f.lower()) if f else None

    else:
        output_label.config(text="Invalid color selection!")

# Create the main window
window = tk.Tk()
window.title("Resistor Color Code Calculator")
window.geometry("300x300")

# Create the dropdown menu for number of bands
num_bands = tk.StringVar(window)
num_bands.set("4 Bands")

num_bands_menu = tk.OptionMenu(window, num_bands, "4 Bands", "5 Bands", "6 Bands")
num_bands_menu.config(width=20)
num_bands_menu.grid(row=0, column=1, padx=15, pady=10)

# Create the color selection menus
color_label1 = tk.Label(window, text="Band 1:")
color_label1.grid(row=1, column=0, padx=10, pady=5)
color_var1 = tk.StringVar(window)
color_var1.set("black")
color_menu1 = tk.OptionMenu(window, color_var1, *color_digit.keys())
color_menu1.config(width=10)
color_menu1.grid(row=1, column=1, padx=10, pady=5)

color_label2 = tk.Label(window, text="Band 2:")
color_label2.grid(row=2, column=0, padx=10, pady=5)
color_var2 = tk.StringVar(window)
color_var2.set("brown")
color_menu2 = tk.OptionMenu(window, color_var2, *color_digit.keys())
color_menu2.config(width=10)
color_menu2.grid(row=2, column=1, padx=10, pady=5)

color_label3 = tk.Label(window, text="Band 3:")
color_label3.grid(row=3, column=0, padx=10, pady=5)
color_var3 = tk.StringVar(window)
color_var3.set("red")
color_menu3 = tk.OptionMenu(window, color_var3, *color_digit.keys())
color_menu3.config(width=10)
color_menu3.grid(row=3, column=1, padx=10, pady=5)

color_label4 = tk.Label(window, text="Multiplier:")
color_label4.grid(row=4, column=0, padx=10, pady=5)
color_var4 = tk.StringVar(window)
color_var4.set("brown")
color_menu4 = tk.OptionMenu(window, color_var4, *multiplier.keys())
color_menu4.config(width=10)
color_menu4.grid(row=4, column=1, padx=10, pady=5)

color_label5 = tk.Label(window, text="Tolerance:")
color_label5.grid(row=5, column=0, padx=10, pady=5)
color_var5 = tk.StringVar(window)
color_var5.set("brown")
color_menu5 = tk.OptionMenu(window, color_var5, *tolerance.keys())
color_menu5.config(width=10)
color_menu5.grid(row=5, column=1, padx=10, pady=5)

color_label6 = tk.Label(window, text="Temp Coefficient:")
color_label6.grid(row=6, column=0, padx=10, pady=5)
color_var6 = tk.StringVar(window)
color_var6.set("brown")
color_menu6 = tk.OptionMenu(window, color_var6, *temperature_coefficient.keys())
color_menu6.config(width=10)
color_menu6.grid(row=6, column=1, padx=10, pady=5)

# Create the buttons
resistance_button = tk.Button(window, text="Calculate Resistance", command=findResistance)
resistance_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Create the output label
output_label = tk.Label(window, text="Resistance: ")
output_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

window.mainloop()
