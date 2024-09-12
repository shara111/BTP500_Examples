#include "Book.h"

Book::Book(){
    bookID = -1;
    bookTitle.assign("");
    pageLength = -1;
}

Book::Book(const int num, const std::string title, const int length){
    bookID = num;
    bookTitle.assign(title);
    pageLength = length;
}

Book::Book(const Book& other){
    bookID = other.bookID;
    bookTitle.assign(other.bookTitle);
    pageLength = other.pageLength;
}


int Book::getBookID() const{
    return bookID;
}

void Book::setBookID(int ID){
    bookID = ID;
}

std::string Book::getBookTitle() const{
    return bookTitle;
}

void Book::setBookTitle(const std::string title){
    bookTitle.assign(title);
}

int Book::getPageLength() const{
    return pageLength;
}

void Book::setPageLength(const int len){
    pageLength = len;
}

std::ostream& Book::displayBook(std::ostream& os) const{
    os << "Book Number: " << this->bookID << std::endl;
    os << "Book Title: " << this->bookTitle << std::endl;
    os << "Page Length: " << this->pageLength << std::endl;

    return os;
}

std::ostream& operator<<(std::ostream& os, const Book book){
    return book.displayBook(os);
}