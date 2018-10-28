//Dongyao Zhu

#ifndef TAG_HPP
#define TAG_HPP

#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#define ABOVE 0
#define BELOW 1
#define LEFT 2
#define RIGHT 3
#define SUB 4
#define SUPER 5
#define OVERLAP 7

using namespace std;

class Tag{

    private:

        string name;
        string cls;//class
        string url;
        string style;
        string id;
        Tag * parent;
        //.first is along y axis(positive to bottom),
        //.second is along x axis(positive to right).
        pair<double, double> tl;//abs topleft coordinate to screen in %
        pair<double, double> br;//abs bottom right coordinate to screen in %
        double wPct;//relative width % (to parent), 0 - 100(no %)
        double hPct;//relative height % (to parent), 0 - 100(no %)
        vector<Tag *> children;
        
    public:

        static map<string, int> count;

        friend int main(int argc, char** argv);

        friend inline ostream & operator << (ostream & os, Tag & t);

        friend class sortC;

        friend class sortS;

        friend class HTML;

        //constructor for actual tags ONLY
        Tag(double tly, double tlx, double bry, double brx,
            string name, string cls = "", string url = "", string style = "") 
            : name(name), cls(cls), url(url), style(style){
                this -> style = "\tposition: relative;\n" + this -> style;
                id = name + to_string(++count[name]);
                tl = make_pair<double, double>((double)tly, (double)tlx);
                br = make_pair<double, double>((double)bry, (double)brx);
                wPct = W();
                hPct = H();
                cout << id << ": new at " << this << endl;
        }

        //constructor for wrapper ONLY
        Tag(double tly, double tlx, double bry, double brx,
            Tag * a, Tag * b) : name("div"){
                tl = make_pair<double, double>((double)tly, (double)tlx);
                br = make_pair<double, double>((double)bry, (double)brx);
                id = "wrap" + to_string(++count["wrap"]);
                children.push_back(a);
                a -> parent = this;
                a -> wPct = 100 * a -> W() / W();
                a -> hPct = 100 * a -> H() / H();
                wPct = W();
                hPct = H();
                if(b){
                    children.push_back(b);
                    b -> parent = this;
                    b -> wPct = 100 * b -> W() / W();
                    b -> hPct = 100 * b -> H() / H();
                }
                style = "\tposition: relative;\n";
                cout << id << ": new at " << this << endl;
        }

        ~Tag(){
            cout << "~t " << *this << endl;
            if(id.find("wrap") != string :: npos){
                count["wrap"]--;
            }else{
                count[name]--;
            }
            for(Tag * t : children){
                delete t;
            }
        }

        bool operator < (Tag & t);
        int relation(Tag * t);

        Tag * expandRow(Tag * next);
        //Tag * expandCol(double maxCol);
        //Tag * expand(Tag * next);
        static Tag * wrap(Tag * a, Tag * b);

        double S();//size
        double W();//width
        double H();//height
        Tag * P();//parent
        
        string openTag();
        string closeTag();
        operator char *() const;//idk, might be useful later
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

