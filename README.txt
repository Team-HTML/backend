
Dongyao Zhu

****************************************************************************
basic structure / workflow:

test.cpp or generator.cpp
    
    This will be the programme to run on server. It should take care of 
    correcting and parsing ML output.
    It should use HTML class's functions to generate the code. 

HTML.cpp

    This will have the core structure and algorithm that together make a 
    html tree from tags' positions on the page. 

Tag.cpp

    This will be the supporting tags for HTML class. A Tag should include 
    complete information for a html tag, plus its RELATIVE positions on the 
    webpage. Refer to the files for more information on coordinates.
****************************************************************************

version 1.1

    from 1:

        made better code style
        memory bug still exists
        TODO: parser, error check

        
