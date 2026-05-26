#!/bin/bash
PYTHONPATH=. env/bin/alembic revision --autogenerate -m "create products table"
PYTHONPATH=. env/bin/alembic upgrade head