def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100-age)+(apples_ate*3.5)+(cigs_smoked*2)
    print(answer)


buckys_data = [27, 20, 0, 8, 5]
x_data = [25, 30, 10]
health_calculator(buckys_data[0], buckys_data[1], buckys_data[4])
health_calculator(x_data[0], x_data[1], x_data[2])

# An easier approach for unpacking the dataset but we have esnure that array and function dataset is same i.e.3 in this case

# health_calculator(*buckys_data)
health_calculator(*x_data)
