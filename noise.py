import numpy as np

# Hàm tạo Gaussian noise và lưu vào file noise.npy
def createNoise(image_shape, mean=0, stddev=25):
    # Tạo Gaussian noise với mean và stddev
    noise = np.random.normal(mean, stddev, image_shape)
    
    # Giới hạn giá trị noise trong khoảng [0, 255]
    noise = np.where(noise > 0, np.around(noise), 0)

    # Lưu noise vào file noise.npy
    np.save('noise.npy', noise)
    
    print("Noise đã được tạo và lưu vào file noise.npy")

# Ví dụ sử dụng
# Kích thước ảnh giả định là 300x300
image_shape = (300, 300)

# Gọi hàm tạo noise
createNoise(image_shape)

