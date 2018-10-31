
//Dongyao Zhu

/*
(0, 0)                   X
  |---------------------->
  | top left 
  |   ____________________
  |  |                    |
  |  |                    |
  |  |                    |
  |  |____________________|
  |                   bottom right
Y v

*/

#ifndef TAG_HPP
#define TAG_HPP

#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

class Tag{

    private:

        string name;
        string cls;//class
        string url;
        string style;
        string id;
        Tag * parent;
        pair<double, double> tl;//abs topleft coordinates on page (no %)
        pair<double, double> br;//abs bottom right coordinates on page (no %)
        double wPct;//relative width % (to parent), 0 to 100(no %)
        double hPct;//relative height % (to parent), 0 to 100(no %)
        vector<Tag *> children;
        
    public:

        static map<string, int> count;

        friend int main(int argc, char** argv);

        friend inline ostream & operator << (ostream & os, Tag & t);

        friend class sortC;

        friend class sortS;

        friend class HTML;

        Tag(double tly, double tlx, double bry, double brx,
            string name, string url, string style);

        Tag(double tly, double tlx, double bry, double brx, Tag * a, Tag * b);

        ~Tag();

        bool operator < (Tag & t);

        Tag * expandRow(Tag * next);
        static Tag * wrap(Tag * a, Tag * b);

        string openTag();
        string closeTag();

        const double topLeftY();
        const double topLeftX();
        const double botRightY();
        const double botRightX();

        double S();
        double W();
        double H();
        Tag * P();

};

inline ostream & operator << (ostream & os, Tag & t) {
    os << "[n:" << t.name << " i:" << t.id << " (" << t.tl.first << "," 
    << t.tl.second << ")(" << t.br.first << "," << t.br.second << ")"
    << " h:" << t.H() << " sz:" << t.S() 
    << " p:" << (t.P()?t.P()->name:"n/a") << " #:" << to_string(t.children.size()) << "]";
    return os;
}

//sort by column
class sortC{
    public:
        bool operator() (Tag * i, Tag * j){ 
            return i -> tl.first > j -> tl.first ? true:
                i -> tl.first < j -> tl.first ? false:
                i -> tl.second > j -> tl.second ? true: false;
        }
};

//sort by size
class sortS{
    public:
        bool operator() (Tag * i, Tag * j){
            return i -> S() > j -> S();
        }
};

#endif

