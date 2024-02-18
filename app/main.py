import datetime
import os
from typing import List, Union

from fastapi import Body, FastAPI, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from openapipages import Elements, RapiDoc, ReDoc, Scalar, SwaggerUI

from .schemas import Profile

basedir = os.path.abspath(os.path.dirname(__file__))

app = FastAPI(
    title="Random Profile",
    description="Random profile generator for designers. Name, surname, biography, username...",
    version="0.0.1",
    contact={
        "name": "Hasan Sezer Taşan",
        "url": "http://www.hasansezertasan.com",
        "email": "hasansezertasan@gmail.com",
    },
    responses={
        404: {
            "description": "Not found",
        },
        500: {
            "description": "Internal Server Error",
        },
    },
)
templates = Jinja2Templates(directory=os.path.join(basedir, "templates"))


@app.get("/")
async def read_root(request: Request) -> str:
    data = Profile(
        first_name="Hasan Sezer",
        last_name="Taşan",
        biography="I am a software developer. I am interested in web development, and web scraping.",
        username="hasansezertasan",
        password="123456",
        email="hasansezertasan@gmail.com",
        address="Ankara, Turkey",
        profession="Software Developer",
        date_of_birth=datetime.date(1999, 6, 19),
        phone_number="1234567890",
        domain="Software Development",
        profile_picture="https://avatars.githubusercontent.com/u/13135006?v=4",
        website="http://www.hasansezertasan.com",
    )
    return templates.TemplateResponse("index.html", {"request": request, "data": data})


@app.get("/swaggerui", response_class=HTMLResponse, include_in_schema=False)
def get_swaggerui() -> str:
    return SwaggerUI(title="Swagger UI").render()


@app.get("/redoc", response_class=HTMLResponse, include_in_schema=False)
def get_redoc() -> str:
    return ReDoc(title="ReDoc").render()


@app.get("/scalar", response_class=HTMLResponse, include_in_schema=False)
def get_scalar() -> str:
    return Scalar(title="Scalar").render()


@app.get("/elements", response_class=HTMLResponse, include_in_schema=False)
def get_elements() -> str:
    return Elements(title="Elements").render()


@app.get("/rapidoc", response_class=HTMLResponse, include_in_schema=False)
def get_rapidoc() -> str:
    return RapiDoc(title="RapiDoc").render()