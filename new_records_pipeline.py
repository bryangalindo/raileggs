from datetime import datetime
import string

import pandas


def get_house_bill_df(file):
    df = pandas.read_excel(file, header=None)
    index_to_leave = [1, 2, 4, 6, 7, 12, 18, 29, 30, 32, 40, 42, 43, 54]

    for index, row in df.iteritems():
        if index not in index_to_leave:
            del df[index]

    df.columns = ['Date Created', 'HBL', 'Customer',
                  'CI Reference', 'MBL', 'HBL T/R', 'Move Type',
                  'Loading Port', 'Final Destination', 'Operator',
                  'Overseas Agent', 'Consignee', 'Notify Party', 'Discharge Port']
    return df


def get_containers_df(file):
    df = pandas.read_excel(file, header=None, usecols='A,C')
    df.columns = ['Containers', 'CI Reference']
    return df


def transform_containers_df(df):
    return df.fillna('').groupby(['CI Reference'])['Containers'].apply(', '.join).reset_index(drop=True)


def transform_house_bill_df(df):
    df['Operator'] = df['Operator'].str.upper()
    df['HBL T/R'] = df['HBL T/R'].apply(lambda x: 1 if 'Express' in x else None)
    df['Consignee'] = df['Customer'].str.translate(str.maketrans('', '', string.punctuation))
    df['Notify Party'] = df['Notify Party'].str.translate(str.maketrans('', '', string.punctuation))
    df['Trucking'] = pandas.np.where(df['Move Type'] == 'CY/DOOR', 'Pending', 'N/A')
    df['SOC G/L'] = pandas.np.where(df['CI Reference'].str[-1] == '^', 'Pending', 'N/A')
    df['Payment'] = 'Pending'
    df = df.loc[df['Operator'] == 'BRYAN']
    df = df.loc[df['Date Created'] == datetime.today().strftime('%Y-%m-%d 00:00:00')]
    df['Status'] = 'On Vessel'
    return df


def join_dataframes(df1, df2):
    return pandas.concat([df1, df2], axis=1, join='inner')


if __name__ == '__main__':
    df1 = transform_house_bill_df(get_house_bill_df())
    df2 = transform_containers_df(get_containers_df())
    df3 = join_dataframes(df1, df2)
    df3.to_csv('{}_new_records.csv'.format(datetime.today().strftime('%m%d%Y')), index=False)
