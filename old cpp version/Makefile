
CC=g++
CXXFLAGS=-std=c++11 -Wall -pedantic
LDFLAGS=

CPPFLAGS += -g
LDFLAGS += -g

all: test

test: HTML.o Tag.o

HTML.o: HTML.hpp Tag.o

Tag.o: Tag.hpp

clean:
	rm -f test *.o core*

