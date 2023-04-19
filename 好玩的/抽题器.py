import random
import tkinter as tk

class RandomNumberGenerator:
    def __init__(self):
        self.numbers = list(range(1, 51))
        self.window = tk.Tk()
        self.window.geometry("400x200")
        self.window.title("第一关抽题器")

        self.button = tk.Button(
            self.window,
            text="生成随机数字",
            font=("华文琥珀", 16),
            bg="pink",
            fg="white",
            command=self.generate_random_number
        )
        self.button.pack(pady=20)

        self.text_box = tk.Text(
            self.window,
            height=3,
            width=8,
            font=("华文琥珀", 24),
            bg="pink",
            fg="white"
        )
        self.text_box.pack()

    def run(self):
        self.window.mainloop()

    def generate_random_number(self):
        if len(self.numbers) > 0:
            num = random.choice(self.numbers)
            self.numbers.remove(num)
            self.text_box.delete("1.0", tk.END)
            self.text_box.insert(tk.END, str(num))
        else:
            self.text_box.delete("1.0", tk.END)
            self.text_box.insert(tk.END, "end")

if __name__ == "__main__":
    rng = RandomNumberGenerator()
    rng.run()
