#include "HTML.hpp"

using namespace std;

int main(int argc, char** argv){
    HTML * html = new HTML(argv[1]);
    html -> toHTML("out.html");
    delete html;
}
