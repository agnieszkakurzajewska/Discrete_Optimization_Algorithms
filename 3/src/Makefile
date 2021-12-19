# https://cpp-polska.pl/post/potwor-przeszlosci-makefile-cz-1
# make -B -s because it doesn't update itself
main:
	@g++ dijkstra.cpp -o dijkstra
	./dijkstra -d simple/simple.gr -ss zrodla.ss -oss wyniki.ss.res
	rm -f dijkstra
