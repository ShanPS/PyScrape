# imports
import requests
from bs4 import BeautifulSoup


# variables
deg_name = 'B.Tech'
semester = '1&2'
month = 'May'
year = '2015'
result_type = 'Regular',
date_time = '2018/01/30+01:46:40.019+GMT+0530'


# function to get the result for a given reg. number
def getResult(regNum):
    url = "http://exam.cusat.ac.in/erp5/cusat/CUSAT-RESULT/Result_Declaration/display_sup_result"
    formData = {'regno': str(regNum),
                'deg_name': deg_name,
                'semester': semester,
                'month': month,
                'year': year,
                'result_type': result_type,
                'date_time': date_time
                }
    request = requests.post(url, formData)
    soup = BeautifulSoup(request.text, 'lxml')

    elements = []
    for e in soup.select("td"):
        elements.append(e.text.strip())
    return elements

# set of reg numbers to fetch the result.
regNums = [12150000, 12150076, 12150002, 12150003, 12150004, 12150005,
           12150006, 12150077, 12150008, 12150009, 12150010, 12150011,
           12150012, 12150013, 12150078, 12150014, 12150015, 12150016,
           12150017, 12150018, 12150020, 12150079, 12150021, 12150022,
           12150023, 12150024, 12150080, 12150025, 12150026, 12150027,
           12150028, 12150029, 12150081, 12150030, 12150082, 12150031,
           12150032, 12150033, 12150034, 12150083, 12150035, 12150036,
           12150037, 12150038, 12150039, 12150040, 12150041, 12150042,
           12150043, 12150044]

# open the file and write the results fetched into it.
with open('S1S2_results.csv', 'w') as file:
    # header --> subjects
    file.write('REG NO,NAME,MATHS-I,PHYSICS,CHEMISTRY,MECHANICS,GRAPHICS,BME,BEE,\
        CP,EVS/TCN,E&M WORKSHOP,CP LAB,LANGUAGE LAB\n')
    for num in regNums:
        print('getting results for RegNum:', num)
        result = getResult(num)
        # write regNum and Name
        file.write(result[0] + ',' + result[1] + ',')
        # write marks for subjects
        for j in range(10, 55, 4):
            file.write(result[j] + ',')
        file.write('\n')
    print('done')
