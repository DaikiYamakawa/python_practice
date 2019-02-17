from decimal import Decimal

d = Decimal(10)
print(d.sqrt())

class Myclass: 
    pass

class Myclass2:
    def __init__(self): # 初期化メソッドを定義
        self.value = 0  # インスタンスにアトリビュートを追加
        print('This is __init() method !')

class Prism:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
    
    # 初期化メソッドにてインスタンスのアトリビュートにデータを保存しているので引数はselfのみ
    def content(self): 
        return self.width*self.height*self.depth

i = Myclass() # Myclassというクラス名からインスタンスを作成し変数iに代入
i.value = 5
print(i.value)

i3 = Myclass2()
print(i3.value)

p1 = Prism(10, 10, 10)
p1.height = 20
ans = p1.content()
print(ans)

