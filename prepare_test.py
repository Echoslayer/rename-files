import os

def create_dir(directory, exist_ok=False):
    """創建目錄，如果目錄已存在，則根據 exist_ok 參數決定是否拋出異常。"""
    os.makedirs(directory, exist_ok=exist_ok)
    print(f"Directory created: {directory}")

def clear(directory):
    """清空指定目錄中的所有文件。"""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted file: {file_path}")

def create_file(directory, files):
    """在指定目錄中創建文件。"""
    for file in files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'w') as f:
            f.write('')  # 創建空文件
            print(f"Created file: {file_path}")

test_dir = r"/Users/xieweizhe/Desktop/MacCode/rename-files/test_folder"

# 創建目錄
create_dir(test_dir, exist_ok=True)

# 檢查目錄是否為空
if len(os.listdir(test_dir)) > 0:
    clear(test_dir)

# 創建文件
create_file(directory=test_dir, files=["i4.png", "i5.png", "i6.png", "i7.png", "i8.png", "i9.png"])