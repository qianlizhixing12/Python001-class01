## 学习笔记

#### django请求流程

1. wsgi接受请求，初始化request对象
2. urlconf找到对应路由，使用对应view
3. view联动model和template，构造response对象
4. wsgi返回response

#### 中间件

- 非侵入作用在1-2，3-4之间
- 处理全局管理，如session，cookie