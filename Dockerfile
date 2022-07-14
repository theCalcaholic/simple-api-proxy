FROM alpine:latest

ENV TARGET_URL="http://localhost"
ENV ADDRESS="0.0.0.0"
ENV PORT="80"


WORKDIR /app
COPY . /app
RUN apk add python3 py3-pip && pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["/app/app.py"]

EXPOSE "$PORT"