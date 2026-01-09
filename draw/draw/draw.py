import tkinter as tk

root = tk.Tk()
root.title("Arizona")

canvas = tk.Canvas(root, width=800, height=500, bg="lightyellow")
canvas.pack()

# Horizon line
canvas.create_line(0, 400, 800, 400, fill="sienna", width=3)

# Simple mountains
canvas.create_line(0, 400, 150, 250, fill="brown", width=3)
canvas.create_line(150, 250, 300, 400, fill="brown", width=3)
canvas.create_line(300, 400, 500, 300, fill="brown", width=3)
canvas.create_line(500, 300, 800, 400, fill="brown", width=3)

# Simple cactus (made of straight lines)
# Main stem
canvas.create_line(150, 400, 150, 300, fill="green", width=5)
# Left arm
canvas.create_line(150, 340, 130, 340, fill="green", width=5)
canvas.create_line(130, 340, 130, 360, fill="green", width=5)
# Right arm
canvas.create_line(150, 320, 170, 320, fill="green", width=5)
canvas.create_line(170, 320, 170, 340, fill="green", width=5)

root.mainloop()
