#include "Lab_Example.h"

// as this function is meant to be in the constructor, it does not call delete on authors
void Manga::constructionHelper(const std::string language, 
    const bool colour, const std::string* authors, const int numAuthors){
    this->language.assign(language);
    this->colour = colour;
    this->authors = new std::string[numAuthors];
    for (int i = 0; i < numAuthors; ++i){
        this->authors[i].assign(authors[i]);
    }
    this->numAuthors = numAuthors;
}


Manga::Manga() : Book(){
    constructionHelper("", false, nullptr, 0);
}

Manga::Manga(const std::string language, const bool colour, 
    const std::string* authors, const int numAuthors, 
    const int id, const std::string titl, const int len) : 
    Book(id, titl, len){
    constructionHelper(language, colour, authors, numAuthors);
}

Manga::Manga(const Manga& other) : Book(other){
    constructionHelper(other.getLanguage(), other.getColour(),
        other.getAuthors(), other.getNumAuthors());
}

Manga::~Manga(){
    if(authors){
        delete [] authors;
    }
    authors = nullptr;
}

Manga& Manga::operator=(const Manga& other){
    if(this != &other){
        if(authors){
            delete [] authors;
            authors = nullptr;
        }
        constructionHelper(other.getLanguage(), other.getColour(), 
            other.getAuthors(), other.getNumAuthors());
    }
    return *this;
}

std::string Manga::getLanguage() const{
    return language;
}

bool Manga::getColour() const{
    return colour;
}

std::string* Manga::getAuthors() const{
    return authors;
}

void Manga::setAuthors(const std::string* authors, const int numAuthors){
    if (this->authors){
        delete[] this->authors;
    }
    this->authors = new std::string[numAuthors];
    for (int i = 0; i < numAuthors; ++i){
        this->authors[i].assign(authors[i]);
    }
    this->numAuthors = numAuthors;
}

int Manga::getNumAuthors() const{
    return numAuthors;
}

std::ostream& Manga::displayManga(std::ostream& os) const{
    Book::displayBook(os);
    os << "Language: " << language << std::endl;
    os << "Colour: " << (colour ? "Yes" : "No") << std::endl;
    os << "Authors: " << (numAuthors ? authors[0] : "") << std::endl;
    for (int i = 1; i < numAuthors; ++i){
        os << "         " << authors[i] << std::endl;
    }
    return os;
}
std::ostream& operator<<(std::ostream& os, const Manga manga){
    return manga.displayManga(os);
}

int main(){
    Manga m("Sousou no Frieren", false, nullptr, 0, 54782572, "English", 132);
    Manga m2 = m;

    std::string* authors = new std::string [2];
    authors[0] = "Kanehito Yamada";
    authors[1] = "Abe Tsukasa";
    m2.setAuthors(authors, 2);

    std::cout << (Book)m << std::endl;
    std::cout << m2;
}