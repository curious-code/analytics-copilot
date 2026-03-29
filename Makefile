.PHONY: install run test format

install:
	pip install -r requirements.txt

run:
	streamlit run app/streamlit_app.py

test:
	pytest tests/

format:
	black src/
	ruff check src/