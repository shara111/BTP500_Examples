#ifndef MANGA_H
#define MANGA_H

#include "Book.h"
/*
* Today, we will create a Manga class which inherits from
* the Book class. It will have the following attributes:
*       std::string language
*       bool colour
*       std::string* authors
* As well as getters and setters, constructors, etc.
*/

class Manga : public Book{
    std::string language;
    bool colour;
    std::string* authors;
public:
    void constructionHelper(std::string, bool, std::string*);

    Manga();
    Manga(std::string, bool, std::string*, int, std::string, int);
    Manga(const Manga&);

    ~Manga();

    std::string getLang() const;
    bool getColour() const;
    std::string* getAuthors() const;

    Manga& operator=(const Manga&);
};

#endif