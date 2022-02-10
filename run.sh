#docker build -t "mypython" .
docker run -it -v $(pwd):/app mypython python convertor.py -i ./input2.txt -o ./ -f YAML -d " " -s "A"
#docker run -it -v $(pwd):/app mypython python convertor.py