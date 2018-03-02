## 概要

このレポジトリは、カワダのnextage openでのテレイグジスタンスシステムのrosパッケージです。
現状はindigoで通信方式は、名前の通りudp通信です。

## 操縦方式
操作は[Perception_Neuron](https://github.com/smhaller/perception-neuron-ros)か
[VIVE](https://github.com/moon-wreckers/vive_tracker)を利用できます。

## コマンド
#### 操縦者側
###### Hiroのシミュレータ起動
'rtmlaunch hironx_ros_bridge hironx_ros_bridge_simulation.launch'
###### moveit起動
'roslaunch hironx_moveit_config moveit_planning_execution.launch'
###### 操縦方法の選択
VIVEかPerception Neuronを選択
###### windowsのディスプレイノード
'rosrun trcp_udp_telexistence joint_publisher.py'
###### 送信する際の関節角の整理用ノード
'rosrun trcp_udp_telexistence angle_publisher.py'
###### udpサーバーに送信するノード
'rosrun trcp_udp_telexistence send_angle.py'
