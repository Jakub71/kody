typedef struct ELEMENT{
    int value;
    ELEMENT *next;
}ELEMENT;

typedef struct HEADER{
    ELEMENT *head;
    ELEMENT *tail;
}HEADER;

class Lista {
    private:// hermetyzacja danych
        HEADER header;//blok info
    public:
        Lista();//konstructor oba nic nie zwracają
        ~Lista();//destructor 
        void Dodaj(int);
        bool Wstaw(int, int);
        int Usun();
        bool Usun(int); // przeciążanie metod
        void Wyswietl();
        bool Pusta();
};
