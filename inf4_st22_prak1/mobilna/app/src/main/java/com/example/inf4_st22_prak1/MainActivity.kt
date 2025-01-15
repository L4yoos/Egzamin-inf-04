package com.example.inf4_st22_prak1

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.appcompat.widget.AppCompatButton

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        val email: EditText = findViewById(R.id.editTextTextEmailAddress)
        val password: EditText = findViewById(R.id.editTextTextPassword)
        val passwordConfirm: EditText = findViewById(R.id.editTextTextPassword2)
        val button: Button = findViewById(R.id.button)
        val tekst: TextView = findViewById(R.id.rezultat)

        tekst.text = "Autor: 0000000000000"

        button.setOnClickListener {
            val email = email.text.toString()
            val pass = password.text.toString()
            val passCon = passwordConfirm.text.toString()

            if (!email.contains("@")) {
                tekst.text = "Nieprawidłowy adres e-mail."
            }
            else if (pass != passCon ) {
                tekst.text = "Hasła się różnią."
            }
            else {
                tekst.text = "Witaj $email"
            }
        }
    }
}