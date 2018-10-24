
#include "HTML.hpp"

/*
 * name: constructor
 */
HTML :: HTML(string filePath){
    priority_queue<Tag *, vector<Tag *>, TagPtrComp> tags = parse(filePath);
    if(!tags.empty){
        root = tags.top();
        tags.pop();
    }
    while(!tags.empty()){
        Tag * current = tags.top();
        insert(current);
        tags.pop();
    }
    
}

/*
 * name: destructor
 */
HTML :: ~HTML(){
}

/*
 * name: insert
 * description: insert a tag into the html structure tree
 * input: a tag pointer to be inserted; the reason for not taking 
        a vector is that some may not be inserted successfully
 * output: whether the tag is successfully inserted
 */
bool HTML :: insert(Tag * tag){
    return false;
}

/*
 * name: remove
 * description: remove a tag from the html structure tree
 * input: a tag pointer to be removed; the reason for not taking 
 a vector is that some may not be removed successfully
 * output: whether the tag is successfully removed
 */
bool HTML :: remove(Tag * tag){
    return false;
}

/*
 * name: wrap
 * description: wrap up several tags into a new big tag (like a div)
 * input: a vector of tag * to be wrapped up, a string of their new name
 * output: new Tag * containing all tags
 */
Tag * HTML :: wrap(vector<Tag *> tags, string newTagName){
    return 0;
}

/*
 * name: dissect
 * description: breaks up a big tag into smaller tags
 * input: a pointer to a big tag *, a vector of tag * to get out from it
 * output: a vector of tag * that came out from the big tag
 */
vector<Tag *> HTML :: dissect(Tag * group, vector<Tag *> parts){
    return vector<Tag *>(5,0);
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
 * name: toHTML
 * description: generate html source code from html structure tree, DFS
 * input: a designated path to store the file
 * output: whether successfully written a html file to the path
 */
bool HTML :: toHTML(string path){
    return false;
}

