"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""

# 示例下载 https://www.pytk.net/blog/1702564569.html
import utils
from res_calculator import ResCalculator


class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object

    def __init__(self):
        self.calculator = ResCalculator()

    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作

    def handle_divider_cal(self, evt):
        e_type = int(self.ui.res_e_series.get())
        self.calculator.set_res_table(e_type)
        vin = utils.get_float_input(self, "lhbmtn25")
        vout = utils.get_float_input(self, "lhbmurrf")
        r_min = utils.get_float_input(self, "lhbmwkar") * 1000
        r_max = utils.get_float_input(self, "lhbmwujp") * 1000
        # print(vin, vout, r_min, r_max)
        self.calculator.voltage_divider_cal(vin, vout, r_min, r_max, r_min, r_max)
        results = self.calculator.get_results(len=100)
        table = self.ui.tk_table_lhbn5jnk
        table.delete(*table.get_children())
        for li in results:
            table.insert("", "end", values=li)

    def handle_res_cal(self, evt):
        e_type = int(self.ui.res_e_series.get())
        self.calculator.set_res_table(e_type)
        cal_type = int(self.ui.res_compose_type.get())
        desired = utils.get_float_input(self, "lhbn7or6") * 1000
        r1_min = utils.get_float_input(self, "lhbnc1sa") * 1000
        r1_max = utils.get_float_input(self, "lhbncnhk") * 1000
        r2_min = utils.get_float_input(self, "lhbnoq64") * 1000
        r2_max = utils.get_float_input(self, "lhbnohw1") * 1000
        r3_min = utils.get_float_input(self, "lhbnoypr") * 1000
        r3_max = utils.get_float_input(self, "lhbnp1be") * 1000
        # print((desired, cal_type, r1_min, r1_max, r2_min, r2_max, r3_min, r3_max))
        self.calculator.res_compose_cal(
            desired, cal_type, r1_min, r1_max, r2_min, r2_max, r3_min, r3_max
        )
        results = self.calculator.get_results(len=100)
        table = self.ui.tk_table_lhbnewl1
        table.delete(*table.get_children())
        for li in results:
            table.insert("", "end", values=li)
