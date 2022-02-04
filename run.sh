#docker build -t "mypython" .
docker run -it -v $(pwd):/app mypython python convertor.py