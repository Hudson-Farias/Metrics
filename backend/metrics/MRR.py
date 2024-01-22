from pandas import DataFrame, to_datetime
from datetime import datetime

class MRR:
    columns_checked = True

    def __init__(self, dataframe: DataFrame):
        self.dataframe = dataframe
        self.__check_columns()


    def __check_columns(self):
        required_columns = ['data início', 'valor', 'cobrada a cada X dias', 'quantidade cobranças']
        self.columns_checked = all(column in self.dataframe.columns for column in required_columns)


    def calc(self):
        self.__set_start_date_infos()
        self.__set_monthly_fee_amount()

        payload = {}

        for index, row in self.dataframe.iterrows():
            year = row['ano início']
            month = row['mes início']
            amount_charges = row['quantidade cobranças']

            for _ in range(month, month + amount_charges):
                if month == 13:
                    month = 1
                    year += 1

                key = f'{month}/{year}'

                if key not in payload: payload[key] = 0.0

                payload[key] += row['valor mensal']
                payload[key] = round(payload[key], 2)

                month += 1

        payload = dict(sorted(payload.items(), key = lambda item: datetime.strptime(item[0], '%m/%Y')))
        return payload
            

    def __set_start_date_infos(self):
        datetime = to_datetime(self.dataframe['data início'], format = '%m/%d/%y %H:%M')

        self.dataframe['ano início'] = datetime.dt.year
        self.dataframe['mes início'] = datetime.dt.month


    def __set_monthly_fee_amount(self):
        self.dataframe['valor'] = self.dataframe['valor'].astype(str)
        self.dataframe['valor'] = self.dataframe['valor'].str.replace(',', '.').astype(float)

        self.dataframe['valor mensal'] = self.dataframe.apply(lambda row: round(row['valor'] if row['cobrada a cada X dias'] == 30 else row['valor'] / 12, 2), axis=1)
