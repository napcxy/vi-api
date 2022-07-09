from flask import Flask

app = Flask(__name__)


# 车牌识别
# 支持对中国大陆机动车车牌的识别，包括地域编号和车牌号
@app.route('/vi/v1/license_plate/', methods=['POST'])
def license_plate():
    return 'TODO: implementing license_plate'


# 车辆检测
# 识别图像中的所有车辆，返回每辆车的类型和坐标位置，
# 可识别小汽车、卡车、巴士、摩托车、三轮车 5 大类车辆并且可以在检测和识别的基础上，
# 对小汽车、卡车、巴士、摩托车、三轮车 5 类车辆分别计数，支持指定不规则区域的车辆统计
@app.route('/vi/v1/vehicle_detect/', methods=['POST'])
def vehicle_detect():
    return 'TODO: implementing vehicle_detect'


# 车辆识别
# 检测拍摄照片中的主体车辆位置，识别车辆品牌型号（如宝马 X3）、年份、颜色信息，
# 应该识别近 1000 款常见车型（小汽车为主）
# 这个功能可用于相册管理、图片分类打标签、电子汽车说明书、一键拍照租车等场景
# @app.route('/vi/v1/car/', methods=['POST'])
# def car():
#     return 'TODO: implementing car'


# 车辆属性识别
# 针对小汽车识别 11 种外观属性，
# 包括：是否有车窗雨眉、是否有车顶架、副驾驶是否有人、
# 驾驶位是否系安全带、遮阳板是否放下、车辆朝向等
# @app.route('/vi/v1/vehicle_attr/', methods=['POST'])
# def vehicle_attr():
#     return 'TODO: implementing vehicle_attr'


# 扩展功能
# 车辆外观损伤识别
# 车辆外观损伤识别，针对常见小汽车车型，识别车辆外观受损部件及损伤类型，
# 可识别数十种车辆部件、五大类外观损伤（刮擦、凹陷、开裂、褶皱、穿孔）主要应用于车祸，
# 保险，车辆检修等场景
# @app.route('/vi/v1/vehicle_damage/', methods=['POST'])
# def vehicle_damage():
#     return 'TODO: implementing vehicle_damage'


if __name__ == '__main__':
    app.run()
