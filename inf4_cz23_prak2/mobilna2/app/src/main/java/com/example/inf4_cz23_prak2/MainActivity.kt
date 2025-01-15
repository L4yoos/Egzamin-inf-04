package com.example.inf4_cz23_prak2

import android.os.Bundle
import android.widget.Button
import android.widget.SeekBar
import android.widget.TextView
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.example.inf4_cz23_prak2.ui.theme.Inf4_cz23_prak2Theme

class MainActivity : ComponentActivity() {
    private var index = 1;

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.main)

        val suwak: SeekBar = findViewById(R.id.suwak);
        val rozmiar: TextView = findViewById(R.id.textView2);
        val cytat: TextView = findViewById(R.id.textView3);
        val btn: Button = findViewById(R.id.button);

        suwak.setOnSeekBarChangeListener(object : SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(
                seekBar: SeekBar?,
                progress: Int,
                fromUser: Boolean
            ) {
                rozmiar.text = "Rozmiar $progress"
                cytat.textSize = progress.toFloat()
            }

            override fun onStartTrackingTouch(seekBar: SeekBar?) {

            }

            override fun onStopTrackingTouch(seekBar: SeekBar?) {

            }
        })

        val cytaty = arrayOf("Dzień Dobry", "Good morning", "Buenos dias")

        btn.setOnClickListener {
            if(index == 3) index = 0
            cytat.text = cytaty[index]
            index++
        }
    }
}

@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello $name!",
        modifier = modifier
    )
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    Inf4_cz23_prak2Theme {
        Greeting("Android")
    }
}