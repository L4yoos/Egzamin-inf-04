import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
/**
 ******************************************************
 nazwa klasy:   AppComponent
 pola:          film - obiekt przechowujący tytuł i kategorię filmu
 metody:        dodajFilm, void – wypisuje dane wprowadzone do formularza w konsoli
 informacje:    Komponent reprezentuje formularz do wprowadzania filmów
 autor:         00000000000000
 ******************************************************
 */
export class AppComponent {
  film = {
    tytul: '',
    kategoria: ''
  };

  dodajFilm() {
    console.log({
      tytul: this.film.tytul,
      kategoria: this.film.kategoria
    });
  }
}
