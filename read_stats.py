import PyPDF2
import re
import pandas as pd


class ReportReader:
    """Class to read raw report which is the output from the software (pdf)"""

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

        # print(stats_dict)
        for key, value in stats_dict.items():
            print(len(stats_dict[key]))
            # if len(stats_dict[key]) == 51:
            #     stats_dict[key].pop(len(stats_dict[key]) - 2)

            # print(stats_dict[key])
            # print(len(stats_dict[key]))
        print(stats_dict)
        return stats_dict


if __name__ == '__main__':
    r = ReportReader()
    f = r.read_software_report('Bochnia_stats.pdf')
    df = pd.DataFrame.from_dict(f, orient='index')
    df.to_excel('test.xlsx')