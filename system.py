import datetime
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit, QLineEdit, QVBoxLayout, QWidget, QMessageBox, QMenuBar, QAction
from PyQt5.QtGui import QPalette, QColor, QBrush, QPixmap, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit, QLineEdit, QVBoxLayout, QWidget, QMessageBox, QProgressBar

class DailyRiseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Daily Rise")

        # Defina o ícone da janela (usando PNG, JPG ou GIF)
        icon_path = 'foto_icone.png'  # Pode ser PNG, JPG ou GIF
        self.setWindowIcon(QIcon(icon_path))

        self.setWindowTitle("Daily Rise")
        self.setGeometry(100, 100, 640, 480)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.header_label = QLabel("Bem-vindo ao Daily Rise!")
        self.layout.addWidget(self.header_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.layout.addWidget(self.progress_bar)

        self.progress_bar_label = QLabel("Progressão de nível:")
        self.layout.addWidget(self.progress_bar_label)

        self.view_quests_button = QPushButton("Ver missões atuais")
        self.view_quests_button.clicked.connect(self.view_current_quests)
        self.layout.addWidget(self.view_quests_button)

        self.view_completed_quests_button = QPushButton("Ver missões completas")
        self.view_completed_quests_button.clicked.connect(self.view_completed_quests)
        self.layout.addWidget(self.view_completed_quests_button)

        self.xp = self.load_xp('xp.txt')
        self.level = self.load_level('level_user.txt')

        self.xp_label = QLabel(f"Seu XP atual: {self.xp}")
        self.layout.addWidget(self.xp_label)

        self.level_label = QLabel(f"Seu nível atual: {self.level}")
        self.layout.addWidget(self.level_label)

        self.new_quest_entry = QLineEdit()
        self.layout.addWidget(self.new_quest_entry)

        self.add_quest_button = QPushButton("Adicionar missão")
        self.add_quest_button.clicked.connect(self.add_quest)
        self.layout.addWidget(self.add_quest_button)

        self.complete_quest_entry = QLineEdit()
        self.layout.addWidget(self.complete_quest_entry)

        self.complete_quest_button = QPushButton("Marcar missão como completa")
        self.complete_quest_button.clicked.connect(self.complete_quest)
        self.layout.addWidget(self.complete_quest_button)

        self.quests_text = QTextEdit()
        self.quests_text.setReadOnly(True)
        self.layout.addWidget(self.quests_text)

        self.completed_quests_text = QTextEdit()
        self.completed_quests_text.setReadOnly(True)
        self.layout.addWidget(self.completed_quests_text)

        self.central_widget.setLayout(self.layout)
        self.view_progress()
        self.set_background()

        # Defina um menu
        menubar = self.menuBar()
        file_menu = menubar.addMenu('Menu')
        exit_action = QAction('Sair', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def load_xp(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def load_level(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def view_current_quests(self):
        with open('quests.txt', 'r') as file:
            quests = file.readlines()
        self.quests_text.clear()
        self.quests_text.append("MISSÕES ATUAIS:")
        for idx, quest in enumerate(quests):
            self.quests_text.append(f"{idx + 1}. {quest.strip()}")

    def view_completed_quests(self):
        with open('completed_quests.txt', 'r') as file:
            completed_quests = file.readlines()
        self.completed_quests_text.clear()
        self.completed_quests_text.append("MISSÕES COMPLETAS:")
        for quest in completed_quests:
            self.completed_quests_text.append(quest.strip())

    def view_progress(self):
        level_progress = self.xp % 50
        self.progress_bar.setValue(level_progress)
        self.progress_bar_label.setText(f"Progressão de nível: {'#' * level_progress}{'-' * (50 - level_progress)}")

    def add_quest(self):
        new_quest = self.new_quest_entry.text()
        if new_quest and new_quest != "DIGITE SUA MISSÃO AQUI":
            with open('quests.txt', 'a') as file:
                file.write(new_quest + '\n')
            self.new_quest_entry.clear()
            self.view_current_quests()
        else:
            QMessageBox.warning(self, "Erro", "Digite uma missão válida.")

    def complete_quest(self):
        self.view_current_quests()
        try:
            quest_number = int(self.complete_quest_entry.text()) - 1
        except ValueError:
            QMessageBox.warning(self, "Erro", "Digite um número válido.")
            return
        quests = []
        with open('quests.txt', 'r') as file:
            quests = file.readlines()
        if quest_number < len(quests):
            quest_completed = quests.pop(quest_number)
            with open('quests.txt', 'w') as file:
                file.writelines(quests)
            with open('completed_quests.txt', 'a') as file:
                completion_date = datetime.date.today()
                file.write(f"{quest_completed.strip()} - Concluída em: {completion_date}\n")
            self.xp += 25
            with open('xp.txt', 'w') as file:
                file.write(str(self.xp))
            if self.xp >= 50:
                self.xp -= 50
                self.level += 1
                with open('level_user.txt', 'w') as file:
                    file.write(str(self.level))
            self.view_progress()
            self.complete_quest_entry.clear()
            self.view_current_quests()
            self.view_completed_quests()
            self.xp_label.setText(f"Seu XP atual: {self.xp}")
            self.level_label.setText(f"Seu nível atual: {self.level}")

    def set_background(self):
        palette = QPalette()
        gradient = QBrush(QColor(173, 216, 230), Qt.SolidPattern)  # Light Blue color
        palette.setBrush(QPalette.Window, gradient)
        self.setPalette(palette)

def main():
    app = QApplication(sys.argv)
    window = DailyRiseApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
