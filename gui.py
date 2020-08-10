from PyQt5.QtWidgets import QApplication, QFileDialog

app = QApplication([])

def get_file_path():
    file = QFileDialog.getOpenFileName(None, 'Open file', '.','*.json')
    path = file[0]
    return path


def get_save_file_path():
    file = QFileDialog.getSaveFileName(None, 'Save file', '.', '*.png')
    path = file[0]
    return path





if __name__ == "__main__":
    pass