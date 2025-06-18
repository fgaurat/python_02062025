import requests
from bs4 import BeautifulSoup

def main():
    url="https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_a = soup.find_all('a')

    all_logs = [a['href'].strip() for a in all_a if a['href'].endswith('.log')]

    for a in all_logs:
        full_url = f"{url}{a}"

        response = requests.get(full_url)
        with open(a,'w') as f:
            f.write(response.text)

    

if __name__=='__main__':
    main()
