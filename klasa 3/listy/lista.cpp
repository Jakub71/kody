/*
 * lista.cpp
 */
#include <iostream>
#include "lista.h"

using namespace std;

Lista::Lista() {
    header.head = NULL;
    header.tail= NULL;
}


Lista::~Lista() {
    ;
    //while (header.head != NULL)
      //  Usun();
}

void Lista::Dodaj(int value) {
    ELEMENT *el = new ELEMENT;
    el->value = value;
    el->next = NULL;
    if (header.head == NULL){
        header.head = el;
        header.tail = el;
    } else {
        header.tail->next = el; // łaczenie elementów listy
        header.tail = el;
    }
}


void Lista::Wyswietl() {
    ELEMENT *el = header.head;
    while (el !=NULL) {
        cout << el->value << endl;
        el = el->next;
    }
}

int Lista::Usun() {
    if (header.head == Null)
        return 0;
    int value;
    if (header.head = header.tail) {
        value = header.head->value;
        delete header.head;
        header.head=header.tail = Null;
    } else {
        value = header.tail->value;
    }
    return value;
}
