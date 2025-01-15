package com.example.inf4_st24_prak2

import android.os.Bundle
import android.widget.*
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Referencje do kontrolek
        val ownerNameEditText: EditText = findViewById(R.id.editTextText)
        val speciesListView: ListView = findViewById(R.id.listView)
        val ageSeekBar: SeekBar = findViewById(R.id.seekBar)
        val ageEditText: TextView = findViewById(R.id.textView3)
        val visitPurposeEditText: EditText = findViewById(R.id.editTextText8)
        val visitTimeEditText: EditText = findViewById(R.id.editTextTime)
        val okButton: Button = findViewById(R.id.button)
        val resultTextView: TextView = findViewById(R.id.textView7)

        // Przygotowanie danych dla Spinnera (Gatunek)
        val speciesOptions = arrayOf("Pies", "Kot", "Świnka morska")
        val adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, speciesOptions)
        speciesListView.adapter = adapter

        // Zmiana wartości maksymalnej suwaka w zależności od wybranego gatunku
        speciesListView.setOnItemClickListener { parent, view, position, id ->
            when (position) {
                0 -> ageSeekBar.max = 18
                1 -> ageSeekBar.max = 20
                2 -> ageSeekBar.max = 9
            }

            ageSeekBar.progress = 0
            ageEditText.text = "ile ma lat?"
        }

        // Zmiana wartości wieku na podstawie suwaka
        ageSeekBar.setOnSeekBarChangeListener(object : SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
                ageEditText.setText("ile ma lat? " + progress.toString())
            }

            override fun onStartTrackingTouch(seekBar: SeekBar?) {}
            override fun onStopTrackingTouch(seekBar: SeekBar?) {}
        })

        // Obsługa przycisku "OK"
        okButton.setOnClickListener {
            val ownerName = ownerNameEditText.text.toString()
            val selectedPosition = speciesListView.checkedItemPosition

            if (selectedPosition == -1) {
                Toast.makeText(this, "Proszę wybrać gatunek z listy!", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }

            val species = speciesOptions[selectedPosition]

            val age = ageSeekBar.progress
            val visitPurpose = visitPurposeEditText.text.toString()
            val visitTime = visitTimeEditText.text.toString()

            val result = "Właściciel: $ownerName, Gatunek: $species, Wiek: $age, Cel wizyty: $visitPurpose, Czas wizyty: $visitTime"
            resultTextView.text = result
        }
    }
}
