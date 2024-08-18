本工具用于电阻凑算，使用Python3开发，GUI使用Tkinter，无第三方依赖。

# 使用方法

## 计算分压电阻值

给定输入、输出电压，计算所需电阻比，根据电阻表选取最接近的电阻组合。电阻表支持E3-E24

支持约束阻值范围，不填表示无约束。支持升压、降压两种拓扑。

## 凑电阻

通过电阻串并联凑出期望阻值。支持三种拓扑。+代表串联，//代表并联。

# 打包

本项目仅依赖Python3标准库。
如使用pyinstaller打包可执行文件，执行`pyinstaller_build.sh`。
如使用nuitka打包可执行文件，执行`nuitka_build.sh`。

`电阻凑算工具.tk` 是[Tkinter布局助手](https://www.pytk.net/)导出的布局文件，可重新导入进行修改。

# 参考资料

[Tkinter布局助手](https://www.pytk.net/)

[Resistor Value and Ratio Calculator](https://jansson.us/resistors.html)