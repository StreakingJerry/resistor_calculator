"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""

from tkinter import *
from tkinter.ttk import *


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.res_e_series = StringVar(value=24)
        self.res_compose_type = StringVar(value=1)

        self.__win()
        self.tk_tabs_lhbmo7q9 = self.__tk_tabs_lhbmo7q9(self)
        self.tk_frame_lzziu5kh = self.__tk_frame_lzziu5kh(self.tk_tabs_lhbmo7q9_0)
        self.tk_frame_lzzj8k9u = self.__tk_frame_lzzj8k9u(self.tk_frame_lzziu5kh)
        self.tk_label_lhbmtl8h = self.__tk_label_lhbmtl8h(self.tk_frame_lzzj8k9u)
        self.tk_input_lhbmtn25 = self.__tk_input_lhbmtn25(self.tk_frame_lzzj8k9u)
        self.tk_label_lhbmtpxy = self.__tk_label_lhbmtpxy(self.tk_frame_lzzj8k9u)
        self.tk_label_lhbmvt01 = self.__tk_label_lhbmvt01(self.tk_frame_lzzj8k9u)
        self.tk_input_lhbmurrf = self.__tk_input_lhbmurrf(self.tk_frame_lzzj8k9u)
        self.tk_label_lhbmtras = self.__tk_label_lhbmtras(self.tk_frame_lzzj8k9u)
        self.tk_label_lhbmwcfd = self.__tk_label_lhbmwcfd(self.tk_frame_lzzj8k9u)
        self.tk_input_lhbmwkar = self.__tk_input_lhbmwkar(self.tk_frame_lzzj8k9u)
        self.tk_label_lhbmz319 = self.__tk_label_lhbmz319(self.tk_frame_lzzj8k9u)
        self.tk_input_lhbmwujp = self.__tk_input_lhbmwujp(self.tk_frame_lzzj8k9u)
        self.tk_label_lhbmycfz = self.__tk_label_lhbmycfz(self.tk_frame_lzzj8k9u)
        self.tk_label_lhbmzk5h = self.__tk_label_lhbmzk5h(self.tk_frame_lzzj8k9u)
        self.tk_button_lhbn5n3b = self.__tk_button_lhbn5n3b(self.tk_frame_lzziu5kh)
        self.tk_table_lhbn5jnk = self.__tk_table_lhbn5jnk(self.tk_frame_lzziu5kh)
        self.tk_frame_lzzkcgdj = self.__tk_frame_lzzkcgdj(self.tk_tabs_lhbmo7q9_1)
        self.tk_label_lhbn81re = self.__tk_label_lhbn81re(self.tk_frame_lzzkcgdj)
        self.tk_label_lhbn763h = self.__tk_label_lhbn763h(self.tk_frame_lzzkcgdj)
        self.tk_input_lhbn7or6 = self.__tk_input_lhbn7or6(self.tk_frame_lzzkcgdj)
        self.tk_label_frame_lhbn9t2y = self.__tk_label_frame_lhbn9t2y(
            self.tk_tabs_lhbmo7q9_1
        )
        self.tk_radio_button_lhbn9vxx = self.__tk_radio_button_lhbn9vxx(
            self.tk_label_frame_lhbn9t2y
        )
        self.tk_radio_button_lhbn9xmo = self.__tk_radio_button_lhbn9xmo(
            self.tk_label_frame_lhbn9t2y
        )
        self.tk_radio_button_lhbn9z6i = self.__tk_radio_button_lhbn9z6i(
            self.tk_label_frame_lhbn9t2y
        )
        self.tk_frame_lhbnbkh6 = self.__tk_frame_lhbnbkh6(self.tk_tabs_lhbmo7q9_1)
        self.tk_label_lhbnbuja = self.__tk_label_lhbnbuja(self.tk_frame_lhbnbkh6)
        self.tk_input_lhbnc1sa = self.__tk_input_lhbnc1sa(self.tk_frame_lhbnbkh6)
        self.tk_label_lhbnc2y3 = self.__tk_label_lhbnc2y3(self.tk_frame_lhbnbkh6)
        self.tk_label_lhbnclao = self.__tk_label_lhbnclao(self.tk_frame_lhbnbkh6)
        self.tk_input_lhbncnhk = self.__tk_input_lhbncnhk(self.tk_frame_lhbnbkh6)
        self.tk_label_lhbncqal = self.__tk_label_lhbncqal(self.tk_frame_lhbnbkh6)
        self.tk_label_lhbndkze = self.__tk_label_lhbndkze(self.tk_frame_lhbnbkh6)
        self.tk_label_lhbnl410 = self.__tk_label_lhbnl410(self.tk_frame_lhbnbkh6)
        self.tk_label_lhbnofss = self.__tk_label_lhbnofss(self.tk_frame_lhbnbkh6)
        self.tk_label_lhbnogju = self.__tk_label_lhbnogju(self.tk_frame_lhbnbkh6)
        self.tk_label_lhbnoh63 = self.__tk_label_lhbnoh63(self.tk_frame_lhbnbkh6)
        self.tk_input_lhbnohw1 = self.__tk_input_lhbnohw1(self.tk_frame_lhbnbkh6)
        self.tk_label_lhbnoiut = self.__tk_label_lhbnoiut(self.tk_frame_lhbnbkh6)
        self.tk_input_lhbnoq64 = self.__tk_input_lhbnoq64(self.tk_frame_lhbnbkh6)
        self.tk_label_lhbnoxiw = self.__tk_label_lhbnoxiw(self.tk_frame_lhbnbkh6)
        self.tk_label_lhbnoy31 = self.__tk_label_lhbnoy31(self.tk_frame_lhbnbkh6)
        self.tk_input_lhbnoypr = self.__tk_input_lhbnoypr(self.tk_frame_lhbnbkh6)
        self.tk_label_lhbnozmq = self.__tk_label_lhbnozmq(self.tk_frame_lhbnbkh6)
        self.tk_label_lhbnp0e3 = self.__tk_label_lhbnp0e3(self.tk_frame_lhbnbkh6)
        self.tk_input_lhbnp1be = self.__tk_input_lhbnp1be(self.tk_frame_lhbnbkh6)
        self.tk_label_lhbnp2df = self.__tk_label_lhbnp2df(self.tk_frame_lhbnbkh6)
        self.tk_table_lhbnewl1 = self.__tk_table_lhbnewl1(self.tk_tabs_lhbmo7q9_1)
        self.tk_button_lhbnf1zk = self.__tk_button_lhbnf1zk(self.tk_tabs_lhbmo7q9_1)
        self.tk_frame_lzzk2acd = self.__tk_frame_lzzk2acd(self)
        self.tk_radio_button_lzzk3uww = self.__tk_radio_button_lzzk3uww(
            self.tk_frame_lzzk2acd
        )
        self.tk_radio_button_lzzk6xfb = self.__tk_radio_button_lzzk6xfb(
            self.tk_frame_lzzk2acd
        )
        self.tk_radio_button_lzzk6yol = self.__tk_radio_button_lzzk6yol(
            self.tk_frame_lzzk2acd
        )
        self.tk_radio_button_lzzk8qos = self.__tk_radio_button_lzzk8qos(
            self.tk_frame_lzzk2acd
        )

    def __win(self):
        self.title("电阻凑算工具")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""

        def show():
            if vbar:
                vbar.lift(widget)
            if hbar:
                hbar.lift(widget)

        def hide():
            if vbar:
                vbar.lower(widget)
            if hbar:
                hbar.lower(widget)

        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar:
            vbar.bind("<Enter>", lambda e: show())
        if vbar:
            vbar.bind("<Leave>", lambda e: hide())
        if hbar:
            hbar.bind("<Enter>", lambda e: show())
        if hbar:
            hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor="ne")

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor="sw")

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_tabs_lhbmo7q9(self, parent):
        frame = Notebook(parent)
        self.tk_tabs_lhbmo7q9_0 = self.__tk_frame_lhbmo7q9_0(frame)
        frame.add(self.tk_tabs_lhbmo7q9_0, text="分压")
        self.tk_tabs_lhbmo7q9_1 = self.__tk_frame_lhbmo7q9_1(frame)
        frame.add(self.tk_tabs_lhbmo7q9_1, text="凑电阻")
        frame.place(x=10, y=10, width=580, height=480)
        return frame

    def __tk_frame_lhbmo7q9_0(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=10, width=580, height=480)
        return frame

    def __tk_frame_lhbmo7q9_1(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=10, width=580, height=480)
        return frame

    def __tk_frame_lzziu5kh(self, parent):
        frame = Frame(
            parent,
        )
        frame.place(x=0, y=0, width=580, height=455)
        return frame

    def __tk_frame_lzzj8k9u(self, parent):
        frame = Frame(
            parent,
        )
        frame.place(x=20, y=20, width=430, height=80)
        return frame

    def __tk_label_lhbmtl8h(self, parent):
        label = Label(
            parent,
            text="VIN=",
            anchor="center",
        )
        label.place(x=0, y=0, width=50, height=30)
        return label

    def __tk_input_lhbmtn25(self, parent):
        ipt = Entry(
            parent,
        )
        ipt.place(x=60, y=0, width=70, height=30)
        return ipt

    def __tk_label_lhbmtpxy(self, parent):
        label = Label(
            parent,
            text="V",
            anchor="center",
        )
        label.place(x=140, y=0, width=30, height=30)
        return label

    def __tk_label_lhbmvt01(self, parent):
        label = Label(
            parent,
            text="MIN=",
            anchor="center",
        )
        label.place(x=0, y=50, width=50, height=30)
        return label

    def __tk_input_lhbmurrf(self, parent):
        ipt = Entry(
            parent,
        )
        ipt.place(x=320, y=0, width=70, height=30)
        return ipt

    def __tk_label_lhbmtras(self, parent):
        label = Label(
            parent,
            text="VOUT=",
            anchor="center",
        )
        label.place(x=260, y=0, width=50, height=30)
        return label

    def __tk_label_lhbmwcfd(self, parent):
        label = Label(
            parent,
            text="MAX=",
            anchor="center",
        )
        label.place(x=260, y=50, width=50, height=30)
        return label

    def __tk_input_lhbmwkar(self, parent):
        ipt = Entry(
            parent,
        )
        ipt.place(x=60, y=50, width=70, height=30)
        return ipt

    def __tk_label_lhbmz319(self, parent):
        label = Label(
            parent,
            text="KΩ",
            anchor="center",
        )
        label.place(x=400, y=50, width=30, height=30)
        return label

    def __tk_input_lhbmwujp(self, parent):
        ipt = Entry(
            parent,
        )
        ipt.place(x=320, y=50, width=70, height=30)
        return ipt

    def __tk_label_lhbmycfz(self, parent):
        label = Label(
            parent,
            text="KΩ",
            anchor="center",
        )
        label.place(x=140, y=50, width=30, height=30)
        return label

    def __tk_label_lhbmzk5h(self, parent):
        label = Label(
            parent,
            text="V",
            anchor="center",
        )
        label.place(x=400, y=0, width=30, height=30)
        return label

    def __tk_button_lhbn5n3b(self, parent):
        btn = Button(
            parent,
            text="计算",
            takefocus=False,
        )
        btn.place(x=480, y=20, width=80, height=80)
        return btn

    def __tk_table_lhbn5jnk(self, parent):
        # 表头字段 表头宽度
        columns = {"R high": 134, "R low": 134, "VOUT": 134, "误差": 134}
        tk_table = Treeview(
            parent,
            show="headings",
            columns=list(columns),
        )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor="center")
            tk_table.column(
                text, anchor="center", width=width, stretch=False
            )  # stretch 不自动拉伸

        tk_table.place(x=20, y=120, width=540, height=320)
        self.create_bar(parent, tk_table, True, False, 20, 120, 540, 320, 580, 455)
        return tk_table

    def __tk_frame_lzzkcgdj(self, parent):
        frame = Frame(
            parent,
        )
        frame.place(x=20, y=20, width=200, height=30)
        return frame

    def __tk_label_lhbn81re(self, parent):
        label = Label(
            parent,
            text="KΩ",
            anchor="center",
        )
        label.place(x=170, y=0, width=30, height=30)
        return label

    def __tk_label_lhbn763h(self, parent):
        label = Label(
            parent,
            text="期望R值",
            anchor="center",
        )
        label.place(x=0, y=0, width=50, height=30)
        return label

    def __tk_input_lhbn7or6(self, parent):
        ipt = Entry(
            parent,
        )
        ipt.place(x=70, y=0, width=77, height=30)
        return ipt

    def __tk_label_frame_lhbn9t2y(self, parent):
        frame = LabelFrame(
            parent,
            text="拓扑",
        )
        frame.place(x=262, y=0, width=291, height=70)
        return frame

    def __tk_radio_button_lhbn9vxx(self, parent):
        rb = Radiobutton(parent, text="R1+R2", variable=self.res_compose_type, value=1)
        rb.place(x=10, y=10, width=80, height=30)
        return rb

    def __tk_radio_button_lhbn9xmo(self, parent):
        rb = Radiobutton(
            parent, text="R1//R2+R3", variable=self.res_compose_type, value=3
        )
        rb.place(x=170, y=10, width=112, height=30)
        return rb

    def __tk_radio_button_lhbn9z6i(self, parent):
        rb = Radiobutton(parent, text="R1//R2", variable=self.res_compose_type, value=2)
        rb.place(x=90, y=10, width=80, height=30)
        return rb

    def __tk_frame_lhbnbkh6(self, parent):
        frame = Frame(
            parent,
        )
        frame.place(x=20, y=75, width=430, height=130)
        return frame

    def __tk_label_lhbnbuja(self, parent):
        label = Label(
            parent,
            text="R1",
            anchor="center",
        )
        label.place(x=0, y=0, width=50, height=30)
        return label

    def __tk_input_lhbnc1sa(self, parent):
        ipt = Entry(
            parent,
        )
        ipt.place(x=130, y=0, width=70, height=30)
        return ipt

    def __tk_label_lhbnc2y3(self, parent):
        label = Label(
            parent,
            text="MIN=",
            anchor="center",
        )
        label.place(x=70, y=0, width=50, height=30)
        return label

    def __tk_label_lhbnclao(self, parent):
        label = Label(
            parent,
            text="KΩ",
            anchor="center",
        )
        label.place(x=210, y=0, width=30, height=30)
        return label

    def __tk_input_lhbncnhk(self, parent):
        ipt = Entry(
            parent,
        )
        ipt.place(x=320, y=0, width=70, height=30)
        return ipt

    def __tk_label_lhbncqal(self, parent):
        label = Label(
            parent,
            text="MAX=",
            anchor="center",
        )
        label.place(x=260, y=0, width=50, height=30)
        return label

    def __tk_label_lhbndkze(self, parent):
        label = Label(
            parent,
            text="KΩ",
            anchor="center",
        )
        label.place(x=400, y=50, width=30, height=30)
        return label

    def __tk_label_lhbnl410(self, parent):
        label = Label(
            parent,
            text="R1",
            anchor="center",
        )
        label.place(x=0, y=50, width=50, height=30)
        return label

    def __tk_label_lhbnofss(self, parent):
        label = Label(
            parent,
            text="MIN=",
            anchor="center",
        )
        label.place(x=70, y=50, width=50, height=30)
        return label

    def __tk_label_lhbnogju(self, parent):
        label = Label(
            parent,
            text="KΩ",
            anchor="center",
        )
        label.place(x=210, y=50, width=30, height=30)
        return label

    def __tk_label_lhbnoh63(self, parent):
        label = Label(
            parent,
            text="MAX=",
            anchor="center",
        )
        label.place(x=260, y=50, width=50, height=30)
        return label

    def __tk_input_lhbnohw1(self, parent):
        ipt = Entry(
            parent,
        )
        ipt.place(x=320, y=50, width=70, height=30)
        return ipt

    def __tk_label_lhbnoiut(self, parent):
        label = Label(
            parent,
            text="KΩ",
            anchor="center",
        )
        label.place(x=400, y=0, width=30, height=30)
        return label

    def __tk_input_lhbnoq64(self, parent):
        ipt = Entry(
            parent,
        )
        ipt.place(x=130, y=50, width=70, height=30)
        return ipt

    def __tk_label_lhbnoxiw(self, parent):
        label = Label(
            parent,
            text="R1",
            anchor="center",
        )
        label.place(x=0, y=100, width=50, height=30)
        return label

    def __tk_label_lhbnoy31(self, parent):
        label = Label(
            parent,
            text="MIN=",
            anchor="center",
        )
        label.place(x=70, y=100, width=50, height=30)
        return label

    def __tk_input_lhbnoypr(self, parent):
        ipt = Entry(
            parent,
        )
        ipt.place(x=130, y=100, width=70, height=30)
        return ipt

    def __tk_label_lhbnozmq(self, parent):
        label = Label(
            parent,
            text="KΩ",
            anchor="center",
        )
        label.place(x=210, y=100, width=30, height=30)
        return label

    def __tk_label_lhbnp0e3(self, parent):
        label = Label(
            parent,
            text="MAX=",
            anchor="center",
        )
        label.place(x=260, y=100, width=50, height=30)
        return label

    def __tk_input_lhbnp1be(self, parent):
        ipt = Entry(
            parent,
        )
        ipt.place(x=320, y=100, width=70, height=30)
        return ipt

    def __tk_label_lhbnp2df(self, parent):
        label = Label(
            parent,
            text="KΩ",
            anchor="center",
        )
        label.place(x=400, y=100, width=30, height=30)
        return label

    def __tk_table_lhbnewl1(self, parent):
        # 表头字段 表头宽度
        columns = {"R1": 107, "R2": 107, "R3": 107, "R": 107, "误差": 107}
        tk_table = Treeview(
            parent,
            show="headings",
            columns=list(columns),
        )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor="center")
            tk_table.column(
                text, anchor="center", width=width, stretch=False
            )  # stretch 不自动拉伸

        tk_table.place(x=20, y=220, width=540, height=220)
        self.create_bar(parent, tk_table, True, False, 20, 220, 540, 220, 580, 480)
        return tk_table

    def __tk_button_lhbnf1zk(self, parent):
        btn = Button(
            parent,
            text="计算",
            takefocus=False,
        )
        btn.place(x=480, y=100, width=80, height=80)
        return btn

    def __tk_frame_lzzk2acd(self, parent):
        frame = Frame(
            parent,
        )
        frame.place(x=270, y=0, width=330, height=30)
        return frame

    def __tk_radio_button_lzzk3uww(self, parent):
        rb = Radiobutton(parent, text="E3", variable=self.res_e_series, value=3)
        rb.place(x=0, y=0, width=80, height=30)
        return rb

    def __tk_radio_button_lzzk6xfb(self, parent):
        rb = Radiobutton(parent, text="E12", variable=self.res_e_series, value=12)
        rb.place(x=160, y=0, width=80, height=30)
        return rb

    def __tk_radio_button_lzzk6yol(self, parent):
        rb = Radiobutton(parent, text="E24", variable=self.res_e_series, value=24)
        rb.place(x=240, y=0, width=80, height=30)
        return rb

    def __tk_radio_button_lzzk8qos(self, parent):
        rb = Radiobutton(parent, text="E6", variable=self.res_e_series, value=6)
        rb.place(x=80, y=0, width=80, height=30)
        return rb


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_lhbn5n3b.bind("<Button-1>", self.ctl.handle_divider_cal)
        self.tk_button_lhbnf1zk.bind("<Button-1>", self.ctl.handle_res_cal)
        pass

    def __style_config(self):
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
