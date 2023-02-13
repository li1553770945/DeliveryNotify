# 快递信息变动提醒

## 目的

你是否有这样的情况：新买了某个XX，好像早点拿到！男/女朋友送的礼物，好期待！于是，你每隔5分钟刷新一次快递物流信息。

## 功能

按照使用说明输入订单号等信息，启动程序，程序会在快递信息发生变化时发送推送到你的手机上。


### 支持的快递类型
[支持快递列表](deliver.md)
### 支持的通知方式
[支持通知方式列表](notify.md)

## 使用方法

### 安装依赖
使用`pip install -r requirements.txt"即可。

### 修改配置

修改json文件下的deliveries.json和settings.json。

deliveries.json是一个列表，每个项代表一个快递，包括type和number，分别代表[快递类型](deliver.md)和订单号。

settings.json包含query_interval和notifications，"query_interval"是查询的间隔，单位为秒。"notifications"是通知方式，包括type和key，分别代表[通知类型](notify.md)和key。
## 为本项目做贡献

### 添加支持快递
在delivery文件夹下新增文件，新建类集成delivery.py中的Delivery。在构造对象时，进行第一次查询，get_notification返回一个Notification对象，包含error、have_update和latest_msg,如果出现错误，则error为错误信息，否则为空字符串。have_update为bool类型，表明是否有更新，latest_msg表示当前最新消息。

完成后，更新delivery.md以及main.py中的delivery_classes。

### 添加支持通知

在notify文件夹下新增文件，新建类集成notify.py中的Notify。在构造对象时，传入参数为一个key，需要实现函数send，即发送消息。

完成后，更新notify.md以及main.py中的notify_classes。