# -*- coding: utf-8 -*-

from gpiozero import MCP3008
import math

class WaterTempSencer:
    R25C    = 10000 # R25C = Ω
    B_CONST = 3380 # B定数
    K       = 273.16 # ケルビン
    C25     = K + 25 # 摂氏25度

    def temp_celsius(self, volt):
        r = self.resistance_from_volt(volt)
        return self.resistance_to_temp(r)

    def resistance_from_volt(self, volt):
        r = ( 5.0 / volt - 1.0 ) * self.R25C # サーミスタ抵抗計算
        return r

    def resistance_to_temp(self, resistance):
        return self.B_CONST / (math.log(resistance / self.R25C) + (self.B_CONST / self.C25)) - self.K


class OilPressSencer:
    def pressure(self, volt):
        return (4.23e-3*volt) * 100 # BAR

vref              = 5.0
ch1               = MCP3008(channel=0)
ch2               = MCP3008(channel=1)
water_temp_sencer = WaterTempSencer()
oil_press_sencer  = OilPressSencer()

while True:
    water_temp = str(water_temp_sencer.temp_celsius(ch1.value * vref))
    oil_press = str(oil_press_sencer.pressure(ch2.value * vref))
    print(water_temp + 'C|' + oil_press + 'BAR')

