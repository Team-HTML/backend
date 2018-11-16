//Dongyao Zhu

#include "Tag.hpp"

//need to initialise static field somewhere
map<string, int> Tag :: count = map<string, int>();

/*
 * name: constructor
 * description: creates an actual Tag
 * input: Tag's information
 * output: Tag *
 */
Tag :: Tag(double tly, double tlx, double bry, double brx,
    string name, string url = "", string style = "") 
    : name(name), cls(name), url(url), style(style){
        this -> style = "\tposition: relative;\n" + this -> style;
        if(name == "p"){
            this -> style += "\tmargin: 0%;\n";
        }
        id = name + to_string(++count[name]);
        tl = make_pair<double, double>((double)tly, (double)tlx);
        br = make_pair<double, double>((double)bry, (double)brx);
        wPct = W();
        hPct = H();
}

/*
 * name: constructor
 * description: creates a wrapper Tag
 * input: information of Tags to be wrapped; if only one Tag,
        it is for expanding row.
 * output: Tag *
 */
Tag :: Tag(double tly, double tlx, double bry, double brx,
    Tag * a, Tag * b) : name("div"){
        tl = make_pair<double, double>((double)tly, (double)tlx);
        br = make_pair<double, double>((double)bry, (double)brx);
        id = "wrap" + to_string(++count["wrap"]);
        cls = "wrap";
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
}

/*
 * name: destructor
 * description: dfs, also decrease name count
 * input/output: none
 */
Tag :: ~Tag(){
    count[cls]--;
    for(Tag * t : children){
        delete t;
    }
}

/*
 * name: operator <
 * description: overloading operator < for comparing 2 Tags
        this is for priority queue's TagPtrComp comparision class
        want: smaller topLeftY, bigger H()
 * input: this and Tag & t
 * output: if this' priority < that of t's
 */
bool Tag :: operator < (Tag & t){
    return topLeftY() > t.topLeftY() ? true:
        topLeftY() < t.topLeftY() ? false:
        H() < t.H() ? true : false;/*H() > t.H() ? false:
        topLeftX() > t.topLeftX() ? true:
        topLeftX() < t.topLeftX() ? false:
        W() < t.W() ? true : false;*/
}

/*
 * name: expandRow
 * description: if t protrudes downwards, this tag will be wrapped with one 
        expanding to t's botRightY so this can include more tags as a row)
 * input: a pointer to another Tag
 * output: a pointer to the wrapper if wrapped, this otherwise
 */
Tag * Tag :: expandRow(Tag * t){
    //t is too long in y axis
    if(t -> botRightY() > botRightY()){ 
        return new Tag
            (topLeftY(), topLeftX(), t -> botRightY(), botRightX(), this, 0);
    }
    return this;
}

/* 
 * name: wrap
 * description: static, used to wrap 2 tags in a bigger parent tag, 
        and their positions are relative to their parent now.
 * input: 2 Tag * to be wrapped together
 * output: the parent wrapper
 */
Tag * Tag :: wrap(Tag * a, Tag * b){
    //smallest tly, tlx, largest bry, brx
    double tly = min(a -> topLeftY(), b -> topLeftY());
    double tlx = min(a -> topLeftX(), b -> topLeftX());
    double bry = max(a -> botRightY(), b -> botRightY());
    double brx = max(a -> botRightX(), b -> botRightX());
    Tag * t = new Tag(tly, tlx, bry, brx, a, b);
    //below are dirty css tricks
    //horizontal adjustment
    double ax = 100 * (a -> topLeftX() - t -> topLeftX()) / t -> W();
    if(ax > 0){
        a -> style += "\tleft: " + to_string(ax) + "%;\n";
    }
    double bx = 100 * (b -> topLeftX() - t -> topLeftX()) / t -> W();
    if(bx > 0){
        b -> style += "\tleft: " + to_string(bx) + "%;\n";
    }
    //vertical adjustment
    double ay = 100 * (a -> topLeftY() - t -> topLeftY()) / t -> H();
    if(ay > 0){
        a -> style += "\ttop: " + to_string(ay) + "%;\n";
    }
    double by = 100 * (b -> topLeftY() - t -> topLeftY() - a -> H()) / t -> H();
    if(by != 0){
        b -> style += "\ttop: " + to_string(by) + "%;\n";
    }
    return t;
}

/********************getters make life easier********************/

//returns opening tag to be written in html file
string Tag :: openTag(){
    string t = "<" + name;
    if(id != ""){
        t += " id = \"" + id + "\"";
    }
    if(cls != ""){
        t += " class = \"" + cls + "\"";
    }
    if(url != ""){
        if(name == "img"){
            return " src = \"" + url + "\">\n";
        }else{
            t += " href = \"" + url + "\"";
        }
    }
    return t + ">\n";
}

//returning closing tag to be written in html file
string Tag :: closeTag(){
    if(name == "img"){
        return "";
    }
    return "</" + name + ">\n";
}

//get top left corner's y coordinate
const double Tag :: topLeftY(){
    return tl.first;
}

//get top left corner's x coordinate
const double Tag :: topLeftX(){
    return tl.second;
}

//get bottom right corner's y coordinate
const double Tag :: botRightY(){
    return br.first;
}

//get bottom right corner's x coordinate
const double Tag :: botRightX(){
    return br.second;
}

//get size
double Tag :: S(){
    return (botRightX() - topLeftX()) * (botRightY() - topLeftY());
}

//get width
double Tag :: W(){
    return botRightX() - topLeftX();
}

//get height
double Tag :: H(){
    return botRightY() - topLeftY();
}

//get parent(useful for updating %)
Tag * Tag :: P(){
    return parent;
}

//eof
