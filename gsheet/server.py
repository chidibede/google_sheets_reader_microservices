import utils
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.requests import Request


async def homepage(request):
    return JSONResponse({"hello": "Hello welcome"})

async def readsheet(request: Request):
    try:
       data = await request.json()
       response_data = utils.read_gsheet(data)

    except RuntimeError:
        return "Data not received"
    
    return JSONResponse({"status": 'true', "data": response_data})

routes = [
    Route('/', homepage),
    Route('/readsheet', readsheet, methods=['POST'])
]

app = Starlette(debug=True, routes=routes)
