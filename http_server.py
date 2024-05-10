#!/usr/bin/python3
import http.server
import os
from urllib.parse import unquote
import pathlib

folder_path = pathlib.Path(__file__).parent.resolve().absolute()

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # 设置缓存控制头部
#        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
#        self.send_header('Pragma', 'no-cache')
#        self.send_header('Expires', '0')
        
        # 解码URL路径以获取文件名
        #filepath = unquote(self.path[1:])  # 移除开头的 '/'
        filepath = str(folder_path) + self.path
        
        print(filepath)
#        print("111111111111111")
        
        # 检查文件是否存在于当前目录
        if os.path.exists(filepath) and os.path.isfile(filepath):
            # 发送200 OK响应
            self.send_response(200)
            self.end_headers()
            with open(filepath, 'rb') as file:
                self.wfile.write(file.read())
        else:
            # 文件不存在，发送404 Not Found响应
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'File not found')

# 设置HTTP服务器和端口
with http.server.HTTPServer(('', 8000), SimpleHTTPRequestHandler) as server:
    print("Server started at localhost:8000")
    server.serve_forever()
