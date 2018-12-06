# wordcounter
A python program that analyzes a document and tracks the frequency of each unique word

The program is able to:                                                             

  Prompt user for file name                                                                           
    Ensure file is of .txt variety                                                                                      
    
  Open and read the contents of that file into a text string                                                          
    Sanitize the string and remove characters other than letters and spaces                                               
    Return the word count of that sanitized text string                                                                       
  
  Scan through the text file word by word                                                                                           
    Keep a list of lists containing 2 items: A word and its # of occurances                                                           
    Add to the list any new word it comes across and give it a count of 1                                                         
    Increment the count of a word already in the list by 1 for each subsequent occurance                                            
    Sort the lists by # of occurances descending                                                                                  
    Calculate each words occurance percentage, and append it to that words sub-list in the main list                                
    Print each entry in the list                                                                                              
   
To use:                                                                                                                             
  Run wordcounter.py                                                                                                            
  You will be prompted to enter a file name or patch name. If you do not enter a .txt file, you will be reprompted                  
  The scanner will then work with your file. Depending on the length of the file, it can take anywhere from seconds to an hour.         
  The results will then be printed to you on screen.                                                                                                                  
  
Goals for the future:                                                                                                                                     
  Had trouble removing '-' from text, as some words such as re-iterate require it, but other times its used as a space or pause indicator
  Would like to have a visual representation of the results rather than just percents. Something like a graph, or outputing even to a .csv file for use in external programs
  The ability to store output in an external file for easier eye-consumption
  A progress bar to show how far along the process is. Long text files such as War and Peace kinda leave you hanging for a long time
