import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class peak_area_comparison(tk.Frame):
    def __init__(self, master):
        """
        コンストラクタ
        ・tk.Frameを継承
        ・フレームの配置、pltの初期設定
        """
        super().__init__(master)
        self.master = master
        self.master.title("ピーク面積比較ツール")

        # pyplotの初期設定
        plt.rcParams['font.family'] = 'Arial'
        # plt.rcParams['font.size'] = '20'
        plt.subplots_adjust(
            top=0.92,
            bottom=0.22,
            left=0.125,
            right=0.9,
            hspace=0.2,
            wspace=0.2
        )

        # フレームとボタンの作成
        self.graph_frame = self.create_graph_frame()
        # self.file_frame = self.create_file_frame()
        # self.option_button = tk.Button(
        #                         self.master, 
        #                         text = "オプション", 
        #                         command = self.option_button_command
        #                         )

        # 配置
        self.graph_frame.pack(fill=tk.BOTH, expand=True)
        # self.file_frame.pack()
        # self.option_button.pack()
        
    def create_graph_frame(self):
        graph_frame = tk.Frame(self.master)
        
        # matplotlibの描画領域の作成
        self.fig = plt.figure()
        # matplotlibの描画領域とウィジェット(Frame)の関連付け
        self.fig_canvas = FigureCanvasTkAgg(self.fig, graph_frame)
        # matplotlibのツールバーを作成
        self.toolbar = NavigationToolbar2Tk(self.fig_canvas, graph_frame)
        # matplotlibのグラフをフレームに配置
        self.fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        return graph_frame
    
root = tk.Tk()
app = peak_area_comparison(master=root)
app.mainloop()