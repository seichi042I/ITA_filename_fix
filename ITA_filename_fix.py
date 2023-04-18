import sys
import re
import os
import subprocess
from pathlib import Path
import multiprocessing
from tqdm import tqdm


def process_file(filepath):
    correct_pattern = r"(RECITATION324|EMOTION100)_\d{3}.wav"
    name = filepath.name
    stem = filepath.stem
    match = re.match(correct_pattern, filepath.name)
    # print(multiprocessing.current_process().name)
    if match:
        return
    else:
        match = re.match(r"[A-z0-9]*_[0-9]*",name)
        if match:
            number = int(stem.split('_')[1])
        else:
            number = int(re.findall(r'\d+', name)[-1])
        
        match = re.match(r"r.*$",name)
        if match:
            # recitation
            new_name = f"RECITATION324_{number:03d}.wav"
        else:
            # emotion
            new_name = f"EMOTION100_{number:03d}.wav"
            
        os.rename(str(filepath),str(filepath.with_name(new_name)))

def main():
    # forループでファイルを順番に表示するBashコマンド
    args = sys.argv
    if len(args) != 2:
        exit(1)
    print(args[1])
    
    command = f'find {args[1]} -name "*.wav"| sort'

    # コマンドを実行する
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)

    # 実行結果を表示する
    filepaths = result.stdout.decode().split('\n')[:-1]
    filepaths = [Path(f) for f in filepaths]
    
    # 最大で3つのプロセスを使用してファイルを処理する
    with multiprocessing.Pool(processes=8) as pool:
        # ファイルを処理する関数を並列実行する
        async_result = pool.map_async(process_file, tqdm(filepaths))
        async_result.wait()
    # 処理結果を表示する
    result = async_result.get()
    # print(result)

if __name__ == "__main__":
    main()
