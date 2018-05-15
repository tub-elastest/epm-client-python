FROM python:3.5.2

RUN pip install epm-client six urllib3 certifi

ADD test_full.py test.py

ADD resources resources

ENTRYPOINT python test.py
