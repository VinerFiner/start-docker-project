FROM nginx

## 复制文件
# COPY index.html /usr/share/nginx/html/index.html
COPY index.html /mnt/index.html

# 映射文件
RUN ln -sf /mnt/index.html /usr/share/nginx/html/index.html