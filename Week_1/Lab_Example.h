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
    int numAuthors;
    void constructionHelper(const std::string, const bool, const std::string*, const int);
public:

    Manga();
    Manga(const std::string, const bool, const std::string*, const int, const int, const std::string, const int);
    Manga(const Manga&);
    ~Manga();

    Manga& operator=(const Manga&);

    std::string getLanguage() const;
    void setLanguage(const std::string);
    bool getColour() const;
    void setColour(const bool);
    std::string* getAuthors() const;
    void setAuthors(const std::string*, const int);
    int getNumAuthors() const;

    std::ostream& displayManga(std::ostream&) const;
    friend std::ostream& operator<<(std::ostream&, const Manga);
};

#endif