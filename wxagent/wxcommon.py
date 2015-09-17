import enum

WXAGENT_SERVICE_NAME = 'io.qtc.wxagent'
WXAGENT_SEND_PATH = '/io/qtc/wxagent'
WXAGENT_IFACE_NAME = 'io.qtc.wxagent.iface'

WXAGENT_EVENT_BUS_PATH = '/io/qtc/wxagent/signals'
WXAGENT_EVENT_BUS_IFACE = 'io.qtc.wxagent.signals'


######
class WXMsgType(enum.IntEnum):
    MT_TEXT = 1
    MT_FACE = 2
    MT_SHOT = 3
    MT_VOICE = 34
    MT_X47 = 47  # 像是群内动画表情，好友之间的动画表情
    MT_X49 = 49  # 像是服务号消息,像是群内分享，像xml格式  # 像是文件啊
    MT_X51 = 51  # 像是好友之间的图片消息
    MT_X10000 = 10000  # 系统通知？

