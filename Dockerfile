FROM python:3.10.9


SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN apt-get update && apt-get -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim redis-server

RUN useradd -rms /bin/bash api_user && chmod 777 /opt /run

WORKDIR /api_user

RUN mkdir /api_user/static && mkdir /api_user/media && chown -R api_user:api_user /api_user && chmod 755 /api_user

COPY --chown=api_user:api_user . .

RUN pip install -r requirements.txt

USER api_user