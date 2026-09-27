class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        res=[]
        kelvin=celsius+273.15
        res.append(kelvin)

        farenheit=(celsius*1.80)+32.00
        res.append(farenheit)

        return res