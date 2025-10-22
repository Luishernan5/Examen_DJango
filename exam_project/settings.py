from pathlib import Path
import os
import dj_database_url  # 🔹 Para base de datos de Render

# --- RUTAS BASE ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SEGURIDAD ---
SECRET_KEY = 'django-insecure-%n!ev4!zw(#z!xy*pb!aq3#zbug1lcvd#m@1%3=*lk9ua-&4'

# ⚠️ En producción cambia a False
DEBUG = True

# 🔹 Render o cualquier otro host
ALLOWED_HOSTS = ['*']

# --- APLICACIONES ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'examapp',  # tu app
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- CONFIGURACIÓN DE URLS Y WSGI ---
ROOT_URLCONF = 'exam_project.urls'
WSGI_APPLICATION = 'exam_project.wsgi.application'

# --- TEMPLATES ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- BASE DE DATOS ---
# SQLite local / PostgreSQL en Render automáticamente
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}",
        conn_max_age=600
    )
}

# --- VALIDACIÓN DE CONTRASEÑAS ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- LOCALIZACIÓN ---
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# --- ARCHIVOS ESTÁTICOS ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_DIRS = [
    os.path.join(BASE_DIR, 'examapp', 'static'),
]

# --- CLAVE POR DEFECTO PARA MODELOS ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'