import threading
import time
import queue
from gui import start_gui
from functions import MyFunctions

def main_loop(flags_2_main, myfunc, queues_2_main, queues_2_gui):
    """ Main loop that checks if any flag is set """
    while not flags_2_main[3].is_set():  # Check the exit flag
        if flags_2_main[0].is_set():
            myfunc.function_1()
            flags_2_main[0].clear()
            queues_2_gui.put("Function 1 in main executed")
        if flags_2_main[1].is_set():
            myfunc.function_2()
            flags_2_main[1].clear()
            queues_2_gui.put("Function 2 in main executed")
        if flags_2_main[2].is_set():
            myfunc.function_3()
            flags_2_main[2].clear()
            queues_2_gui.put("Function 3 in main executed")
        for i, text_queue in enumerate(queues_2_main): # Check for text in the queues
            try:
                text = text_queue.get_nowait()
                print(f"Received text from gui queue {i + 1}: {text}")
                queues_2_gui.put(f"Received text from main queue {i + 1}: {text}")
                # Here you can add code to handle the text
            except queue.Empty:
                pass        
        time.sleep(0.1)

def main():
    flag_b1 = threading.Event()   # Create Event objects to signal between threads
    flag_b2 = threading.Event()
    flag_b3 = threading.Event()
    flag_exit = threading.Event()   # Exit flag
    flags_2_main = [flag_b1, flag_b2, flag_b3, flag_exit]
    myfunc = MyFunctions()      # Create an instance of MyFunctions
    queue_2_main = queue.Queue() # Create queues for text
    text_queue2 = queue.Queue()
    queues_2_main = [text_queue1, text_queue2]
    queues_2_gui = queue.Queue()   # Create a queue for communication from main_loop to GUI
    
    gui_thread = threading.Thread(target=start_gui,     # Create GUI thread
                                  args=(flags_2_main, queues_2_main, queues_2_gui))
    main_thread = threading.Thread(target=main_loop,    # Create main_loop thread
                                   args=(flags_2_main, myfunc, queues_2_main, queues_2_gui))
    gui_thread.start()        # Start both threads
    main_thread.start()    
    gui_thread.join()         # Wait for both threads to complete
    main_thread.join()

if __name__ == "__main__":
    main()
