# Подготовка виртуального окружения
.PHONY: venv
venv:
	python3 -m venv ./.venv

# Установка указанных пакетов (когда отсутствует файл `requirements.txt`)
.PHONY: direct_deps
direct_deps: venv
	(. ./.venv/bin/activate; pip3 install \
		transformers sentencepiece streamlit torch pytest flake8)

# Установка пакетов указанных в `requirements.txt`
.PHONY: deps
deps: venv
	(. ./.venv/bin/activate; pip install -r requirements.txt)

# Удаление виртуального окружения
.PHONY: del_deps
del_deps:
	rm -R ./.venv

# Сохранение зависимостей в файл `requirements.txt`
.PHONY: freeze
freeze:
	(. ./.venv/bin/activate; pip freeze > requirements.txt)

# Запуск
.PHONY: run
run:
	(. ./.venv/bin/activate; streamlit run main.py --server.port 7070)

# Запуск тестов
.PHONY: test
test:
	(. ./.venv/bin/activate; pytest)

# Линтер
.PHONY: lint
lint:
	(. ./.venv/bin/activate; \
		flake8 . --exclude .venv,test --count --select=E9,F63,F7,F82 --show-source --statistics; \
		flake8 . --exclude .venv,test --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics)

# docker build
.PHONY: docker_build
docker_build:
	docker build -t app-img .

# docker run
.PHONY: docker_run
docker_run:
	docker run -d -p 7070:7070 app-img
