#include <iostream>
#include <fstream>

using namespace std;

const int MAX_N = 100; // maksymalna ilość wierzchołków w grafie

struct TNode
{
	int node;            // numer wierzchołka
	int weight;          // waga krawędzi
	struct TNode * next; // następny element listy
};

void writeToFile(string result_file_name) {
	ofstream MyFile(result_file_name);
	MyFile << "Files can be tricky, but it is fun enough!";
	MyFile.close();
}

string readDataFile(string data_file_path) {
	string file_content;
	ifstream MyReadFile(data_file_path);
	while (getline (MyReadFile, file_content)) {
		cout << file_content;
	}
	MyReadFile.close();

	return file_content;
}

void parseDataToGraph(string file_content) {

}

int main(int argc, char **argv) {

	string result_file_name = "";
	string source_file_path = "../data/";
	string data_file_path = "../data/";

    for (int i = 0; i < argc; i++) {
		if (!strcmp(argv[i], "-oss")) result_file_name = argv[i+1];
		else if (!strcmp(argv[i], "-ss")) source_file_path += +argv[i+1];
		else if (!strcmp(argv[i], "-d")) data_file_path += argv[i+1];
	}

	writeToFile(result_file_name);
	string file_content = readDataFile(data_file_path);
	parseDataToGraph(file_content);
    return 0;
// 	int i,wmax,n,x,y,z;
// 	struct TNode *L[MAX_N],*p;

// 	for(i = 0; i < MAX_N; i++) L[i] = NULL;
// 	wmax = 0;
// 	cin >> n; // odczytujemy ilość krawędzi

// 	for(i = 0; i < n; i++) {
// 		cin >> x >> y >> z; // odczytujemy krawędź
// 		wmax = (x > wmax) ? x : wmax;
// 		wmax = (y > wmax) ? y : wmax;
// 		p = new TNode;
// 		p->next = L[x-1]; p->node = y; p->weight = z; L[x-1] = p;
// 	}
// 	cout << endl;

// 	for(i = 0; i < wmax; i++) {
// 		cout << i + 1 << ":";
// 		p = L[i];

// 		while(p) {
// 			cout << p->node << "#" << p->weight << " ";
// 			p = p->next;
// 		}
// 		cout << endl;
// 	}
// 	char s[1];
// 	cin.getline(s,1);
// 	cin.getline(s,1);
// 	cout<<"Eeeeeee"<<endl;
}