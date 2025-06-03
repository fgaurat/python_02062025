import json

def main():
    csv_file = "MOCK_DATA.csv"
    json_file = "MOCK_DATA_2.json"

    final_data = []
    with open(csv_file) as f:
        all_data = [line.strip() for line in f.readlines()]

    header = all_data[0].split(';')
    data = all_data[1:]
    for line in data:
        item = line.split(';')
        d = dict(zip(header,item))
        final_data.append(d)
    
    with open(json_file,'w') as f:
        json.dump(final_data,f,indent=4)

        
        
        
        
    



if __name__=='__main__':
    main()
