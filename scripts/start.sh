#!/bin/bash
# 从第一行到最后一行分别表示：
# 2. 收集静态文件到根目录，
# 3. 生成数据库可执行文件，
# 4. 根据数据库可执行文件来修改数据库
# 5. 用 gunicorn 启动 django 服务
export DJANGO_SETTINGS_MODULE=backend.settings.production
python manage.py collectstatic --noinput&&
python manage.py makemigrations&&
python manage.py migrate
gunicorn backend.wsgi:application -c /ap/config/gunicorn.conf.py