# 必要機材
Ubuntu 14.04(ros-indigoはインストール済み) ×2  
Nextage open  
VIVE or perception Neuron  
※Perception Neuronの場合
windows(7以降)＆Visual Studio(2015以降)

##  VIVE用  
[ここ](http://bluelet.sakura.ne.jp/db/2017/12/11/post-57/)を参照に  
依存関係のインストール  
`sudo apt-get install steam libsdl2-dev libvulkan-dev libudev-dev libssl-dev zlib1g-dev python-pip`  
`sudo apt-get install libxtst6:i386 libxrandr-dev:i386 libglib2.0-dev:i386 libgtk2.0-0:i386 libpulse0:i386`  
SteamVRのインストール  
`steam://run/250820` からSteamVRをインストール  
OpenVR(python用　c++版はgitのソースから)をインストール  
`sudo pip install -U pip openvr`  
Steamの設定(OpenvrとLinuxでのSteamVRはBeta版なので、許可しないと立ち上がらない)  
`設定->アカウントから"ベータへの参加"を"Steam Beta update"にする`  
これでSteam右上VRアイコンでSteamVRが立ち上がることができる

##  Perception用 windows
公式からaxis neuronをインストール  
axis neuronは
`setting/broadcasting` のBVHにチェックを入れる  
`setting/output` のblock type は binary で固定する。  
Perception_Neuron_rosのtar.gzを解凍し、Visual Studioでビルドする。  
ビルドしたexeの場所にtar.gz内にあった、32bitのdllをコピーする。
あとは、exeを実行することで、Perception_NeuronがROSで使用可能になった。
