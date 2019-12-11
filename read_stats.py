import PyPDF2
import re
import pandas as pd
import numpy as np


class ReportReader:
    """Class to read raw report which is the output from the software (pdf)"""
    df_data = None

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
        title = data_list[1]
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
        print(stats_dict)
        return stats_dict

    def convert_to_df(self, dict_data):
        self.df_data = pd.DataFrame.from_dict(dict_data, orient='index')
        self.df_data = self.df_data.apply(lambda x: x.str.replace(',', '.'))
        self.df_data = self.df_data.apply(lambda x: x.str.replace('--', 'nan'))
        self.df_data = self.df_data.astype(float)

    def tranform_data(self):
        self.df_data.loc[pd.isna(self.df_data[55]), 'Player_Position'] = 'PL'
        self.df_data.loc[pd.isna(self.df_data['Player_Position']), 'Player_Position'] = 'GK'


if __name__ == '__main__':
    r = ReportReader()
    f = r.read_software_report('Politechnika.pdf')
    r.convert_to_df(f)
    r.df_data.to_excel('test.xlsx')
