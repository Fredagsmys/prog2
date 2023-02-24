"""
Solutions to exam tasks for module M4
Name:
Code:
"""
import concurrent.futures as future

# A9
def get_balance(index):
    """This method opens customers.json and returns the field
    'balance' for the person with the given index.
    Leave this method as is.
    Note that '$' and ',' are removed from 'balance' in the jason file"""
    import json
    with open('customers.json') as f:
        data = json.load(f)
        return float(data[index]['balance'].replace('$', '').replace(',', ''))

def get_total_balance():
    """Method that runs get_balance in parallel for each index 0-111.
    The method should return the sum of all balances."""
    sum = 0
    customers = 112
    pro = []

    with future.ProcessPoolExecutor() as ex:
        for i in range(customers):
            pro.append(ex.submit(get_balance, i))
            sum += pro[i].result()
    return sum
    
# A10


def get_balance_gender(index):
    import json
    with open('customers.json') as f:
        data = json.load(f)
        return data[index]['gender'], float(data[index]['balance'].replace('$', '').replace(',', ''))

def get_mean_balances():
    """Method that return the mean balance for male and female customes. Gender 
    is set in the field 'gender' ('male' or 'female')"""
    sum_male = 0
    sum_female = 0
    females = 0
    males = 0
    ammount = 112
    for index in range(ammount):
        gender, balance = get_balance_gender(index)
        if gender == 'female':
            sum_female += balance
            females +=1
        else:
            sum_male += balance
            males+=1

    return [sum_male/males, sum_female/females]
    
# B4
def leapyears(years):

    return [year for year in years if year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)]



def main():
    print('Test of A9 ')
    print(get_total_balance())
    print('Test of A10 ')
    print(get_mean_balances())
    print('Test of B4 ')
    ly=leapyears(range(1900,2101))
    print(ly)
    if ly != None:
        print(len(ly))

if __name__ == "__main__":
    main()
    print('Over and out')
