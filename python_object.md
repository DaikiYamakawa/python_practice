# pythonでオブジェクト指向を勉強する

## 使った教科書

- みんなのPython

## オブジェクトとしての組み込み型

### 命令型プログラミング

- 今までやっていたプログラミング手法は命令型プログラミング
- データはデータ、命令は命令というように別々に扱う
  - 利点
    - シンプルで明瞭なプログラムを作ることができる
  - 欠点
    - できることが少なく、色々な種類の関数を用意する必要がある
      - プログラムが無駄に長くなったり、見通しが悪くなる
    - 複雑なプログラムや、規模の大きなプログラムが作りづらい

### オブジェクト指向
- 複雑で規模の大きなプログラムを手軽に作ることを要求されている
- データと命令を一緒にしてしまおうというのが基本的な考え方
- 少し乱暴な説明だけどデータと命令(メソッド)が一緒になっているもののことをオブジェクトと呼ぶ
- どのような処理を必要としているのかはオブジェクトが知っているという風に考える

### メソッド呼び出しの記法

```bash
データ．メソッド名(引数1，引数2，…)
```

### 変更可能と変更不可能

- オブジェクト自体を変更できるかできないで分類することがある
- 変更可能(mutable)
  - リスト型、ディクショナリ型など
  - リストのソートを行うsort()メソッドなどは自分自身(オブジェクト自体)を書き換える
  → 破壊的操作と呼ぶ
- 変更不可能(immutable)
  - タプル型、文字列型など
  - 自分自身を書き換える破壊的操作ができなくなっている

## クラスとオブジェクト指向開発

オブジェクトはデータと命令が一緒になっているものであり、プログラムで使う部品のようなもの  
オブジェクト指向開発の特徴は出来合いの部品を組み合わせてプログラムを作成していくこと

## Pythonでクラスを使う

- オブジェクト
  - 数値や文字列、リストなどのデータ
  - データに対していろいろな処理を実行できるメソッド  
  → 単なるデータではなく、どのような振る舞いをすればよいかを知っている
  - データの性質によって分類されている
  - 似た性質を持ったオブジェクトには同じメソッドが使えるようになっている
- クラス
  - オブジェクトの設計図
  - オブジェクトがどのような性質を持っていて、どのような振る舞いをするのかを定義する

## クラスからオブジェクト(インスタンス)を作る

```bash
from decimal import Decimal

d = Decimal(10) # Decimalクラスのインスタンスを作成
print(d)
```

- クラスから作ったオブジェクトのことを特別に区別する意味でインスタンスと呼ぶ
- インスタンスはデータもメソッドも持っているのでオブジェクトの一種
  - Decimalクラスのオブジェクト　→　特に区別してDecimalクラスのインスタンスと呼ぶ

## インスタンスを利用する

- Decimalクラスのインスタンスは組み込み型の数値型と同じように四則演算ができる

```bash
print(d+20)
```

- Decimalクラスのインスタンスはメソッド(データをどのように処理するか)も持っている

```bash
print(d.sqrt())
```

## オブジェクトとインスタンス

- オブジェクトとインスタンスはとても良く似た作りになっている
  - 両方ともデータとメソッドを持っている
  - 組み込み型
    - データの性質によって数値型や文字列型などの「型」が存在してた
    - どのような型であるかによって、オブジェクトに対して実行できる操作やメソッドの種類が異なっていた
  - クラス
    - クラス名が組み込み型の「型」に相当する
    - クラス名によって、インスタンスの性質を決まると考える
    - インスタンスの場合は、どのクラスのインスタンスであるかによって、メソッドや処理の種類が変わってくる
  - 組み込み型とクラスの共通点
    - プログラムで使う部品の「設計図」のようなもの
      - 設計図を元に、プログラムを組み立てるために作る「部品」がオブジェクトやインスタンス
  - オブジェクト指向を使った開発の基本
    - プログラムで利用する部品をあらかじめ作成しておき、必要に応じて部品を作って利用する
    - 考え方はこれだけなので特に難しいことはない

## クラスを作る

- クラスとはプログラムを利用するオブジェクトの設計図
  - オブジェクト(クラスから作られたらインスタンス)
    - データとメソッドを持っている
    - 自分自身がどのようなデータを持っていて、どのような振る舞いをすれば良いのかを知っている

- 普段はPythonが持っている標準のクラスを用いてインスタンスを作成することでプログラムを作成している
  - 特殊なこと、独自の処理を行いたいときは新しいクラスを作ったり、既存のクラスを拡張したりする

- クラスはインスタンスの設計図となるもの
  - インスタンスがどのような性質のデータをもっているか
  - インスタンスの持つデータに対してどのような処理を行う必要があるのか
  ↑この2つに注目してクラスという設計図を作成する
  - このことをクラス定義と呼ぶ
    - 設計図にはオブジェクト(インスタンス)にどのようなデータが保存されるか
      - データはアトリビュートと呼ばれる変数のようなものを使って、オブジェクトに保存する
    - どのようなメソッドを持つか
      - メソッドはPythonの関数定義と同じ記法を使って定義していく
    ↑この2つを定義していく

## クラスを定義する

- class文を使って定義する
  
```bash
class Myclass: # Myclassがクラス名
  pass
```

- クラス名には基本的に大文字で始まる英単語を利用する

## インスタンスのアトリビュート

- 作成したクラスからインスタンスを作成

```bash
i = Myclass() # Myclassというクラス名からインスタンスを作成し変数iに代入
```

- Myclassというクラスには何も定義をしていないため白紙の設計図
  - 作成されたインスタンスにはデータもメソッドもない
  - データを持っていないインスタンスにデータを持たせるためには？
    - アトリビュートを使う
    ```bash
    i.value = 5
    print(i.value)
    ```
    - アトリビュートは変数と同じような働きをする
    - 未定義のアトリビュートを参照するとエラーになる
    - アトリビュートはインスタンスごとに存在するので、異なるインスタンスから同じように参照しようとすると未定義エラーになる

## メソッドの定義と初期化メソッド「__init__()」

- アトリビュートのデメリット
  - 実際に代入操作を行ったインスタンスにしかアトリビュートが追加されない
  - データを追加したいときには、毎回インスタンスのアトリビュートに代入を行わなければならない
  - 例
    - 100個のインスタンスを作成してデータをもたせたい場合、アトリビュートへの代入を100回行わなければならない
- クラスはインスタンスの設計図
  - インスタンスが持つべきデータは、インスタンスが作られたときにあらかじめ代入しておくように設計図を書いておけば良い
  - Pythonでは、インスタンスが作られるときに自動的に呼ばれるメソッド(初期化メソッド)を定義できる

## 初期化メソッド

どのインスタンスにも共通して必要なアトリビュートは、初期化メソッドに代入して定義する

- Pythonのクラスにメソッドを定義する
  - クラス定義のブロック内にdef文を記述する
  - 一見すると関数定義と同じように見える
    - 違う点
      - メソッドの引数には必ずselfを定義する
      - 引数selfにはインスタンス自体が渡される
      - 簡単に言うと、selfを使うとインスタンス自体を操作することができる
  - 初期化メソッドを定義する
    - 名前は必ず__init__()でないといけない
    - インスタンスの生成時に自動的に実行される
    - 注意点
      - メソッドの定義がクラスのブロックの中にあること
      - 初期化メソッドの中では、インスタンス(self)にアトリビュート(value)を追加し、数値(0)を代入している
  
  ```bash
  class Myclass2:
    def __init__(self): # 初期化メソッドを定義
        self.value = 0  # インスタンスにアトリビュートを追加
        print('This is __init() method !')

  i3 = Myclass2() # インスタンスを作成
  print(i3.value) # インスタンスのアトリビュートを表示する
  ```

  - 作成されたインスタンスにはvalueというアトリビュートがあらかじめ作られていることがわかる
- クラス設計の考え方
  - インスタンスにどのようなデータをもたせるか
  - インスタンスにはアトリビュートを使ってデータを保存することができる
  - しかし、インスタンスごとにアトリビュートを設定するのは面倒くさい
  - そこで、クラスを定義する際に初期化メソッドを使ってインスタンスに必要なアトリビュートを作っておくようにする
    - 初期化メソッドにはself以外にも引数を設定することができる
    - 他の引数を設定すると、インスタンス作成時に追加の引数を設定することができる
    - そして、インスタンスを初期化するときに引数を渡し、インスタンスのデータ内容を制御することができる

## メソッドと第一引数「self」
- クラスのメソッドは「__init__()」以外にも様々なものを作ることができる
- しかし、第一引数には絶対にselfを渡すようにすること！
- 例題として角柱をあつかう
  - 構成要素
    - 幅
    - 高さ
    - 奥行
  - このように複数のデータを持つオブジェクトを手軽に扱いたいときに、クラスを定義すると便利
  - クラスの設計
    - クラスから作成されるインスタンス
      - 幅、高さ、奥行きの3つのデータを持っている
      - インスタンスを作るときに3つのデータを渡す
        - 初期化メソッドが呼ばれるときに3つの数値を渡すようにする
        - それらの値をインスタンスのアトリビュートとして保存しておけばよい
  ```bash
  class Prism:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
    
    # 初期化メソッドにてインスタンスのアトリビュートにデータを保存しているので引数はselfのみ
    def content(self): 
        return self.width*self.height*self.depth
  
  p1 = Prism(10, 30, 20)
  # contentメソッドを使用する
  # 引数はselfには自動的にインスタンスが代入されて呼び出されるため引数は不要
  ans = p1.content() 
  print(ans)
  ```
- Pythonのクラス定義にはselfがとても大切
- クラス定義の中でインスタンスに対して操作を行いたいときには、必ず引数にselfを設定する
  - クラス定義の時にp1.heightでインスタンスのアトリビュートの値を取り出せることからselfはインスタンスを指し示していることが分かっている
  ```bash
  p1 = Prism(10, 10, 10)
  # アトリビュートを書き換える
  p1.height = 20 
  ans = p1.content()
  print(ans)
  ```
- 変数を書き換えるようにアトリビュートを書き換えることができる
- Pythonののクラスのメソッド定義では、selfという引数を活用して処理を進めていく
- selfを使ってインスタンスにデータを登録、メソッドを使ってメソッドのふるまいを定義していく

## アトリビュートの隠蔽
今までのことより、アトリビュートは外部から書き換えることができることがわかった．
- デメリット
  - メソッドやアトリビュートが外部から操作できることで意図しないエラーを引き起こすことがある
  - 対応策
    - クラスの内部だけで利用するアトリビュートやメソッドを外部から隠す
    - これをカプセル化という
- カプセル化
  - アトリビュート名やメソッド名の先頭にアンダースコア(_)を一つつける
    - プログラマにわかる暗黙の了解
    - 外部から書き換えてはいけないことを表している
  - アトリビュート名やメソッド名の先頭にアンダースコア(__)を二つつける
    - 1つの場合よりも強い制限がかかっている
    - pythonの機能により、内部的に違う変数に置き換えられる
    - そのため、外部から書き換えることができない
      - 名前の置き換えルールを知っていれば書き換えることができる
  - Pythonのカプセル化は簡易的に作られている

# クラスの継承と高度なオブジェクト指向機能

## クラスを継承する
継承：あるクラスをひな型にして、別のクラスを作ること
スーパークラス：ひな形となる親クラス
サブクラス：スーパークラスを元に作られたクラス
多重継承：複数のクラスを組み合わせて、新しいクラスを定義すること
- 前章より、クラスとはプログラミングで利用する部品(インスタンス)の設計図
- 継承を使うことですでにある設計図を基に
  - 一部の機能を書き換える
  - 機能を強化した別の設計図(クラス)を作成
  - 同じ処理を書く必要がないので効率が良いコードを書ける

## スーパークラスを指定する
クラスの継承方法
```bash
class クラス名(スーパークラス名1[, スーパークラス名2, ...]):
```

## メソッドのオーバーライド
- クラスを継承する際に、スーパークラスのメソッドはサブクラスに受け継がれる
- 機能を変更したいメソッドだけ、サブクラスで改めて定義する
  - クラスのオーバーライドという

例題：直方体を作るサブクラスを作成
- Prismクラスは長方体だったので、辺の長さを3つ指定する必要があった
- しかし、Cubeは直方体なので、辺の長さはすべて同じ
- Cubeクラスの特徴に合わせて、初期化メソッドを定義しなおす

```bash
# Prismクラスを継承したCubeクラスを定義
class Cube(Prism):
    def __init__(self, length): # 初期化メソッドを再定義
        self.width = self.height = self.depth = length # アトリビュートをlengthで初期化

# Cubeクラスを使う
c = Cube(20) # lengthに20を渡す
print(c.content()) # Prismクラスのメソッドを呼び出す
```

- content()メソッドはPrismクラス内で定義されている
- Cubeクラスの初期化メソッドは1つの引数しか取らない
- Prismクラスのインスタンスが持つ3つのアトリビュートと同じアトリビュートを持っているため、content()メソッドをそのまま利用する

## 初期化メソッドのオーバーライド

- Pythonのオーバーライドは完全な上書きが行われる
- 場合によっては厄介なことがある
- Cubeクラスで独自の__init__()メソッドを定義した結果、Prismクラス側で定義してある__init__()メソッドは呼び出されない
- そのため、Prismクラスを拡張したものが反映されずエラーを出力することがある
- 解決策
  - Prismクラスの変更に合わせて、継承しているCubeクラスも変更する必要がある
  - サブクラスの初期化メソッドでスーパークラスの初期化メソッドを呼び出す

## super()を使ったスーパークラスの取得

- スーパークラスのメソッドを呼び出すためには、super()という組み込み関数を使う
- super()
  - 引数を与えずに呼び出すとスーパークラスを自動的に呼び出す
  - 引数を渡す場合
    - 1つ目はスーパークラスを調べたいサブクラスのクラス名
    - 2つ目はインスタンス(self)を渡すようにする
    - 引数で指定したサブクラスのクラス名を返す
  ```bash
  # Prismクラスを継承したCubeクラスを定義
  class Cube(Prism):
      def __init__(self, length): # 初期化メソッドを再定義
          super().__init__(length, length, length) # スーパークラス(Prism)のメソッドを呼び出し
  ```  
  - このように、スーパークラスのメソッドを呼び出す必要がある場合は明示的に示す必要がある

## スロット

- pythonでは代入を行うことでインスタンスにアトリビュートを自由に追加することができる
- スロットを使うとアトリビュートの機能を制限することができる
  - メモリの使用効率を良くするためなどに利用される機能
- スロットの定義方法

```bash
__slot__ = [追加で許可するアトリビュート名]
```

- スロットに定義されていないアトリビュートを定義しようとすると、エラー出力される

## プロパティ

- pythonのアトリビュートは、インスタンスを通して参照したり、書き換えることができる
- 不意に予期せぬ種類のデータに書き換えられることがあるので、あまり好ましいことではない
  - これを防ぐ方法
    - インスタンスのデータ(アトリビュート)を変更したり参照する専用のメソッドを作ることがある
- セッター：データを設定するメソッドのこと
- ゲッター：データを取り出すメソッドのこと
- プロパティはセッターとゲッターを手軽に定義するための機能
  - property()という特別な組み込み関数を使って設定する
  - 定義方法
  ```bash
  property([ゲッター[, セッター]])
  ```
  - プログラム
  ```bash
  class Prop:
    def __init__(self):
        self.__x = 0 # アトリビュートを作る
    def getx(self): # ゲッター
        return self.__x # アトリビュートを返す
    def setx(self, x): # セッター
        self.__x = x # アトリビュートに値を入れる
    x = property(getx, setx) # プロパティを設定する

  i = Prop()
  print(i.x)

  i.x = 10
  print(i.x)

  print(i._Prop__x)
  ```

- プロパティと「__」を使うことで、実体を隠しながら、メソッドを使ってアトリビュートの操作や参照を行うことができる

## 特殊メソッドを利用する
- pythonは、__init__()以外にもアンダースコアが2つついたメソッドを多く持っている
  - これらの多くは特殊メソッドと呼ばれる
  - オブジェクトの振る舞いを変更したり、クラスの性質にあった特別な挙動を持たせたいときに特殊メソッドを使う

## 特殊メソッドを定義する
- 新しく作ったクラスに特殊メソッドを定義すると、インスタンスに対して演算子などを使った操作を行えるようになる
- 組み込み型を継承したクラスで特殊メソッドをオーバーライドすると、演算子などを使った場合の処理の内容を変更することができる
- 特殊メソッドの種類
  - 算術演算子
  - 比較演算子
  - 型の変換
  - コンテナ型で利用する
    - リストやタプルなど
  - アトリビュートのアクセスに利用される

## 組み込み型を継承する
- pythonでは組み込み型を継承して新しいクラスを作ることができる
- 組み込み型を部分的に機能をカスタマイズすることで、もともとの強力な機能を継承しながら、より使いやすいクラスを作ることができる
- 特殊メソッドを利用すること
  - 演算子や要素の操作など、組み込み型と同じ書式を使ってオブジェクトを操作することができる
  - 似たような機能は同じような方法で使えるようにすることはオブジェクト開発を行う上でとても大切

## ディクショナリ型を継承する

- ディクショナリ型を継承して拡張する

```bash
# ディクショナリ型を継承してクラスを作成
class StrDict(dict):
    def __init__(self):
        pass

    # 特殊メソッドをオーバーライド
    # keyを設定するときに呼ばれる特殊メソッド
    # keyが文字列型以外なら例外を発生
    def __setitem__(self, key, value):

        # 関数やメソッドの引数を制限したいときにはisinstance関数を使う
        if not isinstance(key, str):
            raise ValueError('Key must be str or unicode.')
        # スーパークラスの特殊メソッドを呼び出し、キーと値を設定
        dict.__setitem__(self, key, value)
```

# モジュール

## モジュールファイルを作る

- 標準モジュールだけではなく自分で作ることもできる
- 自分で作った関数やクラスを、モジュールに登録して置くことで、他のプログラムでも使いやすくなる
- モジュール自体をパッケージという形でまとめることで、コードの再利用をより便利に行えるようになる
- モジュール
  - モジュール名は「.py」などの拡張子の前まで
  - 内部に定義した関数や変数を必要に応じて外部から利用することを目的としている
  - pythonではモジュールとスクリプトファイルはほぼ同義
  - スクリプトファイル
    - 主にプログラムの実行を目的に作られる

この後はクラスとモジュールの関係や使い方を解説されていた

## モジュールの階層構造(パッケージ)

- 複数のモジュールを束ねて管理するパッケージという仕組みがある
  - Django
  - NumPy
  - 上記のような大規模なフレームワークやライブラリではパッケージという仕組みを使ってモジュールを管理している

### パッケージの実体

- パッケージによって複数のモジュールを1つのパッケージ配下に収めることができる
- パッケージの実体
  - モジュールとなるファイルを収めたディレクトリ
  - パッケージの階層構造はドットで区切る
- 注意点
  - パッケージの中にあるモジュールで定義されている関数を実行する場合
  ```bash
  # ドットで繋げていかなければならない
  パッケージ名.モジュール名.関数名()
  
  # もしくはfrom文を使ってもう少し短く記述する
  from パッケージ名 import モジュール名

  モジュール名.関数名() # この記述で関数を使えるようになる
  ```

### パッケージを作る

- パッケージの実体はディレクトリまたはフォルダ
- パッケージとして使いたいディレクトリには、「__init__.py」という名前のファイルを設置する
- パッケージをインポートすると、まずこのファイルが読み込まれ、トップレベルのブロックが実行される
  - トップレベルのブロック
    - パッケージをインポートするときに実行したい初期化用のコードを書くことができる
    - ファイルを空にしておいても良い

dir(インスタンス)を使うことでアトリビュートの一覧がわかる
