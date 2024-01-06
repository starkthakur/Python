from urllib import request

goog_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv"


def download_address_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()


download_address_data(goog_url)

