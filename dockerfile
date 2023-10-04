# Usa una imagen base de Python, especifica la versión deseada
FROM python:3

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

RUN pip install Django==3.2.8

# Especifica el comando que se ejecutará cuando se inicie el contenedor
CMD ["bash"]
