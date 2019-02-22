from decimal import Decimal
from strdict import StrDict

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

# Prismクラスを継承したCubeクラスを定義
class Cube(Prism):
    def __init__(self, length): # 初期化メソッドを再定義
        super().__init__(length, length, length) # スーパークラス(Prism)のメソッドを呼び出し
        # self.width = self.height = self.depth = length # アトリビュートをlengthで初期化

class Prop:
    def __init__(self):
        self.__x = 0
    def getx(self):
        return self.__x
    def setx(self, x):
        self.__x = x
    x = property(getx, setx)

i = Myclass() # Myclassというクラス名からインスタンスを作成し変数iに代入
i.value = 5
print(i.value)

i3 = Myclass2()
print(i3.value)

p1 = Prism(10, 10, 10)
p1.height = 20
ans = p1.content()
print(ans)

# Cubeクラスを使う
c = Cube(20)
print(c.content())

i = Prop()
print(i.x)

i.x = 10
print(i.x)

print(i._Prop__x)

d = StrDict()
d['spam'] = 1
print(d['spam'])

d[1] = 1
