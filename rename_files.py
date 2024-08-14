import os
import choose_dir
import csv

csv_path = os.path.join(os.getcwd(), 'names.csv')

if not os.path.exists(csv_path):
    # 如果 CSV 文件不存在，創建一個空的 CSV 文件並寫入標題
    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Filepath", "Fullpath or . or select"])
        writer.writerow(["Origin", "New"])
    print(f"CSV file created at {csv_path} with headers.")
else:
    # 讀取 CSV 文件
    with open(csv_path, 'r') as file:
        reader = list(csv.reader(file))

        # 打印讀取到的內容以確認
        print("CSV Content:", reader)
        
        # 提取 path_option
        path_option = reader[0][1]  # 第二列的值
        
        files = []
        newNames = []
        
        # 讀取文件和新名稱
        for row in reader[2:]:
            if len(row) == 2:
                files.append(row[0])
                newNames.append(row[1])
            else:
                print("Row does not contain enough columns:", row)
    
    print("Files:", files)
    print("New Names:", newNames)

    # 根據 path_option 選擇文件夾
    if path_option == ".":
        folderPath = os.getcwd()
    elif path_option == "select":
        # 讓用戶選擇目錄
        folderPath = choose_dir.tkinter_dir_select()
    else:
        folderPath = path_option

    # 打印選擇的文件夾路徑
    print(f"Selected folder: {folderPath}")

    # 檢查文件夾是否存在
    if os.path.isdir(folderPath):
        # 切換到指定目錄
        os.chdir(folderPath)
        
        for file in files:
            if not os.path.isfile(file):
                print(f"File not found: {file}")
                continue  # 如果文件不存在，則跳過該文件

        # 重命名文件
        for i in range(len(files)):
            old_file = files[i]
            new_file = newNames[i]
            
            if os.path.isfile(old_file):
                os.rename(old_file, new_file)
                print(f"Renamed {old_file} to {new_file}")
            else:
                print(f"File not found for renaming: {old_file}")

    else:
        print(f"Directory not found: {folderPath}")