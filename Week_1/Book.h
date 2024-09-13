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
    Book(const int, const std::string, const int);
    Book(const Book&);

    int getBookID() const;
    void setBookID(const int);

    std::string getBookTitle() const;
    void setBookTitle(const std::string);

    int getPageLength() const;
    void setPageLength(const int);

    std::ostream& displayBook(std::ostream&) const;
    friend std::ostream& operator<<(std::ostream&, const Book);
};

#endif