//Dongyao Zhu

#include "HTML.hpp"

/*
 * name: constructor
 * TODO
 */
HTML :: HTML(string filePath){
    root = new Tag(0, 0, 1, 100, "head", "", "", "");
    priority_queue<Tag *, vector<Tag *>, TagPtrComp> tags = parse(filePath);
    while(!tags.empty()){
        cout << *(tags.top()) << endl;
        delete tags.top();
        tags.pop();
    }  
}

/*
 * name: constructor
 * TODO
 */
HTML :: HTML(priority_queue<Tag *, vector<Tag *>, TagPtrComp> & tags){
    root = new Tag(0, 0, 100, 100, "body", "", "", "\tbackground-color: #293030;\n");
    double last = 0;
    //while all not finished
    while(!tags.empty()){
        Tag * current = tags.top();
        //cout << "current: " << *current << endl;
        priority_queue<Tag *, vector<Tag *>, sortS> row;
        tags.pop();
        //while row not finished
        while(!tags.empty()){
            Tag * next = tags.top();
            //cout << "next: " << *next << endl;
            int relation = current -> relation(next);
            //next is below(next row), moving to next row
            if(relation == ABOVE){
                break;
            }
            //valid relation, save in row
            else if(relation == LEFT || relation == RIGHT){
                //cout << "   is left / right, push next to row\n";
                current = current -> expandRow(next);//shoud include more rows
                row.push(next);
                tags.pop(); 
            }
            //valid relation, save in row
            else if(relation == SUPER){
                //cout << "   is super, push next to row";
                row.push(next);
                tags.pop();
            }
            //this is a debatable solution
            else if(relation == OVERLAP){
                //cout << "   OVERLAP, push next to row\n";
                row.push(next);
                tags.pop();
            }
        }//end of while
        //cout << "   row done, pushing this to row\n";
        row.push(current);
        //cout << "row size: " << row.size() << endl;
        //think of huffman encoding
        while(row.size() > 1){
            //cout << "   wrapping: \n";
            Tag * a = row.top();
            row.pop();
            Tag * b = row.top();
            row.pop();
            //cout << "       " << *a << endl;
            //cout << "       " << *b << endl;
            Tag * w = Tag :: wrap(a, b);
            row.push(w);
            //cout << "   wrapped to " << *w << endl;
        }
        if(row.size() == 1){
            Tag * t = row.top();
            double moveY = t -> tl.first - last;
            t -> style += "\ttop: " + to_string(moveY) + "%;\n";
            t -> style += "\tleft: " + to_string(t -> tl.second) + "%;\n";
            last = t -> br.first - (moveY > 0 ? moveY : 0);
            t -> parent = root;
            root -> children.push_back(t);
            row.pop();
        }
    }//end of while
/*    for(auto it = root -> children.begin(); 
            it != root -> children.end(); ++it){
        cout << "body's children: " << **it << endl;
    }*/
}//HTML

/*
 * name: destructor
 */
HTML :: ~HTML(){
    cout << "~ " << this << endl;
    delete root;
}

/*
 * name: parse
 * description: read tags from file (json?) from given file path
 * input: a string of the file path
 * output: a vector of tag * read from the file
 */
priority_queue<Tag *, vector<Tag *>, TagPtrComp> HTML :: parse(string filePath){
    priority_queue<Tag *, vector<Tag *>, TagPtrComp> pq;
    return pq;
}

/*
 * name: toSourceCode
 * description: generate HTML and CSS source code from html structure tree, DFS
 * input: a designated path to store the file
 * output: whether successfully written a html and css file to the path
 */
bool HTML :: toSourceCode(string pathHTML, string pathCSS){
    if(!root){
        return false;
    }
    ofstream html(pathHTML);
    html << "<!DOCTYPE html>\n<html>\n" << 
        "<head>\n\t<meta name = \"viewport\" content = \"" << 
        "width = device-width, initial-scale = 1, " << 
        "maximum-scale = 1.0, user-scalable = 0\"/>\n" <<
        "\t<link rel=\"stylesheet\" type=\"text/css\" href=\"";
    html << pathCSS << "\">\n</head>\n";
    ofstream css(pathCSS);
    helper(html, css, root, 0);
    html << "</html>\n";
    html.close();
    css.close();
    return true;
}

//running DFS for a more clear html structure
void HTML :: helper(ofstream & html, ofstream & css, Tag * current, int tabCount){
    //cout << "visiting " << (*current) << endl;
    string tabs = "";
    for(int i = 0; i < tabCount; i++){
        tabs += "\t";
    }
    html << tabs << current -> openTag();
    if(current -> name != "div" && current -> name != "body"){
        html << tabs << "\t" << current -> name << "; " << current -> id << endl;
    }
    if(current -> style != ""){
        css << "#" << current -> id << "{\n" << current -> style
            << "\twidth: " << current -> wPct
            << (current -> name == "body" ? "vw" : "%")
            << ";\n\theight: " << current -> hPct 
            << (current -> name == "body" ? "vw" : "%") 
            << ";\n}\n\n";
    }
    for(Tag * t : current -> children){
        helper(html, css, t, tabCount + 1);
    }
    html << tabs << current -> closeTag();
}
