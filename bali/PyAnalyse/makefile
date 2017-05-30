#edit:main.o Comm_Balise_ts.o
#	g++ -o edit main.o Comm_Balise_ts.o

libAnalyse.so: main.cpp Comm_Balise_ts.cpp
	g++ -o libAnalyse.so -shared -fPIC main.cpp Comm_Balise_ts.cpp

clean:
	rm libAnalyse.so

run:
	python Analyse.py

#main.o:main.cpp Comm_Balise_ts.h 
#	g++ -c main.cpp

#Comm_Balise_ts.o:Comm_Balise_ts.cpp Comm_Balise_ts.h
#	g++ -c Comm_Balise_ts.cpp

#clean:
#	rm edit main.o Comm_Balise_ts.o 

