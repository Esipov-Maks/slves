#ВСЕ ВЕЛЕЧИНЫ ПРИВЕДЕНЫ В Г/СМ^3; Г; CM


print('Определение стоимости бруска')

metall = input('Введите название металла:\n Gold\n Silver\n Platinum\n')
d = float(input('Введите длинну бруска\n'))
sh = float(input('Введите ширину бруска\n'))
v = float(input('Введите высоту бруска\n'))


class Brusok :
    def __init__(self, d, sh, v) :
        self.d = d
        self.sh = sh
        self.v = v
    def check(self):
        if metall == 'Gold' :
            self.S = (19.3 / (d * sh * v)) * 2500
        elif metall == 'Silver' :
            self.S = (10.5 / (d * sh * v)) * 110
        else :
            self.S = (21.5 / (d * sh * v)) * 6500
        return self.S

Gold = Brusok(d, sh, v)
Silver = Brusok(d, sh, v)
Platinum = Brusok(d, sh, v)

if metall == 'Gold' :
    print('Стоимость такого бруска золота: ' + str(Gold.check()))
elif metall == 'Silver' :
    print('Стоимость такого бруска серебра :' + str(Silver.check()))
else :
    print('Стоимость такого бруска платины: ' + str(Platinum.check()))
