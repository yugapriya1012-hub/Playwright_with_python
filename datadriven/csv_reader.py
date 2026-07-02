import csv

def get_login_data():
    data=[]
    with open("login_data.csv",newline="") as file:
        reader=csv.DictReader(file)

        for row in reader:
            data.append(row)
        return data
    
print(get_login_data())