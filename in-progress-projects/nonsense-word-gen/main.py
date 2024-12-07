import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
from nwg_ui import Ui_MainWindow  # Import the UI blueprint
from gen import Sounds  # Import your word generation class

# This is your actual window class that implements the functionality
class MainWindow(QMainWindow):
    def __init__(self):
        # Initialize the main window
        super(MainWindow, self).__init__()
        
        # Create an instance of the UI blueprint
        self.ui = Ui_MainWindow()
        # Use the blueprint to set up this window
        self.ui.setupUi(self)
        
        # Create an instance of your word generator
        self.sounds = Sounds()
        
        # Set up the scroll area where generated words will appear
        # We need a widget and layout to organize the words vertically
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.ui.generated_words.setWidget(self.scroll_widget)
        self.ui.generated_words.setWidgetResizable(True)
        
        # Set up the dropdown box with word pattern options
        self.ui.soundsBox.clear()
        self.sound_options = ["cv", "vc", "ccv", "vcc", "cvc", "ccvc", "cvcc", "ccvcc"]
        self.ui.soundsBox.addItems([option.upper() for option in self.sound_options])
        
        # Set up the number input (spin box) with reasonable limits
        self.ui.words_number.setMinimum(1)
        self.ui.words_number.setMaximum(100)
        self.ui.words_number.setValue(10)
        
        # Connect the generate button to our generate_words function
        # This means when the button is clicked, generate_words will run
        self.ui.generate_button.clicked.connect(self.generate_words)
        
    def generate_words(self):
        # Clear any previously generated words from the scroll area
        for i in reversed(range(self.scroll_layout.count())): 
            self.scroll_layout.itemAt(i).widget().setParent(None)
        
        # Get all the settings from the UI elements
        # This replaces the input() calls from your original script
        sound_type = self.sound_options[self.ui.soundsBox.currentIndex()]  # Which pattern (cv, cvc, etc.)
        use_digs = self.ui.include_digs.isChecked()  # Include digraphs?
        use_dips = self.ui.include_dips.isChecked()  # Include diphthongs?
        use_qpk = self.ui.include_qpk.isChecked()   # Include qu, ph, kn?
        use_teams = self.ui.checkBox.isChecked()    # Include vowel teams?
        num_words = self.ui.words_number.value()    # How many words to generate
        
        # Get the right method from your Sounds class based on the pattern
        # This is like choosing between sounds.cv(), sounds.cvc(), etc.
        method = getattr(self.sounds, sound_type)
        
        # Generate the requested number of words
        for _ in range(num_words):
            # Generate one word using your existing methods
            word = method(use_dips, use_teams, use_digs, use_qpk)
            # Create a label to display the word
            label = QLabel(word)
            label.setFont(self.ui.generated_words.font())
            # Add the word to the scroll area
            self.scroll_layout.addWidget(label)

# This is the standard way to start a Qt application
if __name__ == '__main__':
    # Create the application
    app = QApplication(sys.argv)
    # Create and show the window
    window = MainWindow()
    window.show()
    # Start the application and keep it running
    sys.exit(app.exec())