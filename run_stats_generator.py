import sys
from stats_generator_gui import Ui_MainWindow
from read_stats import *
from PySide2.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assign_widgets()
        self.show()
        self.report = ReportReader()
        self.file_name_input = ''
        self.path_to_save_output = ''
        self.output_file_name = ''

    def assign_widgets(self):
        self.pushButton_Input_File.clicked.connect(self.select_input_file)
        self.pushButton_Output_Folder.clicked.connect(self.select_output_folder)
        self.pushButton_generate.clicked.connect(self.generate_output)

    def select_input_file(self):
        self.file_name_input = askopenfilename(title="Select pdf file with stats",
                                          filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
        self.label_Input_File.setText(self.file_name_input)

    def select_output_folder(self):
        self.path_to_save_output = askdirectory(title="Choose folder to save the result")
        self.label_Output_Folder.setText(self.path_to_save_output)

    def generate_output(self):
        # print(self.label_Input_File.text())
        # print(self.textEdit_Output_File_Name.toPlainText())
        # print(self.label_Output_Folder.text())
        if self.label_Input_File.text() == '':
            print('Select input file!')
        else:
            if self.label_Output_Folder.text() == '':
                self.path_to_save_output = os.getcwd()
            else:
                if self.textEdit_Output_File_Name.toPlainText() != '':
                    self.output_file_name = self.textEdit_Output_File_Name.toPlainText()
                else:
                    self.output_file_name = os.path.splitext(self.file_name_input)[0]
                    print(f'Generating output with default name: {self.output_file_name}.xlsx')
                f_rep = self.report.read_software_report(self.label_Input_File.text())
                self.report.convert_to_df(f_rep)
                self.report.transform_data()
                self.report.format_data()
                # print(r.df_data)
                # print(os.path.join(self.path_to_save_output, self.output_file_name + "." + 'xlsx'))
                self.report.df_data.to_excel(
                    os.path.join(self.path_to_save_output, self.output_file_name + "." + 'xlsx'), index=False)
                print('Done! Close application.')
                sys.exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    root = tk.Tk()
    root.withdraw()
    sys.exit(app.exec_())

