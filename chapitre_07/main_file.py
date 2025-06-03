
def main():
    # f = open("hello.txt","w")
    # f.write('Hello')
    # print(f.closed)
    # f.close()

    with open("hello.txt","w") as f:
        for i in range(10):
        # f.write('Hello')
            print(f'Hello {i}',file=f)

    with open("hello.txt","r") as f:
        # La totalité du fichier
        # all_file = f.read()
        # print(all_file)
        # all_lines = f.readlines()
        # lines = []
        # for line in all_lines:
        #     lines.append(line.strip())
        # # print(lines)

        # all_lines = f.readlines()
        # lines = [line.strip() for line in all_lines]
        for line in f:
            print(line.strip())

if __name__=='__main__':
    main()
