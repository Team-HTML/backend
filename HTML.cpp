//Dongyao Zhu

#include "HTML.hpp"

/*
 * name: constructor
 * description: builds the HTML tree structure from the tags
        row by row, each row determined by a reference tag that 
        starts most topleft and spans most row.
 * input: size of window, a priority queue of tags, given in the generator.cpp
 * output: a HTML tree
 */
HTML :: HTML(double width, double height, 
    priority_queue<Tag *, vector<Tag *>, TagPtrComp> & tags){

    root = new Tag(0, 0, width, height, "body", "", 
        "\tbackground-color: #293030;\n");
    double last = 0;
    //while all not finished
    while(!tags.empty()){
        Tag * current = tags.top();
        //this pq will store all tags in this row
        priority_queue<Tag *, vector<Tag *>, sortS> row;
        tags.pop();
        //while this row not finished
        while(!tags.empty()){
            Tag * next = tags.top();
            //next is below(it is in next row), moving to next row
            if(current -> botRightY() <= next -> topLeftY()){
                break;
            }else{
                //valid relations: next tag is NOT BELOW reference, which
                //may need to include more rows if next protrudes downwards
                current = current -> expandRow(next);
                row.push(next);
                tags.pop(); 
            }
        }//end of while
        row.push(current);
        //wrap row elements 2 by 2 then push back, think of huffman encoding
        //note: not really necessary, but will make html structure more clear
        while(row.size() > 1){
            Tag * a = row.top();
            row.pop();
            Tag * b = row.top();
            row.pop();
            row.push(Tag :: wrap(a, b));
        }
        //the final gigantic wrapped element
        if(row.size() == 1){
            Tag * t = row.top();
            //see Tag for relative position math
            double moveY = t -> topLeftY() - last;
            t -> style += "\ttop: " + to_string(moveY) + "%;\n";
            t -> style += "\tleft: " + to_string(t -> topLeftX()) + "%;\n";
            //total vertical adjustments
            last = t -> botRightY() - (moveY > 0 ? moveY : 0);
            t -> parent = root;
            root -> children.push_back(t);
            row.pop();
        }
    }//end of while
}//HTML

/*
 * name: destructor
 * description: delegate to Tag's destructor
 * input/output: none
 */
HTML :: ~HTML(){
    delete root;
}

/*
 * name: write
 * description: generate HTML and CSS source code from html structure tree, DFS
 * input: a designated path to store the file, a string css file path
 * output: whether successfully written a html and css file to the path
 */
bool HTML :: write(string pathHTML, string pathCSS){
    ofstream html(pathHTML);
    ofstream css(pathCSS);
    if(!root || !html.is_open() || !css.is_open()){
        return false;
    }
    writeHeader(html, pathCSS);
    writeSize(css);
    string tab = "\t";
    for(Tag * t : root -> children){
        helper(html, css, t, tab);
    }
    html << "</body>\n</html>\n";
    html.close();
    css.close();
    return true;
}

void HTML :: addStyle(string pathCSS){
    moreCSS += "\t<link rel=\"stylesheet\" type=\"text/css\" href=\"" + 
        pathCSS + "\">\n";
}

/*
 * name: writeHeader
 * description: writes out necessary HTML beginning information and css links
 * input: an ofstream & to write, a string of css link
 * output: none
 */
void HTML :: writeHeader(ofstream & html, string pathCSS){
    html << header << moreCSS << css << pathCSS << "\">\n</head>\n<body>\n";
}

/*
 * name: writeSize
 * description: writes webpage size to CSS
 * input: ofstream &
 * output: none
 */
void HTML :: writeSize(ofstream & css){
    css << "body{\n" << root -> style 
        << "\twidth: " << root -> W()
        << "vw;\n\theight: " << root -> H()
        << "vw;\n}\n";
}

/*
 * name: helper
 * description: write helper
 * input: same as write
 * output: none
 */
void HTML :: helper(ofstream & html, ofstream & css, 
    Tag * current, string tabs){

    html << tabs << current -> openTag();
    //write id(CHANGE TO ACTUAL CONTENT) except for wrappers
    if(current -> cls != "wrap"){
        html << tabs << "\t" << current -> id << endl;
    }
    //write style
    if(current -> style != ""){
        css << "#" << current -> id << "{\n" << current -> style
            << "\twidth: " << current -> wPct
            << "%;\n\theight: " << current -> hPct  
            << "%;\n}\n\n";
    }
    //running DFS for the html structure
    for(Tag * t : current -> children){
        helper(html, css, t, tabs + "\t");
    }
    html << tabs << current -> closeTag();
}

//eof