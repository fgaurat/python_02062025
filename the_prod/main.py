import requests

def main():
    r = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = r.json()

    print(data[0]['title'])

if __name__=='__main__':
    main()
