# -*- coding: utf-8 -*-
# 分压凑算器
import itertools
import math


class ResCalculator:
    def __init__(self) -> None:
        self.set_res_table()
        self.results = []
        self.results_type = ""

    def cal_e_series(self, e=24):
        _diff = math.log(10) / e
        series = []
        for i in range(e):
            _value = round(math.exp(i * _diff), 1)
            if 2.6 <= _value <= 4.6:
                series.append(round(_value + 0.1, 1))
            elif _value == 8.3:
                series.append(round(_value - 0.1, 1))
            else:
                series.append(_value)
        return series

    def get_res_table(self):
        return ",".join([self.res_print_helper(r) for r in self.res_table])

    def set_res_table(self, e=24):
        _e_table = self.cal_e_series(e)
        self.res_table = (
            [i * 1000 for i in _e_table]
            + [i * 10000 for i in _e_table]
        )
        return ",".join([self.res_print_helper(r) for r in self.res_table])

    def res_print_helper(self, r):
        if r < 1e3:
            return "{:>.1f}Ω".format(r)
        elif r < 1e6:
            return "{:>.1f}KΩ".format(r / 1e3)
        elif r < 1e9:
            return "{:>.1f}MΩ".format(r / 1e6)
        else:
            raise ValueError(f"r={r}")

    def voltage_divider_cal(self, vin, vout, r1_min=0, r1_max=0, r2_min=0, r2_max=0):
        r1_max = math.inf if r1_max == 0 else r1_max
        r2_max = math.inf if r2_max == 0 else r2_max
        self.results = []
        for r1, r2 in itertools.product(self.res_table, self.res_table):
            v_div = r2 / (r1 + r2) * vin
            err = abs(v_div - vout) / vout
            if r1 >= r1_min and r1 <= r1_max and r2 >= r2_min and r2 <= r2_max:
                self.results.append((r1, r2, v_div, err))
        self.results.sort(key=lambda ele: ele[3])
        self.results_type = "voltage_divider_cal"
        return self.results

    def res_compose_cal(
        self, desired, type, r1_min=0, r1_max=0, r2_min=0, r2_max=0, r3_min=0, r3_max=0
    ):
        # type=1:R1+R2; type=2:R1//R2; type=3:(R1//R2)+R3
        r1_max = math.inf if r1_max == 0 else r1_max
        r2_max = math.inf if r2_max == 0 else r2_max
        r3_max = math.inf if r3_max == 0 else r3_max
        self.results = []
        r3_table = self.res_table if type == 3 else [r3_min]
        for r1, r2, r3 in itertools.product(self.res_table, self.res_table, r3_table):
            if (
                r1 >= r1_min
                and r1 <= r1_max
                and r2 >= r2_min
                and r2 <= r2_max
                and r3 >= r3_min
                and r3 <= r3_max
                and r1 <= r2
            ):
                if type == 1:
                    r = r1 + r2
                elif type == 2:
                    r = r1 * r2 / (r1 + r2)
                elif type == 3:
                    r = r1 * r2 / (r1 + r2) + r3
                else:
                    ValueError(f"Unsupported type {type}")
                err = abs(r - desired) / desired
                self.results.append((r1, r2, r3, r, err))
        self.results.sort(key=lambda ele: ele[4])
        self.results_type = "res_compose_cal"
        return self.results

    def get_results(self, len="inf", return_raw=False):
        if len == "inf":
            raw_results = self.results
        else:
            assert isinstance(len, int)
            raw_results = self.results[:len]
        if return_raw:
            return raw_results
        else:
            results = []
            if self.results_type == "voltage_divider_cal":
                for each in raw_results:
                    r1, r2, v_div, err = each
                    r1 = self.res_print_helper(r1)
                    r2 = self.res_print_helper(r2)
                    v_div = "{:.3f}V".format(v_div)
                    err = "{:.2%}".format(err)
                    results.append((r1, r2, v_div, err))
            elif self.results_type == "res_compose_cal":
                for each in raw_results:
                    r1, r2, r3, r, err = each
                    r1 = self.res_print_helper(r1)
                    r2 = self.res_print_helper(r2)
                    r3 = self.res_print_helper(r3)
                    r = self.res_print_helper(r)
                    err = "{:.2%}".format(err)
                    results.append((r1, r2, r3, r, err))
            else:
                raise ValueError(f"Err results_type={self.results_type}")
            return results


if __name__ == "__main__":
    res_cal = ResCalculator()
    # res_cal.voltage_divider_cal(vin, vout, cal_type, r1_min, r1_max, r2_min, r2_max)
    # res_cal.voltage_divider_cal(3.3, 1)
    # res_cal.print()
    res_cal.res_compose_cal(1e6, 1, 0, 0, 0, 0, 0, 0)
