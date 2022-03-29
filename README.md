# BingImageApi  一个基于Flask的轻量的必应每日一图API
---
## Python版本 3.9
---
## 安装相关库
```python 

pip install flask
pip install gevent

```
---
## 使用  

启动服务 ```python3 app.py```

---
## 路由

http://localhost/api/v1/bing 返回JSON数据  
http://localhost/api/v1/bing/t 返回当天图片 默认4K  
http://localhost/bing/index 展示页面  

## 说明

默认端口 `54321`

自行修改端口 打开`app.py`文件见修改
