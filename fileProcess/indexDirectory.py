def index(dir):
    for item in os.listdir(dir):
        # print(os.path.abspath(item))
        # if os.path.isfile(dir + '\\' + item):
        #     if item.endswith(".mp4") or item.endswith(".mkv"):
        #         if re.search('#', item):
        #             serialNum = re.findall('#\d+', item[:-34])

        #         if len(serialNum) > 0:
        #             with open('index.csv', 'a+') as fh:
        #                 record = f"{serialNum[-1]},  {item.replace(',', '-')} \n"
        #                 fh.write(record)

        # if os.path.isdir(item):
        # index(os.path.abspath(item))
        #     if re.match('^\d', item):
        #         pass
        #     else:
        #         serialNum = re.findall('\d+', item)

        #         if len(serialNum) > 0:
        #             # index(os.path.abspath(item))
        #             originalName = os.path.join(dir, item)
        #             newBasename = serialNum[-1] + ' ' + item
        #             newName = os.path.join(dir, newBasename)
        #             shutil.move(originalName, newName)

        if os.path.isdir(item):
            serialNum = re.findall('\d+', item)
            if len(serialNum) > 0:
                with open('index.csv', 'a+') as fh:
                    record = f"{serialNum[-1]},  {item.replace(',', '-')} \n"
                    fh.write(record)
