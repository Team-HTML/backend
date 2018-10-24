
#include "Tag.hpp"
#include <vector>
#include <queue>
#include <stack>
#include <fstream>
using namespace std;

class HTML{

        pair<int, int> size;

        Tag * root;

    public:

        HTML(string filePath);

        ~HTML();

        bool insert(Tag * tag);

        bool remove(Tag * tag);

        Tag * wrap(vector<Tag *> tags, string newTagName);

        vector<Tag *> dissect(Tag * group, vector<Tag *> parts);

        priority_queue<Tag *, vector<Tag *>, TagPtrComp> parse(string filePath);

        bool toHTML(string path);

};
