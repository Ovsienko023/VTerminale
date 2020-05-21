build :
	python3 Application-VT/testing/create_db.py

test :
	python3 Application-VT/testing/test_server.py

run :
	python3 Application-api/main.py

all: build test run