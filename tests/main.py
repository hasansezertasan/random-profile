# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
