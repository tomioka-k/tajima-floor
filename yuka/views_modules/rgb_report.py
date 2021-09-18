import numpy as np
import PIL.ImageDraw
import scipy.cluster
import os


class ImageReport:

    def __init__(self, image_path=None, n_cluster=3):
        self.image_path = image_path
        self.n_cluster = n_cluster

    def kmeans_process(self):
        img = PIL.Image.open(self.image_path)
        sm_img = img.resize((100, 100))
        color_arr = np.array(sm_img)
        w_size, h_size, n_color = color_arr.shape
        color_arr = color_arr.reshape(w_size * h_size, n_color)
        color_arr = color_arr.astype(np.float)

        codebook, distortion = scipy.cluster.vq.kmeans(
            color_arr, self.n_cluster)  # クラスタ中心
        code, _ = scipy.cluster.vq.vq(
            color_arr, codebook)  # 各データがどのクラスタに属しているか

        n_data = []  # 各クラスタのデータ数
        for n in range(self.n_cluster):
            n_data.append(len([x for x in code if x == n]))

        desc_order = np.argsort(n_data)[::-1]  # データ数が多い順に「第○クラスタ、第○クラスタ、、、、」

        return ['#{:02x}{:02x}{:02x}'.format(*(codebook[elem].astype(int))) for elem in desc_order]

    def triple_color_image(self, im_size=300):

        colors = self.kmeans_process()
        im = PIL.Image.new('RGB', (im_size, im_size), (255, 255, 255, 255))
        draw = PIL.ImageDraw.Draw(im)
        single_width = im_size / self.n_cluster

        for i, color in enumerate(colors):
            # 色を描画
            p1 = (single_width * i, 0)
            p2 = (single_width * (i + 1), im_size)
            pos = [p1, p2]
            draw.rectangle(pos, fill=color)

        # im.save('zzz.png')
        return im


if __name__ == "__main__":
    pass
