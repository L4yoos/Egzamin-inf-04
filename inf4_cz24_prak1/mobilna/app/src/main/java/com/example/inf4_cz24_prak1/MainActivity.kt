package com.example.inf4_cz24_prak1

import android.os.Bundle
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import kotlin.random.Random

class MainActivity : AppCompatActivity() {

    private lateinit var diceImages: Array<ImageView>
    private lateinit var rollButton: Button
    private lateinit var resetButton: Button
    private lateinit var rollResultTextView: TextView
    private lateinit var gameResultTextView: TextView

    private var gameScore = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        diceImages = arrayOf(
            findViewById(R.id.dice1),
            findViewById(R.id.dice2),
            findViewById(R.id.dice3),
            findViewById(R.id.dice4),
            findViewById(R.id.dice5)
        )
        rollButton = findViewById(R.id.button)
        resetButton = findViewById(R.id.button2)
        rollResultTextView = findViewById(R.id.wynik)
        gameResultTextView = findViewById(R.id.wynikgry)

        rollButton.setOnClickListener {
            val diceValues = IntArray(5)
            val diceCount = IntArray(7) { 0 }
            var rollScore = 0

            // Losowanie wartości dla każdej kości i ustawianie odpowiedniego obrazu
            for (i in diceImages.indices) {
                val value = Random.nextInt(1, 7) // Losowanie liczby od 1 do 6
                diceValues[i] = value
                diceCount[value]++ // Aktualizowanie liczby wystąpień wylosowanej wartości
                diceImages[i].setImageResource(getDiceImage(value))
            }

            // Obliczanie wyniku rzutu
            for (value in 1..6) {
                if (diceCount[value] >= 2) {
                    rollScore += value * diceCount[value]
                }
            }

            // Aktualizacja wyniku rzutu i całkowitego wyniku gry
            rollResultTextView.text = "Wynik rzutu: $rollScore"
            gameScore += rollScore
            gameResultTextView.text = "Wynik gry: $gameScore"
        }

        resetButton.setOnClickListener {
            // Resetowanie obrazów kości do question.jpg
            for (dice in diceImages) {
                dice.setImageResource(R.drawable.question)
            }

            // Resetowanie wyników
            rollResultTextView.text = "Wynik rzutu: 0"
            gameResultTextView.text = "Wynik gry: 0"
            gameScore = 0
        }
    }

    private fun getDiceImage(value: Int): Int {
        return when (value) {
            1 -> R.drawable.k1
            2 -> R.drawable.k2
            3 -> R.drawable.k3
            4 -> R.drawable.k4
            5 -> R.drawable.k5
            6 -> R.drawable.k6
            else -> R.drawable.question
        }
    }
}