import time

localtime = time.localtime()
postname = time.strftime('%Y-%m-%d-%Y%m%d.md', localtime)
with open(postname, 'w') as f:
    content = '---\nlayout: post\ntitle: ""\ndescription: \ndate: {}\ncategories: 日记\n---'.format(time.strftime('%Y-%m-%d %H:%M:%S %z', localtime))
    f.write(content)
    print('[INFO] {} has been created!'.format(postname))
    print(content)
