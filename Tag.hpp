
#include <vector>
#include <cstdlib>
#include <string>
using namespace std;

class Tag{

    private:

        string name;
        string id;
        string cls;//class
        string url;
        pair<int, int> tl;//topleft coordinate
        pair<int, int> br;//bottom right coordinate
        Tag * parent;
        vector<Tag *> children;
        double size;

    public:

        Tag(string name, string id, string cls = "", string url = "", 
            Tag * parent = 0) : name(name), id(id), cls(cls), url(url),
            parent(parent){
            size = (br.first - tl.first) * (br.second - tl.second);
        }

        ~Tag();
        
        bool operator < (const Tag & other);

        bool within(Tag * other);

        double S();

};

class TagPtrComp{
    public:
        bool operator() (Tag * & lhs, Tag * & rhs) const{
            return *lhs < *rhs;
        }
};
