import datetime
import os
from typing import List, Union

from fastapi import Body, FastAPI, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from openapipages import Elements, RapiDoc, ReDoc, Scalar, SwaggerUI

from .config import API_CONFIG
from .schemas import Profile

basedir = os.path.abspath(os.path.dirname(__file__))

app = FastAPI(**API_CONFIG)
templates = Jinja2Templates(directory=os.path.join(basedir, "templates"))


@app.get("/", include_in_schema=False)
async def root(request: Request) -> str:
    data = Profile(
        first_name="Hasan Sezer",
        last_name="Taşan",
        username="hasansezertasan",
        password="123456",
        email="hasansezertasan@gmail.com",
        phone_number="1234567890",
        profession="Software Developer",
        date_of_birth=datetime.date(1999, 6, 19),
        city="Ankara",
        address="Ankara, Turkey",
        biography="I am a software developer. I am interested in web development, and web scraping.",
        interests=["Web Development", "Web Scraping"],
        profile_picture="https://avatars.githubusercontent.com/u/13135006?v=4",
        website="http://www.hasansezertasan.com",
    )
    return templates.TemplateResponse("index.html", {"request": request, "data": data})


@app.get("/scalar", response_class=HTMLResponse, include_in_schema=False)
def get_scalar() -> str:
    return Scalar(title="Scalar").render()


@app.get("/elements", response_class=HTMLResponse, include_in_schema=False)
def get_elements() -> str:
    return Elements(title="Elements").render()


@app.get("/rapidoc", response_class=HTMLResponse, include_in_schema=False)
def get_rapidoc() -> str:
    return RapiDoc(title="RapiDoc").render()
