import os
import shutil

base_dir = os.getcwd()

for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)

    if os.path.isdir(folder_path):
        parts = folder.rsplit('_', 1)
        if len(parts) == 2:
            name_part = parts[0]
            downloaded_path = os.path.join(folder_path, 'downloaded')

            if os.path.isdir(downloaded_path):
                target_dir = os.path.join(base_dir, name_part)
                os.makedirs(target_dir, exist_ok=True)

                # 移动 downloaded 目录下的所有文件/文件夹
                for item in os.listdir(downloaded_path):
                    src_path = os.path.join(downloaded_path, item)
                    dest_path = os.path.join(target_dir, item)

                    if os.path.isfile(src_path):
                        shutil.move(src_path, dest_path)
                    elif os.path.isdir(src_path):
                        shutil.move(src_path, dest_path)

                # 删除原 {name}_{suffix} 目录
                shutil.rmtree(folder_path)
                print(f"已处理：{folder} -> {name_part}")

print("全部完成")
