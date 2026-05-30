class Loli:
    def __init__(self,name='咲来'):
        self.name=name
        self.caught=False

    def speak(self):
        return f'呐~{input("你的名字是")}君...\n既然用球召唤了我，\n就永远别想逃开终端了哦！'

my_loli=Loli()
print('命中！')
print(my_loli.speak())
print('\n捕捉成功！她将陪你debug到天亮~')
