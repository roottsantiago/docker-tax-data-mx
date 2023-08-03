#!/bin/sh

echo "--- Run server ---"
uvicorn taxdata.app.main:app --reload --host 0.0.0.0 --port 8000
