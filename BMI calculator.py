from tkinter import *
from tkinter import ttk

def bmi():
    try:
        Height = float(h.get())
        Weight = float(w.get())
        m = Height / 100
        B = round(float(Weight / m ** 2), 1)
        label.config(text=B)

        if B <= 18.5:
            label1.config(text="Underweight", fg="#3498db")
        elif 18.5 < B <= 25:
            label1.config(text="Normal", fg="#2ecc71")
        elif 25 < B <= 30:
            label1.config(text="Overweight", fg="#f39c12")
        else:
            label1.config(text="Health is at risk!\n Need to lose", fg="#e74c3c")

    except ValueError:
        label.config(text="Invalid input", fg="#e74c3c")
        label1.config(text="Please enter valid numbers", fg="#e74c3c")

root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.config(bg="#F0F0F0")

top = Label(root, text="BMI CALCULATOR", font=("Arial", 25, "bold"), width=25, bd=5, bg="#3498db", fg="white")
top.place(x=0, y=0)

Label(root, width=72, height=18, bg="#F0F0F0").pack(side="bottom")

Label(root, text="Height (in cm):", font=("Arial", 12), bg="#F0F0F0").place(x=20, y=100)
h = Entry(root, width=5, font=("Arial", 20), bg="#ecf0f1", fg="#34495e", bd=0, justify="center")
h.place(x=160, y=90)

Label(root, text="Weight (in kg):", font=("Arial", 12), bg="#F0F0F0").place(x=20, y=160)
w = Entry(root, width=5, font=("Arial", 20), bg="#ecf0f1", fg="#34495e", bd=0, justify="center")
w.place(x=160, y=150)

slider_h = ttk.Scale(root, from_=0, to=220, orient="horizontal", style="TScale")
slider_h.place(x=80, y=250)
slider_h.bind("<Motion>", lambda event: h.delete(0, END) or h.insert(0, str(slider_h.get())))

slider_w = ttk.Scale(root, from_=0, to=200, orient="horizontal", style="TScale")
slider_w.place(x=300, y=250)
slider_w.bind("<Motion>", lambda event: w.delete(0, END) or w.insert(0, str(slider_w.get())))

Button(root, text="Report", width=15, height=2, font=("Arial", 10, "bold"), bg="#3498db", fg="white", command=bmi).place(x=200, y=340)

label = Label(root, font=("Arial", 30, "bold"), bg="#F0F0F0", fg="#34495e")
label.place(x=350, y=450)

label1 = Label(root, font=("Arial", 10, "bold"), bg="#F0F0F0", fg="#34495e", width=50)
label1.place(x=20, y=500)

root.mainloop()
