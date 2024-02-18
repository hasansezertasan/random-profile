import datetime
import os
import secrets
import string

from litestar import Litestar, MediaType, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.openapi import OpenAPIConfig
from litestar.response import Template
from litestar.template.config import TemplateConfig
from openapipages import Scalar

from .config import API_CONFIG
from .schemas import Profile

basedir = os.path.abspath(os.path.dirname(__file__))
ALPHABET = string.ascii_letters + string.digits + "-_"


@get(path="/", include_in_schema=False)
async def root() -> Template:
    data = Profile(
        first_name="Hasan Sezer",
        last_name="Taşan",
        username="hasansezertasan",
        password="".join(secrets.choice(ALPHABET) for i in range(20)),
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
    return Template(template_name="index.html", context={"data": data})


@get(path="/schema/scalar", media_type=MediaType.HTML, include_in_schema=False)
def get_scalar() -> str:
    return Scalar(title="Scalar", openapi_url="/schema/openapi.json").render()


app = Litestar(
    route_handlers=[root, get_scalar],
    template_config=TemplateConfig(
        directory=os.path.join(basedir, "templates"),
        engine=JinjaTemplateEngine,
    ),
    openapi_config=OpenAPIConfig(**API_CONFIG),
)
