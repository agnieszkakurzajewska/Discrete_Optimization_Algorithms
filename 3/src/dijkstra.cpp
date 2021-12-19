#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;

const int MAX_N = 100; // maksymalna ilość wierzchołków w grafie

struct Node {
	int index;            // numer wierzchołka
	vector <struct Neighbour> next_nodes;
};

struct Neighbour {
	Node *p;
	int weight;
};

struct Graph {
	int n;
	int m;
	vector <struct Node> nodes;
};

vector<string> explode(string const & s, char delim)
{
    vector<string> result;
    istringstream iss(s);

    for (string token; getline(iss, token, delim); )
    {
        result.push_back(move(token));
    }

    return result;
}

void writeToFile(string result_file_name) {
	ofstream MyFile(result_file_name);
	MyFile << "Files can be tricky, but it is fun enough!";
	MyFile.close();
}

vector <Node> fill_nodes_list(int n) {
	vector <struct Node> nodes;
	vector <struct Neighbour> next_nodes;
	for (int i = 1; i<=n ; i++) {
		struct Node node;
		node.index = i;
		node.next_nodes = next_nodes;
		nodes.push_back(node);
	}
	return nodes;
}

void readDataFile(string data_file_path) {

	struct Graph g;
	struct Neighbour nb;
	vector <struct Node> nodes;

	ifstream file(data_file_path);
	if (file.is_open()) {
		string line;
		while (getline(file, line)) {
			vector<string> params = explode(line, ' ');
			if (params.size()) {
				if (params[0] == "p") {
					g.n = stoi(params[2]);
					g.m = stoi(params[3]);
					nodes = fill_nodes_list(g.n);
				} else if (params[0] == "a") {
					nb.p = &nodes[stoi(params[2])-1];
					nb.weight = stoi(params[3]);
					nodes[stoi(params[1])-1].next_nodes.push_back(nb);
				}
			}
		}	
		file.close();
		// 	struct Node mm;
		// mm = *(nodes[1].next_nodes[0].p);
		// cout<<mm.index<<endl;
	}
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
	readDataFile(data_file_path);
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