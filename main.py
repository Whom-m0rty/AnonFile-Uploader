import requests, os, datetime, zipfile, shutil

def check_upload():
    list_dir_to_upload = os.listdir('./to_upload')
    return list_dir_to_upload

def open_output_file():
    now = datetime.datetime.now()
    moment = now.time()
    time = str(moment.hour) + '.' + str(moment.minute) + '.' + str(moment.second)
    output = open('output_'+ time + '_.txt', 'w')
    return output

def upload(output, list_dir_to_upload):
    for i in list_dir_to_upload:
        files = {
            'file': (i, open('./to_upload/' + i, 'rb'))
        }
        req = requests.post('https://api.anonfile.com/upload', files=files)
        print('\n')
        print(req.text)
        try:
            print(req.json()['status'])
            resp = req.json()['data']['file']['url']['short']
            print(resp)
            output.write(resp + '\n')
        except:
            print('Произошла ошибка! Возможно файл слишком большой для API')
    output.close()

def upload_zip(output):
    files = {
        'file': ('upload.zip', open('./upload.zip', 'rb'))
    }
    req = requests.post('https://api.anonfile.com/upload', files=files)
    print('\n')
    print(req.text)
    try:
        print(req.json()['status'])
        resp = req.json()['data']['file']['url']['short']
        output.write(resp + '\n')
        output.close()
    except:
        print('Произошла ошибка! Возможно файл слишком большой для API')
        output.close()
def zip_files():
    zip = zipfile.ZipFile('./upload.zip', 'w')
    for folder, subfolders, files in os.walk('./to_upload'):
        for file in files:
            zip.write(os.path.join(folder, file), file, compress_type=zipfile.ZIP_DEFLATED)

def printname():
    print("""
     _______  _        _______  _        _______ _________ _        _______ 
    (  ___  )( (    /|(  ___  )( (    /|(  ____ \\__   __/( \      (  ____ \\
    | (   ) ||  \  ( || (   ) ||  \  ( || (    \/   ) (   | (      | (    \/
    | (___) ||   \ | || |   | ||   \ | || (__       | |   | |      | (__    
    |  ___  || (\ \) || |   | || (\ \) ||  __)      | |   | |      |  __)   
    | (   ) || | \   || |   | || | \   || (         | |   | |      | (      
    | )   ( || )  \  || (___) || )  \  || )      ___) (___| (____/\| (____/\\
    |/     \||/    )_)(_______)|/    )_)|/       \_______/(_______/(_______/
                                                                            
              _______  _        _______  _______  ______   _______  _______ 
    |\     /|(  ____ )( \      (  ___  )(  ___  )(  __  \ (  ____ \(  ____ )
    | )   ( || (    )|| (      | (   ) || (   ) || (  \  )| (    \/| (    )|
    | |   | || (____)|| |      | |   | || (___) || |   ) || (__    | (____)|
    | |   | ||  _____)| |      | |   | ||  ___  || |   | ||  __)   |     __)
    | |   | || (      | |      | |   | || (   ) || |   ) || (      | (\ (   
    | (___) || )      | (____/\| (___) || )   ( || (__/  )| (____/\| ) \ \__
    (_______)|/       (_______/(_______)|/     \|(______/ (_______/|/   \__/
 
""")
def main():
    printname()
    listdir = os.listdir()
    if 'to_upload' not in listdir:
        os.mkdir('./to_upload')
    print("""
1. Отправить файлы из to_upload по отдельности.
2. Отправить файлы из to_upload одним архивом.
3. Очистить to_upload
4. Очистить файлы output

9. Поддержать разработчика.     

0. Выйти из программы.
    """)
    while True:
        inp = input("\nЧто сделать?: ")
        if inp == '1':
            output = open_output_file()
            list_dir_to_upload = check_upload()
            upload(output, list_dir_to_upload)
        if inp == '2':
            output = open_output_file()
            zip_files()
            upload_zip(output)
            os.remove('./upload.zip')
        if inp == '3':
            shutil.rmtree('./to_upload')
            os.mkdir('./to_upload')
        if inp == '4':
            list_file = os.listdir('./')
            for i in list_file:
                if 'output' in i:
                    os.remove('./' + i)
        if inp == '9':
            print('''
Qiwi: 8954082110
Lolzteam: https://lolzteam.org/members/110593/           
Буду рад любому рублю)            
''')
        if inp == '0':
            exit()

if __name__ == '__main__':
    main()
