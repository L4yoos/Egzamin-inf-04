package com.example.inf4_st23_prak2

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.recyclerview.widget.DividerItemDecoration
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MainActivity : AppCompatActivity() {

    private val notesList = mutableListOf<String>()
    private lateinit var notesAdapter: NotesAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Inicjalizacja RecyclerView
        val recyclerView: RecyclerView = findViewById(R.id.notesRecyclerView)
        recyclerView.layoutManager = LinearLayoutManager(this)

        // Inicjalizacja adaptera
        notesAdapter = NotesAdapter(notesList)
        recyclerView.adapter = notesAdapter

        val itemDecoration = DividerItemDecoration(this, DividerItemDecoration.VERTICAL)
        itemDecoration.setDrawable(resources.getDrawable(R.drawable.seperator, null)) // Użycie własnego separatora
        recyclerView.addItemDecoration(itemDecoration)

        // Inicjalizacja pola edycyjnego i przycisku
        val noteEditText: EditText = findViewById(R.id.editTextText)
        val addNoteButton: Button = findViewById(R.id.button)

        // Ustawienie akcji przycisku "DODAJ"
        addNoteButton.setOnClickListener {
            val noteText = noteEditText.text.toString()
            if (noteText.isNotEmpty()) {
                // Dodanie nowej notatki do listy
                notesList.add(noteText)
                notesAdapter.notifyItemInserted(notesList.size - 1) // Odświeżenie widoku listy

                // Wyczyść pole edycyjne
                noteEditText.text.clear()
            } else {
                // Komunikat w przypadku pustego pola
                Toast.makeText(this, "Proszę wpisać treść notatki", Toast.LENGTH_SHORT).show()
            }
        }

        // Wstępne dane - 3 notatki
        notesList.add("Zakupy: chleb, masło, ser")
        notesList.add("Do zrobienia: obiad, umyć podłogi")
        notesList.add("weekend: kino, spacer z psem")
        notesAdapter.notifyDataSetChanged()
    }
}