//Dongyao Zhu

/*
TODO
implement ignoring minor error in a function, possibly takes an argument specifying
    how much error is allowed
idea: for i in all values, if a very close i appeared before, set i to that value

TODO
add test cases, write coordinates as in percentage of the whole page.
see Tag.hpp for coordinate definitions.

TODO
implement a parser, input is hopefully in json format, could 
    search for an existing library for that part. The output could be 
    a priority_queue.

TODO
note that test1 has the bottom right box off a bit because it is using <p> tags
I will work on that
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
    pq.push(new Tag(10, 10, 40, 90, "p", "box1", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(60, 10, 90, 40, "p", "box2", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(60, 60, 70, 90, "p", "box3", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(80, 60, 90, 90, "p", "box4", "", "\tborder: 2px solid white;\n"));
    HTML * html1 = new HTML(pq);
    html1 -> toSourceCode("test1.html", "test1.css");
    delete html1;

    cout << "**********************test2************************\n";
    pq.push(new Tag(20, 40, 80, 60, "div", "bar", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(40, 10, 60, 30, "div", "img", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(40, 70, 60, 90, "div", "img", "", "\tborder: 2px solid white;\n"));
    HTML * html2 = new HTML(pq);
    html2 -> toSourceCode("test2.html", "test2.css");
    delete html2;  

    cout << "**********************test3************************\n";
    pq.push(new Tag(10, 10, 60, 40, "div", "bar", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(40, 60, 90, 90, "div", "img", "", "\tborder: 2px solid white;\n"));
    HTML * html3 = new HTML(pq);
    html3 -> toSourceCode("test3.html", "test3.css");
    delete html3;  

    cout << "**********************test4************************\n";
    pq.push(new Tag(10, 10, 40, 90, "div", "img", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(15, 20, 20, 80, "div", "p", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(25, 20, 30, 80, "div", "p", "", "\tborder: 2px solid white;\n"));

    pq.push(new Tag(60, 10, 70, 40, "div", "bar", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(50, 20, 80, 30, "div", "bar", "", "\tborder: 2px solid white;\n"));

    pq.push(new Tag(50, 60, 60, 80, "div", "box", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(50, 80, 70, 90, "div", "box", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(70, 70, 80, 90, "div", "box", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(60, 60, 80, 70, "div", "box", "", "\tborder: 2px solid white;\n"));

    HTML * html4 = new HTML(pq);
    html4 -> toSourceCode("test4.html", "test4.css");
    delete html4;  

    cout << "**********************test5************************\n";
    pq.push(new Tag(10, 10, 15, 90, "div", "wrap", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(26, 10, 40, 90, "div", "wrap", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(60, 10, 85, 90, "div", "wrap", "", "\tborder: 2px solid white;\n"));
    pq.push(new Tag(90, 10, 95, 90, "div", "wrap", "", "\tborder: 2px solid white;\n"));

    HTML * html5 = new HTML(pq);
    html5 -> toSourceCode("test5.html", "test5.css");
    delete html5; 
}
