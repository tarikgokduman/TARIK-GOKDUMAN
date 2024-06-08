import numpy as np
import pandas as pd

def gaussian_filter(size, sigma=1):
    kernel = np.fromfunction(lambda x, y: (1 / (2 * np.pi * sigma ** 2)) * 
                             np.exp(- ((x - (size - 1) / 2) * 2 + (y - (size - 1) / 2) * 2) / (2 * sigma ** 2)), (size, size))
    return kernel / np.sum(kernel)


def apply_filter(image, filter_kernel):
    filtered_image = np.zeros((image.shape[0] - filter_kernel.shape[0] + 1, image.shape[1] - filter_kernel.shape[1] + 1))
    for i in range(filtered_image.shape[0]):
        for j in range(filtered_image.shape[1]):
            filtered_image[i, j] = np.sum(image[i:i+filter_kernel.shape[0], j:j+filter_kernel.shape[1]] * filter_kernel)
    return filtered_image


data = np.array([[153, 153, 153, 153, 153, 153, 153, 154, 154, 153, 153, 153, 154, 154, 155, 161, 161, 160, 160, 159, 155, 149, 145, 137, 132, 125, 121, 121, 124, 127, 128, 128],
                 [153, 153, 153, 153, 153, 153, 153, 153, 153, 153, 153, 154, 155, 156, 156, 161, 160, 159, 159, 159, 155, 150, 145, 137, 132, 125, 121, 121, 124, 127, 128, 128],
                 [153, 153, 153, 153, 153, 153, 153, 152, 152, 153, 154, 155, 156, 157, 158, 160, 159, 159, 159, 158, 155, 150, 145, 137, 132, 125, 121, 121, 124, 127, 128, 128],
                 [154, 154, 154, 154, 154, 154, 154, 151, 152, 154, 156, 157, 158, 159, 159, 159, 158, 158, 158, 158, 155, 150, 145, 137, 132, 125, 121, 121, 124, 127, 128, 128],
                 [154, 154, 154, 154, 154, 154, 154, 152, 153, 155, 157, 159, 159, 159, 159, 158, 157, 157, 158, 158, 155, 150, 146, 137, 132, 125, 121, 121, 124, 127, 128, 128],
                 [155, 155, 155, 155, 155, 155, 155, 153, 154, 157, 159, 160, 160, 159, 158, 157, 156, 156, 157, 157, 155, 150, 146, 137, 132, 125, 121, 121, 124, 127, 128, 128],
                 [155, 155, 155, 155, 155, 155, 155, 154, 156, 158, 160, 161, 160, 158, 157, 156, 156, 156, 157, 157, 155, 150, 146, 137, 132, 125, 121, 121, 124, 127, 128, 128],
                 [155, 155, 155, 155, 155, 155, 155, 155, 157, 159, 161, 161, 160, 158, 156, 156, 155, 155, 157, 157, 155, 150, 146, 137, 132, 125, 121, 121, 124, 127, 128, 128],
                 [155, 155, 156, 156, 157, 157, 157, 158, 159, 160, 160, 161, 160, 160, 160, 157, 157, 156, 157, 157, 156, 152, 149, 137, 130, 122, 119, 121, 125, 126, 126, 126],
                 [155, 156, 156, 156, 157, 157, 157, 159, 159, 160, 160, 160, 159, 159, 158, 157, 157, 156, 157, 157, 156, 152, 149, 137, 130, 122, 119, 121, 125, 126, 126, 126],
                 [156, 156, 156, 157, 157, 157, 158, 160, 160, 159, 159, 158, 157, 157, 156, 157, 157, 156, 157, 157, 156, 152, 149, 137, 130, 122, 119, 121, 125, 126, 126, 126],
                 [156, 156, 157, 157, 158, 158, 158, 160, 159, 158, 157, 156, 155, 155, 155, 157, 157, 156, 157, 157, 156, 152, 149, 137, 130, 122, 119, 121, 125, 126, 126, 126],
                 [157, 157, 157, 158, 158, 158, 159, 159, 158, 156, 155, 154, 153, 154, 154, 157, 157, 156, 157, 157, 156, 152, 149, 137, 130, 122, 119, 121, 125, 126, 126, 126],
                 [157, 157, 158, 158, 159, 159, 159, 158, 156, 154, 152, 152, 152, 153, 154, 157, 157, 156, 157, 157, 156, 152, 149, 137, 130, 122, 119, 121, 125, 126, 126, 126],
                 [157, 158, 158, 158, 159, 159, 159, 156, 154, 152, 151, 150, 152, 154, 155, 157, 157, 156, 157, 157, 156, 152, 149, 137, 130, 122, 119, 121, 125, 126, 126, 126],
                 [158, 158, 158, 159, 159, 159, 160, 155, 153, 151, 150, 150, 152, 154, 156, 157, 157, 156, 157, 157, 156, 152, 149, 137, 130, 122, 119, 121, 125, 126, 126, 126],
                 [153, 158, 162, 164, 163, 161, 160, 148, 143, 142, 145, 148, 149, 154, 160, 158, 159, 158, 156, 157, 158, 152, 143, 136, 129, 120, 117, 119, 122, 123, 123, 123],
                 [154, 158, 161, 163, 162, 159, 158, 146, 141, 141, 145, 147, 149, 154, 160, 158, 159, 158, 156, 157, 158, 152, 143, 136, 129, 120, 117, 119, 122, 123, 123, 123],
                 [155, 158, 161, 161, 159, 156, 154, 141, 138, 138, 143, 147, 149, 154, 161, 158, 159, 158, 156, 157, 158, 152, 143, 136, 129, 120, 117, 119, 122, 123, 123, 123],
                 [157, 159, 160, 159, 156, 151, 149, 136, 133, 135, 141, 147, 149, 155, 162, 158, 159, 158, 156, 157, 158, 152, 143, 136, 129, 120, 117, 119, 122, 123, 123, 123],
                 [159, 160, 160, 157, 152, 147, 143, 130, 128, 131, 140, 146, 150, 156, 162, 158, 159, 158, 156, 157, 158, 152, 143, 136, 129, 120, 117, 119, 122, 123, 123, 123],
                 [161, 161, 159, 155, 148, 142, 138, 124, 123, 128, 138, 146, 150, 156, 163, 158, 159, 158, 156, 157, 158, 152, 143, 136, 129, 120, 117, 119, 122, 123, 123, 123],
                 [162, 161, 159, 153, 146, 139, 134, 120, 120, 126, 137, 145, 150, 157, 163, 158, 159, 158, 156, 157, 158, 152, 143, 136, 129, 120, 117, 119, 122, 123, 123, 123],
                 [163, 162, 158, 152, 144, 137, 132, 118, 118, 124, 136, 145, 150, 157, 164, 158, 159, 158, 156, 157, 158, 152, 143, 136, 129, 120, 117, 119, 122, 123, 123, 123],
                 [163, 159, 154, 148, 140, 130, 123, 116, 119, 129, 141, 147, 149, 154, 160, 158, 159, 158, 156, 157, 158, 152, 143, 138, 130, 120, 115, 117, 121, 124, 125, 125],
                 [162, 157, 151, 144, 135, 126, 119, 116, 119, 129, 141, 147, 149, 154, 160, 158, 159, 158, 156, 157, 158, 152, 143, 138, 130, 119, 115, 117, 121, 124, 124, 124],
                 [160, 153, 146, 138, 129, 121, 115, 116, 119, 129, 141, 147, 149, 154, 160, 158, 159, 158, 156, 157, 158, 152, 143, 138, 129, 119, 114, 116, 121, 123, 124, 124],
                 [157, 149, 140, 133, 125, 118, 113, 116, 119, 129, 141, 147, 149, 154, 160, 158, 159, 158, 156, 157, 158, 152, 143, 137, 129, 119, 114, 116, 121, 124, 124, 124],
                 [153, 144, 135, 128, 123, 118, 115, 116, 119, 129, 141, 147, 149, 154, 160, 158, 159, 158, 156, 157, 158, 152, 143, 137, 128, 118, 113, 115, 120, 122, 123, 123],
                 [146, 136, 128, 124, 122, 120, 119, 116, 119, 129, 141, 147, 149, 154, 160, 158, 159, 158, 156, 157, 158, 152, 143, 136, 128, 118, 113, 115, 119, 122, 123, 123],
                 [138, 128, 121, 119, 120, 121, 122, 116, 119, 129, 141, 147, 149, 154, 160, 158, 159, 158, 156, 157, 158, 152, 143, 136, 127, 117, 113, 114, 119, 122, 122, 122],
                 [132, 123, 117, 116, 119, 122, 124, 116, 119, 129, 141, 147, 149, 154, 160, 158, 159, 158, 156, 157, 158, 152, 143, 136, 127, 117, 112, 114, 119, 121, 122, 122]])

gauss_kernel = gaussian_filter(3)


filtered_image = apply_filter(data, gauss_kernel)


filtered_df = pd.DataFrame(filtered_image)


print("Gaussian Filtered Image ({}x{}):".format(filtered_image.shape[0], filtered_image.shape[1]))
print(filtered_df)