import csv


def read_csv(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        header = next(reader)
        for row in  reader:
            iterable = list(zip(header, row))
            country_dict = {key: value for key, value in iterable}
            print(country_dict)            

            
if __name__ == '__main__':
    read_csv('./data.csv')
                    