# My Python Project

This project is a simple application that demonstrates the use of threading and a graphical user interface (GUI) in Python. The application consists of two main components: a main program logic that reacts to a button press and a GUI that allows the user to interact with the application.

## Project Structure

```
my-python-project
├── src
│   ├── main.py      # Entry point of the application
│   └── gui.py       # GUI module with a button
├── requirements.txt  # Dependencies for the project
└── README.md        # Project documentation
```

## Requirements

To run this project, you need to install the required dependencies listed in `requirements.txt`. You can install them using pip:

```
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the project directory:

   ```
   cd my-python-project
   ```

2. Run the main program:

   ```
   python src/main.py
   ```

3. A GUI window will appear with a button. Pressing the button will set the `button_pressed_flag` to true, triggering the main program logic.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.