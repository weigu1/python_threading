import tkinter as tk
import queue

class GUI:
    def __init__(self, flags, text_queues):
        self.flags = flags
        self.text_queues = text_queues
        self.root = tk.Tk()
        self.root.title("Simple GUI using threading")        
        self.button_texts_dict = { # Dictionary for button texts (button:message)
                                  "Press Me 1 ": "Button 1 was pressed!",
                                  "Press Me 2" : "Button 2 was pressed!",
                                  "Press Me 3" : "Button 2 was pressed!",
                                  "Submit 1" : "Hello",
                                  "Submit 2" : "Do it now!"}
        self.button_texts_list = list(self.button_texts_dict.keys())
        print(self.button_texts_list)
        self.button1 = tk.Button(self.root,                        # Button 1
                                 text=self.button_texts_list[0],
                                 command=lambda: self.set_flag(self.flags[0],
                                 self.button_texts_dict[self.button_texts_list[0]]))
        self.button1.pack(pady=10)
        self.button2 = tk.Button(self.root,                        # Button 2
                                 text=self.button_texts_list[1],
                                 command=lambda: self.set_flag(self.flags[1],
                                 self.button_texts_dict[self.button_texts_list[1]]))
        self.button2.pack(pady=10)
        self.button3 = tk.Button(self.root,                        # Button 3
                                 text=self.button_texts_list[2],
                                 command=lambda: self.set_flag(self.flags[2],
                                 self.button_texts_dict[self.button_texts_list[2]]))
        self.button3.pack(pady=10)
        self.text_window = tk.Text(self.root, height=10, width=30) # Text window
        self.text_window.pack(pady=20)
        
        self.entry1 = tk.Entry(self.root)                          # Entry window 1
        self.entry1.insert(0, self.button_texts_dict[self.button_texts_list[3]])
        self.entry1.pack(pady=10)
        self.submit_button1 = tk.Button(self.root,
                                        text=self.button_texts_list[3],
                                        command=lambda: self.submit_text(0))
        self.submit_button1.pack(pady=10)

        self.entry2 = tk.Entry(self.root)                          # Entry window 2
        self.entry2.insert(0, self.button_texts_dict[self.button_texts_list[4]])
        self.entry2.pack(pady=10)
        self.submit_button2 = tk.Button(self.root,
                                        text=self.button_texts_list[4],
                                        command=lambda: self.submit_text(1))
        self.submit_button2.pack(pady=10)

    def set_flag(self, flag, message):
        flag.set()
        self.text_window.insert(tk.END, message + "\n")

    def submit_text(self, queue_index):
        if queue_index == 0:
            text = self.entry1.get()
        else:
            text = self.entry2.get()
        self.text_window.insert(tk.END, f"Entry {queue_index + 1} submitted: " + text + "\n")
        self.text_queues[queue_index].put(text)  # Add the text to the appropriate queue

    def run(self):
        self.root.mainloop()

def start_gui(flags, text_queues):
    gui = GUI(flags, text_queues)
    gui.run()