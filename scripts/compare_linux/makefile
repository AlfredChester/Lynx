default:
	mkdir build
	g++ -O2 -Wall -g -m64 -std=c++14 1.cpp -o build/1
	g++ -O2 -Wall -g -m64 -std=c++14 2.cpp -o build/2
	g++ -O2 -Wall -g -m64 -std=c++14 mk.cpp -o build/mk
	cp -r ./build/* .

clear:
	rm -rf ./build/*
	rm ./1
	rm ./2
	rm ./mk