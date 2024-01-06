import tkinter as tk
from tkinter import colorchooser

class PaintingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Painting App")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.setup_menu()

        self.draw_color = "black"
        self.line_width = 2

        self.prev_x = None
        self.prev_y = None

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def setup_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear Canvas", command=self.clear_canvas)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)

        color_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Color", menu=color_menu)
        color_menu.add_command(label="Choose Color", command=self.choose_color)

    def paint(self, event):
        x, y = event.x, event.y

        if self.prev_x and self.prev_y:
            self.canvas.create_line(self.prev_x, self.prev_y, x, y, width=self.line_width, fill=self.draw_color)

        self.prev_x = x
        self.prev_y = y

    def reset(self, event):
        self.prev_x = None
        self.prev_y = None

    def clear_canvas(self):
        self.canvas.delete("all")

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.draw_color = color

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintingApp(root)
    root.mainloop()
