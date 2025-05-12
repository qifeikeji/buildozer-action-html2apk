from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import webbrowser
import threading
import os
from http.server import SimpleHTTPRequestHandler
import socketserver

# 设置工作目录为应用所在目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# HTTP 服务器配置
PORT = 8000

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)

def start_server():
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 添加一个标签
        label = Label(text="本地 HTML 服务已启动", font_size=20)
        layout.add_widget(label)
        
        # 添加按钮，点击打开浏览器访问 localhost
        button = Button(text="打开 HTML 页面", size_hint=(1, 0.5))
        button.bind(on_press=self.open_webpage)
        layout.add_widget(button)
        
        # 在单独的线程中启动 HTTP 服务器
        server_thread = threading.Thread(target=start_server, daemon=True)
        server_thread.start()
        
        return layout
    
    def open_webpage(self, instance):
        # 打开默认浏览器访问 localhost:8000
        webbrowser.open(f"http://localhost:{PORT}")

if __name__ == '__main__':
    MyApp().run()
