#docker build -t "mypython" .
docker run -it -v $(pwd):/app mypython python convertor.py -i ./input1.txt -o ./ -f JSON -d " "
#docker run -it -v $(pwd):/app mypython python convertor.py