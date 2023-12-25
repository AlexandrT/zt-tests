FROM python:3.11-alpine

RUN \
  apk update -q \
  && apk add -q \
  chromium \
  chromium-chromedriver

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN mkdir reports

CMD ["pytest", "tests", "--html=reports/report.html", "--self-contained-html", "--driver", "Chrome"]
