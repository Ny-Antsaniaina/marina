FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN apt update && apt install -y ocaml make opam && \
    opam init -y --disable-sandboxing && \
    opam install -y ocamlfind ounit2 && \
    make

RUN pip install flask

EXPOSE 5000

CMD ["python", "api.py"]
