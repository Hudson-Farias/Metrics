from pandas import DataFrame, to_datetime
from datetime import datetime

class ChurnRate:
    columns_checked = True

    def __init__(self, dataframe: DataFrame):
        self.dataframe = dataframe
        self.__check_columns()


    def __check_columns(self):
        required_columns = ['data início', 'data cancelamento', 'status']
        self.columns_checked = all(column in self.dataframe.columns for column in required_columns)


    def calc(self):
        self.__set_start_date_infos()
        self.__set_cancel_date_infos()

        df = self.dataframe

        payload = {}
        years = self.dataframe['ano início'].unique().tolist()
        years.sort()

        for year in years:
            months = self.dataframe['mes início'].unique().tolist()
            months.sort()

            for month in months:                
                canceled_customers = df[
                    (df['status'] == 'Cancelada') &
                    (df['ano cancelamento'] == year) & 
                    (df['mes cancelamento'] == month)
                ]

                canceled_customers_count = canceled_customers.shape[0]

                total_customers = df[
                    ((df['ano cancelamento'] <= year)  | df['ano cancelamento'].isna()) &
                    ((df['mes cancelamento'] <= month) | df['mes cancelamento'].isna())
                ].shape[0]

                payload[f'{month}/{year}'] = round(canceled_customers_count / total_customers * 100, 1)

                df = df.drop(canceled_customers.index)

        payload = dict(sorted(payload.items(), key = lambda item: datetime.strptime(item[0], '%m/%Y')))
        return payload
            

    def __set_start_date_infos(self):
        datetime = to_datetime(self.dataframe['data início'], format = '%m/%d/%y %H:%M')

        self.dataframe['ano início'] = datetime.dt.year
        self.dataframe['mes início'] = datetime.dt.month


    def __set_cancel_date_infos(self):
        datetime = to_datetime(self.dataframe['data cancelamento'], format='%m/%d/%y %H:%M')

        self.dataframe['ano cancelamento'] = datetime.dt.year.fillna(0).astype(int)
        self.dataframe['mes cancelamento'] = datetime.dt.month.fillna(0).astype(int)

        self.dataframe = self.dataframe.sort_values(by = ['ano cancelamento', 'mes cancelamento'])

