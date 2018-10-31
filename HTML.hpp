//Dongyao Zhu

#ifndef HTML_HPP
#define HTML_HPP
#include "Tag.hpp"
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>

using namespace std;

//for priority queue
class TagPtrComp{
    public:
        bool operator() (Tag * & lhs, Tag * & rhs) const{
            return *lhs < *rhs;
        }
};

class HTML{

        const string header = "<!DOCTYPE html>\n<html>\n"
            "<head>\n\t<meta name = \"viewport\" content = \""
            "width = device-width, initial-scale = 1, "
            "maximum-scale = 1.0, user-scalable = 0\"/>\n";

        const string css = 
            "\t<link rel=\"stylesheet\" type=\"text/css\" href=\"";

        string moreCSS = "";

        Tag * root;
        
        void helper(ofstream & html, ofstream & css, 
            Tag * current, string tabs);

        void writeHeader(ofstream & html, string pathCss);

        void writeSize(ofstream & css);

    public:

        HTML(double width, double height, 
            priority_queue<Tag *, vector<Tag *>, TagPtrComp> & tags);

        ~HTML();

        bool write(string pathHTML, string pathCSS);

        void addStyle(string pathCSS);

};

#endif
