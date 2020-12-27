FROM python:3.6-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# workdir
RUN mkdir /app
WORKDIR /app

# Install build deps
RUN apk add  \
    	    gcc \
	    g++ \
            make \
            libc-dev \
	    libffi-dev \
#            musl-dev \
#            linux-headers \
#            pcre-dev \
            postgresql-dev \
	    mariadb-dev \
	    jpeg-dev \
	    freetype-dev

# Install dependencies
ADD requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# add everything
ADD . /app

# listen on this port
EXPOSE 8000

# Add any custom, static environment variables needed by Django or your settings file here:
#ENV DJANGO_SETTINGS_MODULE=my_project.settings.deploy

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
RUN DATABASE_URL=none python manage.py collectstatic --noinput

# entrypoint
RUN chmod 755 /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

# Start uWSGI
CMD ["gunicorn", "voctoconf.wsgi:application", "--bind", "0.0.0.0:8000"]