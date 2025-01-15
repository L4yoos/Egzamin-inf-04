package com.example.inf4_cz22_prak1

import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {
    private var polubienia = 0;

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        val polub: Button = findViewById(R.id.button)
        val usun: Button = findViewById(R.id.button2)
        val zapisz: Button = findViewById(R.id.button3)
        val licznik: TextView = findViewById(R.id.textView2)

        polub.setOnClickListener {
            polubienia++
            licznik.text = "$polubienia polubień"
        }

        usun.setOnClickListener {
            if (polubienia > 0)
            {
                polubienia--
            }
            licznik.text = "$polubienia polubień"
        }
    }
}