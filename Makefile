
CC=g++
CXXFLAGS=-std=c++11 -Wall -pedantic
LDFLAGS=

# if passed "type=opt" at command-line, compile with "-O3" flag 
# otherwise use "-g" for debugging

ifeq ($(type),opt)
	CPPFLAGS += -O3
	LDFLAGS += -O3
else
	CPPFLAGS += -g
	LDFLAGS += -g
endif

all: test

# include what ever source code *.h files pathfinder relies on 
# these are merely the ones that were used in the solution

test: HTML.o

HTML.o: HTML.hpp Tag.hpp

# include what ever source code *.h files xxx relies on 
# these are merely the ones that were used in the solution

# Note: you do not have to include a *.cpp file if it aleady 
# has a paired *.h file that is already included with class/method headers

clean:
	rm -f program1 program2 *.o core*

