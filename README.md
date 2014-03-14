Kivy is very good.
==================

- Instale dependências (necessárias para instalar o Cython e o PyGame)

<<<<<<< HEAD
```sh
sudo apt-get install build-essential python-dev

sudo apt-get install libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev
=======
``` sh
sudo apt-get install cython
virtualenv venv --system-site-packages
>>>>>>> b1e26bce764102d4e42f85f3dabdeb6cb2a3cf50
```

- Criar um virtualenv

`virtualenv venv`

- Clonar projeto e instalar dependências do projeto

```sh
git clone https://github.com/igr-santos/kivy-examples
cd kivy-examples
pip install -r requirements
```

*NOTA:* Caso tenha problemas para instalar o pygame, utilize os comandos abaixo:

```sh
sudo apt-get install libv4l-dev
sudo ln -s /usr/include/lib4l1-videodev.h videodev.h
```

Caso tenha problemas para carregar as imagens, eu solucionei da seguinte forma:

Recriei a virtualenv com o comando:

```sh
sudo apt-get install python-pygame
virtualenv --system-site-packages
```

Esse comando faz com que o virtualenv seja criado com as dependências do sistema.
