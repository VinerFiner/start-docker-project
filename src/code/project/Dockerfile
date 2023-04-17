FROM nginx

## 复制文件
# COPY index.html /usr/share/nginx/html/index.html
COPY index.html /mnt/index.html

# 映射文件
ENV PERSISTENCE_NAS /mnt/auto
RUN set -eux; \
	if [ ! -d  $PERSISTENCE_NAS ]; then \
		echo "$PERSISTENCE_NAS Not found"; \
		echo "create $PERSISTENCE_NAS"; \
	else \
		echo -e "directory already exists"; \
	fi; \
	\
	rm -rf /usr/share/nginx/html; \
	ln -sf /mnt /usr/share/nginx/html
# END