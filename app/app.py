# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from pathlib import Path

from litestar import Litestar, MediaType, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.openapi import OpenAPIConfig
from litestar.response import Template
from litestar.template.config import TemplateConfig
from openapipages import Scalar

from .config import API_CONFIG, data

basedir = Path(__file__).parent


@get(path="/", include_in_schema=False)
async def root() -> Template:
    return Template(template_name="index.html", context={"data": data})


@get(path="/schema/scalar", media_type=MediaType.HTML, include_in_schema=False)
def get_scalar() -> str:
    return Scalar(title="Scalar", openapi_url="/schema/openapi.json").render()


app = Litestar(
    route_handlers=[root, get_scalar],
    template_config=TemplateConfig(
        directory=basedir / "templates",
        engine=JinjaTemplateEngine,
    ),
    openapi_config=OpenAPIConfig(**API_CONFIG),
)
