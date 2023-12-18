import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import torch
import seaborn as sns
import matplotlib.pyplot as plt

def open_image():

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:
        image = Image.open(file_path)
        image = ImageTk.PhotoImage(image)

        root = tk.Tk()
        root.title("Image Viewer")

        label = tk.Label(root, image=image)
        label.image = image
        label.pack()

        button_exit = tk.Button(root, text="Exit", command=root.destroy)
        button_exit.pack()

        root.mainloop()

def generate_and_display_plot():
  

  
    sns.lineplot(x=range(len(torch_tensor)), y=torch_tensor.numpy())
    plt.title('Seaborn Plot of Torch Tensor')
    plt.show()

def main():
    open_image()
    generate_and_display_plot()

if __name__ == '__main__':
    main()
