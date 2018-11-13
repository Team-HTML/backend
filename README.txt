
Dongyao Zhu

****************************************************************************
basic structure / workflow:

generator.py
    
    This will be the programme to run on server. It should take care of 
    correcting and parsing ML output.
    It should use HTML class's functions to generate the code. 

HTML.py

    This will have the core structure and algorithm that together make a 
    html tree from tags' positions on the page. 

Tag.py

    This will be the supporting tags for HTML class. A Tag should include 
    complete information for a html tag, plus its RELATIVE positions on the 
    webpage. Refer to the files for more information on coordinates.

Deprecated: HTML.cpp, Tag.cpp, test.cpp
****************************************************************************

version 1.3

    from 1.2:

        position styles are now written as inline style instead of in
        a separate css file, for the user to focus on theme style 
        editing and not distracted by positions

        when iterating the tree, all html body and css style will be 
        stored in a string to be written at once, instead of writting 
        part by part, for the sake of better i/o efficiency

        paragraphs now show a defaul text

        TODO: error tolerance in __lt__ of Tag

version 1.2

    from 1.1:
        
        rewritten in python, as requested by server team
        redesigned structure, since parser is no longer needed
            HTML now takes in raw list of tags
            HTML now calls makeTree in constructor
        TODO: error tolerance in __lt__ of Tag

version 1.1

    from 1:

        made better code style
        memory bug still exists
        TODO: parser, error check

        
