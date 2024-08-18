def get_float_input(self, id):
    val = eval("self.ui.tk_input_" + id + ".get()")
    if val == "":
        val = 0
    else:
        val = float(val)
    return val
