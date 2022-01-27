import json


def main():
    datas = []
    with open('example.txt', 'r') as f:
        sub_datas = []
        for line in f.readlines():
            if not line.startswith('<'):
                items = line.strip()[:-1].split("=")
                sub_datas.append({
                    items[0]: items[1]
                })
            elif line.startswith('<SUBEND'):
                datas.append(sub_datas)
                sub_datas = []

    print(json.dumps(datas, indent=4))


if __name__ == '__main__':
    main()
