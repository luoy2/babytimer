import multiprocessing
workers = 2  # 并行工作进程数
threads = 1  # 指定每个工作者的线程数
bind = ['0.0.0.0:18009']  # 监听内网端口8000
worker_tmp_dir = '/dev/shm'
proc_name = 'babyTimer'  # 进程名称
# pidfile = '/tmp/blog.pid'  # 设置进程文件目录
worker_class = 'gevent'  # 工作模式协程
timeout = 30  # 超时
max_requests = 6000  # 最大请求数
errorlog = '-'
loglevel = 'debug'
accesslog = '-'
access_log_format = "{'remote_ip':'%(h)s','request_id':'%({X-Request-Id}i)s','response_code':'%(s)s','request_method':'%(m)s','request_path':'%(U)s','request_querystring':'%(q)s','request_timetaken':'%(D)s','response_length':'%(B)s'}"
