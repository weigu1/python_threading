

class MyFunctions:
    def __init__(self, queue_2_gui):
        self.queue_2_gui = queue_2_gui

    def function_1(self):        
        text = "Function 1 executed, text transported in queues_2_gui"
        self.queue_2_gui.put(text)
        

    def function_2(self):
        text = "Function 2 executed, text transported in queues_2_gui"
        self.queue_2_gui.put(text)

    def function_3(self):
        text = "Function 3 executed, text transported in queues_2_gui"
        self.queue_2_gui.put(text)
