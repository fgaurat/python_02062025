import json 
from pprint import pprint
def main():
    json_file = "MOCK_DATA.json"
    csv_file = "MOCK_DATA.csv"
    
    # with open(json_file,"r") as f:
    with open(json_file) as f:
        all_data = json.load(f)
    
    headers = all_data[0].keys()
    # pprint(all_data)
    print(headers)
    
    with open(csv_file,"w") as f:
    # id; first_name; last_name; email; gender; ip_address
        print(*headers, file=f,sep=";")
        for data in all_data:
            values = [str(d) for d in list(data.values())]
            # print(*values, file=f,sep=";")
            l = ";".join(values)
            f.write(l+"\n")



if __name__=='__main__':
    main()
