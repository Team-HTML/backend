//Dongyao Zhu

/*
TODO
implement ignoring minor error in a function, possibly takes an argument specifying
    how much error is allowed
idea: for i in all values, 
    if a very close value appeared before(use set), 
    set i to that value

TODO
find a json parser online, or rewrite everything in python.

*/

#include "HTML.hpp"

using namespace std;

priority_queue<Tag *, vector<Tag *>, TagPtrComp> parse(string path){
    priority_queue<Tag *, vector<Tag *>, TagPtrComp> pq1;
    return pq1;
}

int main(int argc, char** argv){
    priority_queue<Tag *, vector<Tag *>, TagPtrComp> pq;

    cout << "**********************test1************************\n";
    pq.push(new Tag(10, 10, 40, 90, "p", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(60, 10, 90, 40, "p", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(60, 60, 70, 90, "p", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(80, 60, 90, 90, "p", "", "\tborder: 2px solid white;\n"));
    HTML * html1 = new HTML(100, 100, pq);
    html1 -> write("test1.html", "test1.css");
    delete html1;

    cout << "**********************test2************************\n";
    pq.push(new Tag(20, 40, 80, 60, "div", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(40, 10, 60, 30, "div", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(40, 70, 60, 90, "div", "", "\tborder: 2px solid white;\n"));
    HTML * html2 = new HTML(100, 100, pq);
    html2 -> write("test2.html", "test2.css");
    delete html2;  

    cout << "**********************test3************************\n";
    pq.push(new Tag(10, 10, 60, 40, "div", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(40, 60, 90, 90, "div", "", "\tborder: 2px solid white;\n"));
    HTML * html3 = new HTML(100, 100, pq);
    html3 -> write("test3.html", "test3.css");
    delete html3;  

    cout << "**********************test4************************\n";
    pq.push(new Tag(10, 10, 40, 90, "div", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(15, 20, 20, 80, "div", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(25, 20, 30, 80, "div", "", "\tborder: 2px solid white;\n"));

    pq.push(new Tag(60, 10, 70, 40, "div", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(50, 20, 80, 30, "div", "", "\tborder: 2px solid white;\n"));

    pq.push(new Tag(50, 60, 60, 80, "div", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(50, 80, 70, 90, "div", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(70, 70, 80, 90, "div", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(60, 60, 80, 70, "div", "", "\tborder: 2px solid white;\n"));

    HTML * html4 = new HTML(100, 100, pq);
    html4 -> write("test4.html", "test4.css");
    delete html4;  

    cout << "**********************test5************************\n";
    pq.push(new Tag(10, 10, 15, 90, "div", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(26, 10, 40, 90, "div", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(60, 10, 85, 90, "div", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(90, 10, 95, 90, "div", "", "\tborder: 2px solid white;\n"));

    HTML * html5 = new HTML(100, 100, pq);
    html5 -> write("test5.html", "test5.css");
    delete html5; 
}
