from config.settings import BASE_DIR
from matplotlib import image, pyplot as plt
import numpy as np
import statistics
import cv2
import io
import matplotlib
matplotlib.use('Agg')


def hsv_report(rgb_image, plot_show=False, statistics_show=False):
    """HSV色座標系に変換してヒストグラムを表示する。さらにパーセントタイルを利用して全体的に明るい、暗いなどを検出する


    Args:
        rgb_image(obj): rgbイメージ画像
        plot_show(bool): hsv票色系のグラフをプロットするか
        statistics_show(bool):標準偏差を出力するか(処理が重い)

    Returns:
       hsv票色系のパーセントタイルの値

    """
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)  # hsv票色系に変換
    h, s, v = cv2.split(hsv)  # 各成分に分割

    def get_percentile_list(k, datas):
        # ここでは、パーセントタイルを 5,50,95パーセントとする。
        # パーセントタイルを利用して、輝度より明るい、暗い画像を判定などに利用する
        percentile = [5, 50, 95]  # パーセントタイルの設定。ここは、必要に応じて変更する
        out_datas = {}
        for i in percentile:
            value = np.percentile(np.array(datas), i)
            s = k + "_"+str(i)
            out_datas[s] = value
        return out_datas

    out_dict = {}

    plt.figure(figsize=(8, 5))

    # 色相
    if(plot_show == True):
        plt.hist(h.ravel(), 256, [0, 256], color="red",
                 alpha=0.7, histtype="step", label="Hue")
    data = get_percentile_list("h_per", h.ravel())
    out_dict.update(data)

    if(statistics_show == True):
        out_dict['h_pstdev'] = statistics.pstdev(h.ravel()/255)

    # 彩度
    if(plot_show == True):
        plt.hist(s.ravel(), 256, [0, 256], color="green",
                 alpha=0.7, histtype="step", label="Saturation")
    data = get_percentile_list("s_per", h.ravel())
    out_dict.update(data)
    if(statistics_show == True):
        out_dict['s_pstdev'] = statistics.pstdev(s.ravel()/255)

    # 輝度
    if(plot_show == True):
        plt.hist(v.ravel(), 256, [0, 256], color="blue",
                 alpha=0.7, histtype="step", label="Value")
        plt.legend(bbox_to_anchor=(1, 1), loc='upper right',
                   borderaxespad=0, fontsize=10)
        # plt.show()

    data = get_percentile_list("v_per", v.ravel())
    out_dict.update(data)
    if(statistics_show == True):
        out_dict['v_pstdev'] = statistics.pstdev(v.ravel()/255)

    return out_dict


def plt2svg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s


def plt2png():
    buf = io.BytesIO()
    s = plt.savefig(buf, format='png', dpi=200)
    s = buf.getvalue()
    buf.close()
    return s


def get_hsv_report(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    report = hsv_report(img, plot_show=True)
    return report


if __name__ == '__main__':
    print("hsv_report")
