//Dongyao Zhu

#ifndef HTML_HPP
#define HTML_HPP
#include "Tag.hpp"
#include <vector>
#include <queue>
#include <stack>
#include <iostream>
#include <fstream>
using namespace std;

class TagPtrComp{
    public:
        bool operator() (Tag * & lhs, Tag * & rhs) const{
            return *lhs < *rhs;
        }
};

class HTML{

        Tag * root;

    public:

        HTML(string filePath);

        HTML(priority_queue<Tag *, vector<Tag *>, TagPtrComp> & tags);

        ~HTML();

        priority_queue<Tag *, vector<Tag *>, TagPtrComp> parse(string filePath);

        bool toSourceCode(string pathHTML, string pathCSS);

        void helper(ofstream & html, ofstream & css, Tag * current, int count);

};

#endif
