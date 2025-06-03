
def main():
    all_data = [
    {
        "id": 1,
        "first_name": "Georgena",
        "last_name": "Huison",
        "email": "ghuison0@howstuffworks.com",
        "gender": "Genderqueer",
        "ip_address": "46.100.156.215"
    },
    {
        "id": 2,
        "first_name": "Ardelia",
        "last_name": "Andre",
        "email": "aandre1@pen.io",
        "gender": "Female",
        "ip_address": "207.206.244.110"
    }]

    p = all_data[0]
    print(p)
    print(p.values())
    print(p.keys())

    # p['last_name']

    # for d in l:
    #     print(d['last_name'])
if __name__=='__main__':
    main()
