using System.Text;
using System.Windows.Controls;
using System.Windows;

namespace inf4_st23_prak1
{
    public partial class MainWindow : Window
    {
        // Pole do przechowywania hasła
        private string password;

        public MainWindow()
        {
            InitializeComponent();
        }

        private void generatePassword_Click(object sender, RoutedEventArgs e)
        {
            if (!int.TryParse(PasswordLength.Text, out int length) || length <= 0)
            {
                MessageBox.Show("Podaj prawidłową długość hasła!", "Błąd");
                return;
            }

            bool includeUppercase = Letters.IsChecked == true;
            bool includeDigits = Digits.IsChecked == true;
            bool includeSpecial = Special.IsChecked == true;

            if (!includeUppercase && !includeDigits && !includeSpecial)
            {
                MessageBox.Show("Musisz wybrać przynajmniej jedną opcję znaków!", "Błąd");
                return;
            }

            string lowerCase = "abcdefghijklmnopqrstuvwxyz";
            string upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            string digitsCase = "0123456789";  // Poprawiona lista cyfr
            string specialsCase = "!@#$%^&*()_+-=";

            StringBuilder characterSet = new StringBuilder();
            if (includeUppercase) characterSet.Append(lowerCase + upperCase);
            if (includeDigits) characterSet.Append(digitsCase);
            if (includeSpecial) characterSet.Append(specialsCase);

            Random random = new Random();
            char[] passwordArray = new char[length];
            for (int i = 0; i < length; i++)
            {
                passwordArray[i] = characterSet[random.Next(characterSet.Length)];
            }

            // Przechowujemy wygenerowane hasło w zmiennej klasy
            password = new string(passwordArray);

            MessageBox.Show($"{password}", "Generowanie hasła");
        }

        private void Confirm_Click(object sender, RoutedEventArgs e)
        {
            string name = imieBox.Text;
            string nazwisko = nazwiskoBox.Text;

            // Zmienna do przechowywania stanowiska
            string stanowisko = (stanowiskoBox.SelectedItem as ComboBoxItem)?.Content.ToString();

            // Walidacja, aby sprawdzić, czy wszystkie dane zostały wprowadzone
            if (string.IsNullOrWhiteSpace(name) || string.IsNullOrWhiteSpace(nazwisko) || string.IsNullOrWhiteSpace(stanowisko))
            {
                MessageBox.Show("Proszę uzupełnić wszystkie dane pracownika!", "Błąd");
                return;
            }

            // Jeśli hasło jest puste (np. użytkownik nie wygenerował hasła przed kliknięciem), wyświetl komunikat
            if (string.IsNullOrEmpty(password))
            {
                MessageBox.Show("Proszę wygenerować hasło przed zatwierdzeniem danych!", "Błąd");
                return;
            }

            // Wyświetlamy dane pracownika i wygenerowane hasło
            MessageBox.Show($"Dane pracownika: {name} {nazwisko} {stanowisko} Hasło: {password}", "Zatwierdzono");
        }
    }
}
