import PyPDF2
import re
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
import os


class ReportReader:
    """Class to read raw report which is the output from the software (pdf)"""
    df_data = None
    df_data_raw = None

    def read_software_report(self, pdf_document):
        """
        Read first page of report from software and transform all data into dictionary:
        key: name, value: list of stats.
        """
        s = open(pdf_document, 'rb')
        read_pdf = PyPDF2.PdfFileReader(s)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        data_list = page_content.splitlines()
        # print(data_list)
        # title = data_list[1]
        data_list = data_list[2:]
        # print(data_list)
        # print(title)
        stats_dict = {}
        temp_stat_list = []
        temp_name = ''

        # handle all players except last one (search by string name not numbers
        # different logic for goalkeepers - see output software file
        for elem in data_list:
            if re.match(r"[a-zA-ZąćęłńóśźżĄĘŁŃÓŚŹŻ]", elem):
                if temp_name:
                    if temp_name in stats_dict:
                        if len(temp_stat_list) > len(stats_dict[temp_name]):
                            list_to_add = stats_dict[temp_name]
                            temp_stat_list.pop(len(temp_stat_list) - 1)
                            temp_stat_list.append(data_list[data_list.index(temp_name) - 1])
                            stats_dict[temp_name] = temp_stat_list

                            for elem_to_add in list_to_add:
                                stats_dict[temp_name].append(elem_to_add)
                    else:
                        temp_stat_list.pop(len(temp_stat_list) - 1)
                        stats_dict[temp_name] = temp_stat_list
                        temp_stat_list.append(data_list[data_list.index(temp_name) - 1])
                temp_name = elem
                temp_stat_list = []
            else:
                temp_stat_list.append(elem)

        # print(len(temp_stat_list))
        # last player - have to be limited to 50 or 56 stats (goalkeeper)
        if len(temp_stat_list) > 49:
            if temp_stat_list[10] == '--':
                temp_stat_list = temp_stat_list[:54]
            else:
                temp_stat_list = temp_stat_list[:50]
        if temp_name in stats_dict:
            if len(temp_stat_list) > len(stats_dict[temp_name]):
                list_to_add = stats_dict[temp_name]
                temp_stat_list.pop(len(temp_stat_list) - 1)
                temp_stat_list.append(data_list[data_list.index(temp_name) - 1])
                stats_dict[temp_name] = temp_stat_list

                for elem_to_add in list_to_add:
                    stats_dict[temp_name].append(elem_to_add)
        else:
            temp_stat_list.pop(len(temp_stat_list) - 1)
            stats_dict[temp_name] = temp_stat_list
            temp_stat_list.append(data_list[data_list.index(temp_name) - 1])

        # print(len(temp_stat_list))
        # print(temp_stat_list)
        # print(temp_name)

        # print(stats_dict)
        # for key, value in stats_dict.items():
        #     print(len(stats_dict[key]))
        # print(stats_dict)
        return stats_dict

    def convert_to_df(self, dict_data):
        self.df_data = pd.DataFrame.from_dict(dict_data, orient='index')
        self.df_data = self.df_data.apply(lambda x: x.str.replace(',', '.'))
        self.df_data = self.df_data.apply(lambda x: x.str.replace('--', 'nan'))
        self.df_data = self.df_data.astype(float)

    def transform_data(self):
        """
        Add column and calculations to get the output (see constant.py)
        :return:
        """
        # Add column to differ goalkeepers
        self.df_data.loc[pd.isna(self.df_data[55]), 'Player_Position'] = 'PL'
        self.df_data.loc[pd.isna(self.df_data['Player_Position']), 'Player_Position'] = 'GK'

        # p1 column 8 + 9 + 10 + 11 + 12 + 17
        self.df_data['p1'] = \
            self.df_data[8] + self.df_data[9] + self.df_data[10] + self.df_data[11] + self.df_data[12] + \
            self.df_data[17]

        # p2 column 18 + 19 + 20 + 21 + 22 + 27
        self.df_data['p2'] = \
            self.df_data[18] + self.df_data[19] + self.df_data[20] + self.df_data[21] + self.df_data[22] + \
            self.df_data[27]

        # s1 column 13 + 14 + 15
        self.df_data['s1'] = self.df_data[13] + self.df_data[14] + self.df_data[15]

        # s2 column 23 + 24 + 25
        self.df_data['s2'] = self.df_data[23] + self.df_data[24] + self.df_data[25]

        # k1 column 16
        self.df_data['k1'] = self.df_data[16]

        # k2 column 26
        self.df_data['k2'] = self.df_data[26]

        # k2 gk column 30
        self.df_data['k2gk'] = self.df_data[30]

        # b1 column 35 + 36 + 37 + 38 + 39
        self.df_data['b1'] = \
            self.df_data[35] + self.df_data[36] + self.df_data[37] + self.df_data[38] + self.df_data[39]

        # b2 column 40
        self.df_data['b2'] = self.df_data[40]

        # g1 column 2
        self.df_data['g1'] = self.df_data[6]

        # g2 column 3
        self.df_data['g2'] = self.df_data[7]

        # r column 29
        self.df_data['r'] = self.df_data[29]

        # c1 column 46
        self.df_data['c1'] = self.df_data[46]

        # ANu p1 + p2 + s1 + s2 + k1 + k2 + b1 + b2
        self.df_data['ANu'] = \
            self.df_data['p1'] + self.df_data['p2'] + self.df_data['s1'] + self.df_data['s2'] + self.df_data['k1'] + \
            self.df_data['k2'] + self.df_data['b1'] + self.df_data['b2']

        # PAt_l (left) p1 + p2
        self.df_data['PAt_l'] = self.df_data['p1'] + self.df_data['p2']

        # PAt_r (right) p1
        self.df_data['PAt_r'] = self.df_data['p1']

        # PAt - string PAt_l "/" PAt_r
        self.df_data['PAt'] = self.df_data[self.df_data.notnull()].apply(lambda x: (str(int(x.PAt_l)) + "/" + str(int(x.PAt_r))) if(np.all(pd.notnull(x.PAt_l))) else None, axis=1)

        # FAt_l (left) s1 + s2
        self.df_data['FAt_l'] = self.df_data['s1'] + self.df_data['s2']

        # FAt_r (right) s1
        self.df_data['FAt_r'] = self.df_data['s1']

        # FAt - string FAt_l "/" FAt_r
        self.df_data['FAt'] = self.df_data.apply(lambda x: (str(int(x.FAt_l)) + "/" + str(int(x.FAt_r))) if(np.all(pd.notnull(x.FAt_r))) else None, axis=1)

        # Psh_l (left) k1 + k2
        self.df_data['Psh_l'] = self.df_data['k1'] + self.df_data['k2']

        # PSh_r (right) k1
        self.df_data['PSh_r'] = self.df_data['k1']

        # PSh - string Psh_l "/" PSh_r
        self.df_data['PSh'] = self.df_data.apply(lambda x: (str(int(x.Psh_l)) + "/" + str(int(x.PSh_r))) if(np.all(pd.notnull(x.Psh_l))) else None, axis=1)

        # Err_l (left) b1 + b2
        self.df_data['Err_l'] = self.df_data['b1'] + self.df_data['b2']

        # Err_r (right) b2
        self.df_data['Err_r'] = self.df_data['b2']

        # Err - string Err_l "/" Err_r
        self.df_data['Err'] = self.df_data.apply(lambda x: (str(int(x.Err_l)) + "/" + str(int(x.Err_r))) if(np.all(pd.notnull(x.Err_l))) else None, axis=1)

        # Go p1 + s1 + k1
        self.df_data['Go'] = self.df_data['p1'] + self.df_data['s1'] + self.df_data['k1']

        # Gk_l (left) g1 - g2
        self.df_data['Gk_l'] = self.df_data['g1'] - self.df_data['g2']

        # Gk_r (right) k2
        self.df_data['Gk_r'] = self.df_data['k2gk']

        # Gk - string Gk_l "/" Gk_r
        self.df_data['Gk'] = self.df_data.apply(lambda x: (str(int(x.Gk_l)) + "/" + str(int(x.Gk_r))) if(np.all(pd.notnull(x.Gk_l))) else None, axis=1)

        # PShCr r
        self.df_data['PShCr'] = self.df_data['r']

        # Pen c1
        self.df_data['Pen'] = self.df_data['c1']

        # EffTot - string Go "/" ANu
        self.df_data['EffTot'] = self.df_data.apply(lambda x: (str(int(x.Go)) + "/" + str(int(x.ANu))) if(np.all(pd.notnull(x.Go))) else None, axis=1)
        self.df_data['EffTot%'] = round(self.df_data['Go'].divide(self.df_data['ANu']) * 100, 2)

        # EffTotGk - string Go "/" ANu
        self.df_data['EffTot%Gk_l'] = self.df_data['Gk_l']
        self.df_data['EffTot%Gk'] = round(self.df_data['EffTot%Gk_l'].divide(self.df_data['g1']) * 100, 2)

    def format_data(self):
        self.df_data.loc[self.df_data['Player_Position'] == 'GK', ['ANu', 'PAt', 'FAt', 'PSh', 'Err', 'Go', 'PShCr',
                                                                   'EffTot', 'EffTot%']] = np.nan
        self.df_data.loc[self.df_data['Player_Position'] == 'PL', ['Gk', 'EffTot%Gk']] = np.nan
        # export + gui
        self.df_data['Zawodnik'] = self.df_data.index
        self.df_data_raw = self.df_data
        self.df_data = self.df_data[['Zawodnik', 'ANu', 'PAt', 'FAt', 'PSh', 'Err', 'Go', 'Gk', 'Pen', 'PShCr', 'EffTot%', 'EffTot%Gk']]


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    file_name = askopenfilename(title="Select pdf file with stats", filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    r = ReportReader()
    f = r.read_software_report(file_name)
    r.convert_to_df(f)
    r.transform_data()
    r.format_data()
    print(r.df_data)
    path_to_save = askdirectory(title="Choose folder to save the result")
    r.df_data.to_excel(os.path.join(path_to_save, 'Statystyki.xlsx'), index=False)
    root.deiconify()
    root.destroy()
