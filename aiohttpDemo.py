from aiohttp import web
import asyncio
#如果需要使用装饰器来路由uri的话，需要创建RouteTableDef类的对象来获取一个装饰器
routes = web.RouteTableDef()

@routes.get("/")
async def get_req(request):
    await asyncio.sleep(1)
    return web.Response(text="Hello World")

if __name__ == '__main__':
    app = web.Application()

    #如果不使用装饰器的话， 添加如下代码
    # app.add_routes([web.get("/", get_req),
    #                 web.post("/",post_req)])

    #如果使用装饰器，则添加如下一行
    app.add_routes(routes)
    web.run_app(app, host='127.0.0.1', port=8081)