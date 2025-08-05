FROM python:3.10-slim

RUN apt update && apt install -y \
    ocaml \
    opam \
    make \
    m4 \
    gcc \
    libgmp-dev \
    git \
    curl && \
    apt clean

WORKDIR /app

COPY . /app

RUN opam init -y --disable-sandboxing && \
    eval $(opam env) && \
    opam install -y ocamlfind ounit2 && \
    make

RUN pip install flask

EXPOSE 5000

CMD ["python", "api.py"]
