# Python using threading

This project is a simple application that demonstrates the use of threading and a graphical user interface (GUI) in Python (Copilot helped :)). The application consists of three main components: a main program logic that reacts to a button press and passes text from entry fields, a GUI that allows the user to interact with the application and functions that are executed. The buttons use flags and the entry fields a queue. Flags and Queues are thread-safe and provide a simple way to manage data exchange between threads. They handle synchronization internally.

Look also here: <https://www.weigu.lu/other_projects/python_coding/using_threading/index.html>


## Project Structure

```
threading
├── src
│   ├── main.py      # Entry point of the application
│   ├── functions.py # module with our functions
│   └── gui.py       # GUI module with a button
├── requirements.txt # Dependencies for the project
└── README.md        # Project documentation
```

## Requirements

To run this project, you need to install the required dependencies listed in `requirements.txt`. You can install them using pip:

```
pip install -r requirements.txt
```

The only requirement used is `tkinter`.

## Running the Application

1. Navigate to the project directory:

   ```
   cd threading
   ```

2. Run the main program:

   ```
   python src/main.py
   ```

3. A GUI window will appear with a button. Pressing the button will set the `button_pressed_flag` to true, triggering the main program logic.