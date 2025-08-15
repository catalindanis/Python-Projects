import pandas as pd

def main():
    dataframe1 = pd.read_excel('Order_PM.xlsx', 'Event_Log')
    dataframe2 = pd.read_excel('Order_PM.xlsx', 'Activity_Descriptions')

    print(dataframe1)
    print(dataframe2)

if __name__ == '__main__':
    main()
