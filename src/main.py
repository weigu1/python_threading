import threading
import time
import queue
from gui import start_gui
from functions import MyFunctions

def main_loop(flags, myfunc, text_queues):
    """ Main loop that checks if any flag is set """
    while True:
        if flags[0].is_set():
            myfunc.function_1()
            flags[0].clear()
        if flags[1].is_set():
            myfunc.function_2()
            flags[1].clear()
        if flags[2].is_set():
            myfunc.function_3()
            flags[2].clear()
        for i, text_queue in enumerate(text_queues): # Check for text in the queues
            try:
                text = text_queue.get_nowait()
                print(f"Received text from queue {i + 1}: {text}")
                # Here you can add code to handle the text
            except queue.Empty:
                pass        
        time.sleep(0.1)

if __name__ == "__main__":    
    flag1 = threading.Event()   # Create Event objects to signal between threads
    flag2 = threading.Event()
    flag3 = threading.Event()
    flags = [flag1, flag2, flag3]
    myfunc = MyFunctions()      # Create an instance of MyFunctions
    text_queue1 = queue.Queue() # Create queues for text
    text_queue2 = queue.Queue()
    text_queues = [text_queue1, text_queue2]    
    gui_thread = threading.Thread(target=start_gui,     # Create GUI thread
                                  args=(flags, text_queues))
    main_thread = threading.Thread(target=main_loop,    # Create main_loop thread
                                   args=(flags, myfunc, text_queues))
    gui_thread.start()        # Start both threads
    main_thread.start()    
    gui_thread.join()         # Wait for both threads to complete
    main_thread.join()