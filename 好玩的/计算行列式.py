import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("行列式计算器")
        self.setGeometry(100, 100, 400, 400)

        # Create main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.grid_layout = QGridLayout(self.main_widget)

        # Create label and text box for matrix input
        self.matrix_label = QLabel("输入矩阵：")
        self.matrix_text_box = QTextEdit()
        self.grid_layout.addWidget(self.matrix_label, 0, 0)
        self.grid_layout.addWidget(self.matrix_text_box, 0, 1)

        # Create button to calculate determinant
        self.calculate_button = QPushButton("计算行列式")
        self.calculate_button.clicked.connect(self.calculate_determinant)
        self.grid_layout.addWidget(self.calculate_button, 1, 0)

        # Create label to display determinant
        self.result_label = QLabel("结果：")
        self.result_text_box = QTextEdit()
        self.result_text_box.setReadOnly(True)
        self.grid_layout.addWidget(self.result_label, 2, 0)
        self.grid_layout.addWidget(self.result_text_box, 2, 1)

    def calculate_determinant(self):
        # Get matrix input from text box
        matrix_str = self.matrix_text_box.toPlainText()
        matrix_list = matrix_str.split("\n")

        # Convert input to list of lists of floats
        matrix = []
        for row_str in matrix_list:
            row_str = row_str.strip()
            if row_str:
                row = [float(x) for x in row_str.split()]
                matrix.append(row)

        # Calculate determinant and display result
        result = determinant(matrix)
        self.result_text_box.setText(str(result))

def determinant(matrix):
    # Base case for 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case for larger matrices
    result = 0
    for i in range(len(matrix)):
        sub_matrix = matrix[1:]
        for j in range(len(sub_matrix)):
            sub_matrix[j] = sub_matrix[j][:i] + sub_matrix[j][i+1:]
        sub_determinant = determinant(sub_matrix)
        sign = (-1) ** i
        result += sign * matrix[0][i] * sub_determinant

    return result

if __name__ == "__main__":
    # Create application and window
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Run application
    sys.exit(app.exec_())
