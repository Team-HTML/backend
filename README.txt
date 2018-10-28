
Dongyao Zhu

basic structure:

test.cpp or generator.cpp
    
    This will be the programme to run on server. It should take care of 
    correcting and parsing ML output, if that's not handled by ML group. 
    It should use HTML class's functions to generate the code. 
    Before ML group gives an example output, I will not start writing 
    the parser, but only manually enter the coordinates.

HTML.cpp

    This will have the core structure and algorithm that together make a 
    html tree from tags' positions on the page. 
    It should be responsive to different screen sizes.
    It should include CSS as well. I will look into including links as well.

Tag.cpp

    This will be the supporting tags for HTML class. A Tag should include 
    complete information for a html tag, plus its RELATIVE positions on the 
    webpage. Refer to the files for more information on coordinates.
