from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

class InputWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create widgets
        url_label = QLabel('Enter URL:')
        self.url_input = QLineEdit()
        submit_button = QPushButton('Submit')

        # Create layouts
        input_layout = QHBoxLayout()
        input_layout.addWidget(url_label)
        input_layout.addWidget(self.url_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(submit_button)

        # Set layout for the main window
        self.setLayout(main_layout)

        # Connect the submit button to a function
        submit_button.clicked.connect(self.on_submit_clicked)
        self.url_input.returnPressed.connect(self.on_submit_clicked)

        # Set window properties
        self.setWindowTitle('URL Input Window')
        self.setGeometry(100, 100, 400, 200)

    def on_submit_clicked(self):
        # Retrieve the entered URL
        entered_url = self.url_input.text()

        # You can perform actions with the entered URL here
        # For now, let's just print it
        print('Entered URL:', entered_url)
