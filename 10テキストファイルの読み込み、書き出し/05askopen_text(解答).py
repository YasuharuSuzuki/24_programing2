
# 練習プログラム4 ファイルをダイアログで選ぶ (1.5点)

"""
- tkinkerモジュールを使用して、GUIで選択したファイルを読み込んで出力しましょう。
- サンプルプログラム1同様に、ファイルを開くにはopen()を、読み込みにはread()を、出力する時にはprint()を使用してみましょう。
"""

import tkinter as tk
import tkinter.filedialog as fd

# tkアプリウインドウを表示しない
root = tk.Tk()
root.withdraw()

# オープンダイアログを表示する
file_path = fd.askopenfilename(
   title = "ファイルを選んでください。",
   filetypes=[("TEXT", ".txt"), ("TEXT", ".py"), ("HTML", ".html")]
)

# 選択されたファイルパスからファイルを読み込んで出力する
if file_path:
    with open(file_path, "r", encoding="utf_8") as fileobj:    # ファイルを開く
        text = fileobj.read()    # ファイルを読み込む
        print(text)
