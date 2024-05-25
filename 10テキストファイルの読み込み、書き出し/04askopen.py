
# サンプルプログラム4 ファイルをダイアログで選ぶ

"""
- tkinkerモジュールを使用して、開くファイルをGUIで選ぶことが出来ます
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

# ファイルが選択されたらファイルパス名を出力する
if file_path:
    print(file_path) # ファイルパスを表示する
