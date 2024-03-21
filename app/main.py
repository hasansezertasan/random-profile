# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from openapipages import Elements, RapiDoc, Scalar

from .config import API_CONFIG, data

basedir = Path(__file__).parent

app = FastAPI(**API_CONFIG)
templates = Jinja2Templates(directory=basedir / "templates")


@app.get("/", include_in_schema=False)
async def root(request: Request) -> str:
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
