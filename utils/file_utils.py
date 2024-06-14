import pandas as pd

def list_of_becodian() -> list [str]:
    '''create a list based on the name from the excel file'''
    
    excel = pd.read_excel('Example Excel Template.xlsx')
    becodians = excel['Colleagues'].to_list()
    return becodians


