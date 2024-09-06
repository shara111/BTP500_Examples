#include "Lab_Example.h"

void Manga::constructionHelper(std::string lan,
    bool col, std::string* auth){
    language.assign(lan);
    colour = col;
    authors = auth ? auth : nullptr;
}


Manga::Manga() : Book(){
    constructionHelper("", false, nullptr);
}

Manga::Manga(std::string lang, bool col, std::string* auth,
    int id, std::string titl, int len) : 
    Book(id, titl, len){
    constructionHelper(lang, col, auth);
}

Manga::Manga(const Manga& other) : Book(other){
    constructionHelper(other.getLang(), other.getColour(),
        other.getAuthors());
}

Manga::~Manga(){
    if(authors){
        delete [] authors;
    }
    authors = nullptr;
}

std::string Manga::getLang() const{
    return language;
}

bool Manga::getColour() const{
    return colour;
}

std::string* Manga::getAuthors() const{
    return authors;
}

Manga& Manga::operator=(const Manga& other){
    if(this != &other){
        if(authors){
            delete [] authors;
            authors = nullptr;
        }
        //this->bookID = other.getBookID();

        language.assign(other.getLang());
        colour = other.getColour();
        authors = other.getAuthors();
    }

    return *this;
}

