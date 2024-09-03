#ifndef BOOK_H
#define BOOK_H

#include <iostream>

/*
* Here, I am creating a Book class which will be a 
* parent class for a Manga class.
*/

class Book{
protected:
    int bookID;
    std::string bookTitle;
    int pageLength;
public:
    Book();
    Book(int, std::string, int);
    Book(Book&);

    int getBookID();
    void setBookID(int);

    std::string getBookTitle();
    void setBookTitle(std::string);

    int getPageLength();
    void setPageLength(int);

    std::ostream& displayBook(std::ostream&);
};

#endif