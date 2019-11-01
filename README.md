<h1>py-reversi</h1>
<h2>実行環境</h2>
Python 3.7.3<br>
pipenv<br>
1 pythonをインストールする<br>
2 cmdでpip install pipenvを実行<br>
3 py-reversiディレクトリ内に cdコマンドで移動<br>
4 pipenv install を実行すると　pipfileを読み込み、必要ライブラリを自動でインストールする。<br>
chainer,pandas,etc<br>
5 py-reversi ディレクトリ内でpipenv shellコマンドを実行すると仮想環境ないに入れる<br>
6 python file_name.pyで実行
<h2>実行ファイル</h2>
game_master.py→ゲーム本体　対戦を行い結果を保存したりする<br>
chain_learn.py→学習実行（CPU）<br>
chain_gpu.py→学習実行（GPU)<br>
学習実行ファイルの1行目　importで入力データをどうするか決めれる<br>
import read_fileの場合　すでにあるCSVファイルの中から、黒が勝った試合の黒の手だけ抜き出すとかする<br>
つまり、CSVファイルから入力データを生成するとき用
import make_readだとその場で試合を生成しそのまま学習させる。

