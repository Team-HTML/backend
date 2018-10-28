//Dongyao Zhu

#include "Tag.hpp"

map<string, int> Tag :: count = map<string, int>();

//compare tl.first, then H(), then tl.second, then W()
bool Tag :: operator < (Tag & t){
    return tl.first > t.tl.first ? true:
        tl.first < t.tl.first ? false:
        H() < t.H() ? true : H() > t.H() ? false:
        tl.second > t.tl.second ? true:
        tl.second < t.tl.second ? false:
        W() < t.W() ? true : false;
}

//for allowing error, it would be better if the parse function
//handles error beforehand 
//might discard this and check directly in html's constructor
int Tag :: relation(Tag * next){
    //overlap
    int code = OVERLAP;
    //this is ABOVE next
    if(br.first <= next -> tl.first){
        code = ABOVE;
    }
    //this is BELOW next
    else if(next -> br.first <= tl.first){
        code = BELOW;
    }
    //this on next's LEFT
    else if(br.second <= next -> tl.second){
        //&& tl.first <= next -> tl.first){ 
        //&& next -> br.first <= br.first){
        code = LEFT;
    }
    //this on next's RIGHT
    else if(next -> br.second <= tl.second){
        //&& tl.first <= next -> tl.first){ 
        //&& next -> br.first <= br.first){
        code = RIGHT;
    }
    //this is next's SUPER
    else if(next -> tl.first >= tl.first && next -> tl.second >= tl.second
        && next -> br.first <= br.first && next -> br.second <= br.second){
        code = SUPER;
    }
    //this is next's SUB
    else if(tl.first >= next -> tl.first && tl.second >= next -> tl.second
        && br.first <= next -> br.first && br.second <= next -> br.second){
        code = SUB;
    }
    return code;
}

//wraps a div with one expanding to t's br.second(bry)
Tag * Tag :: expandRow(Tag * t){
    //t is too long in y axis
    if(t -> br.first > br.first){ 
        return new Tag(tl.first, tl.second, t -> br.first, br.second, this, 0);
    }
    return this;
}

//general wrap
Tag * Tag :: wrap(Tag * a, Tag * b){
    //smallest tly, tlx, largest bry, brx
    double tly = min(a -> tl.first, b -> tl.first);
    double tlx = min(a -> tl.second, b -> tl.second);
    double bry = max(a -> br.first, b -> br.first);
    double brx = max(a -> br.second, b -> br.second);
    Tag * t = new Tag(tly, tlx, bry, brx, a, b);
    //horizontal adjustment
    double ax = 100 * (a -> tl.second - t -> tl.second) / t -> W();
    if(ax > 0){
        a -> style += "\tleft: " + to_string(ax) + "%;\n";
    }
    double bx = 100 * (b -> tl.second - t -> tl.second) / t -> W();
    if(bx > 0){
        b -> style += "\tleft: " + to_string(bx) + "%;\n";
    }
    //vertical adjustment
    double ay = 100 * (a -> tl.first - t -> tl.first) / t -> H();
    if(ay > 0){
        a -> style += "\ttop: " + to_string(ay) + "%;\n";
    }
    double by = 100 * (b -> tl.first - t -> tl.first - a -> H()) / t -> H();
    if(by != 0){
        b -> style += "\ttop: " + to_string(by) + "%;\n";
    }
    return t;
}

//get size
double Tag :: S(){
    return (br.first - tl.first) * (br.second - tl.second);
}

//get width
double Tag :: W(){
    return br.second - tl.second;
}

//get height
double Tag :: H(){
    return br.first - tl.first;
}

//get parent(useful for updating %)
Tag * Tag :: P(){
    return parent;
}

//for toSourceCode
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

//for toSourceCode
string Tag :: closeTag(){
    if(name == "img"){
        return "";
    }
    return "</" + name + ">\n";
}
