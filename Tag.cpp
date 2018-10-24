
#include "Tag.hpp"

Tag :: ~Tag(){
    //TODO delete all children
}

bool Tag :: operator < (const Tag & other){
    double diff = size - other.size;
    if(diff > 0.05 * other.size){
        return false;
    }
    if(diff < -0.05 * size){
        return true;
    }
    return tl.first < other.tl.first ? false :
        tl.first > other.tl.first ? true :
        tl.second < other.tl.second ? false : true;
}
        

bool Tag :: within(Tag * other);

double Tag :: S(){
    return size;
}


