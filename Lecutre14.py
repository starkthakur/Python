def get_gender(sex='Unknown'):
    if sex == 'm':
        sex = 'Male'
    elif sex == 'f':
        sex = 'Female'
    print("print gender is", sex)


get_gender('m')
get_gender('f')
get_gender()
