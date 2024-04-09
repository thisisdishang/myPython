import tkinter as tk

# Create a tkinter window
root = tk.Tk()
root.title("Cat Face")

# Create a canvas widget
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Draw the cat's face
canvas.create_oval(50, 50, 150, 150, outline="black", fill="white")  # Head
canvas.create_oval(80, 80, 95, 95, outline="black",
                   fill="black")     # Left eye
canvas.create_oval(105, 80, 120, 95, outline="black",
                   fill="black")    # Right eye
canvas.create_arc(75, 90, 125, 130, start=0, extent=-
                  180, outline="black")  # Mouth

# Draw the cat's ears
canvas.create_polygon(75, 75, 50, 100, 70, 50,
                      outline="black", fill="white")  # Left ear
canvas.create_polygon(125, 75, 150, 100, 130, 50,
                      outline="black", fill="white")  # Right ear

# Run the tkinter event loop
root.mainloop()
