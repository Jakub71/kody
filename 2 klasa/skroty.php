<?php
    // funkcje skrótu
    $tekst = 'kort';
    echo hash('sha1', $tekst);
    echo "\n";
    echo hash('sha256', $tekst);
    echo "\n";
    $haslo = 'kort';
    echo hash('sha1', $haslo);
?>
