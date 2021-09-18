
def upload_product_image_path(instance, filename):
    # ext = filename.split('.')[-1]
    return "product/{}/report/{}".format(instance.product.code, filename)


def upload_product_triple_image_path(instance, filename):
    return "product/{}/report/{}".format(instance.product.code, "triple_image.png")
