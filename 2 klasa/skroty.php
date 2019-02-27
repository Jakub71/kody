<?php
    // funkcje skrótu
    $tekst = 'Siemanko';
    echo hash('sha1', $tekst);
    echo "\n";
    echo hash('sha256', $tekst);
    echo "\n";
    $haslo = 'bardzo tajne itemki';
    echo hash('sha1', $haslo);
?>
