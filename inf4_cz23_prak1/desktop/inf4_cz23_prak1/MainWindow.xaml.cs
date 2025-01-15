using System.Text;
using System.Text.RegularExpressions;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace inf4_cz23_prak1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void SprawdzCeneButton_Click(object sender, RoutedEventArgs e)
        {
            string cena = "";
            string obraz = "";

            if (PocztowkaRadio.IsChecked == true)
            {
                cena = "1 zł";
                obraz = "pocztowka.png";
            }
            else if (ListRadio.IsChecked == true)
            {
                cena = "1.5 zł";
                obraz = "list.png";
            }
            else if (PaczkaRadio.IsChecked == true)
            {
                cena = "10 zł";
                obraz = "paczka.png";
            }

            Cena.Text = $"Cena: {cena}";
            PrzesylkaImage.Source = new BitmapImage(new Uri($"images/{obraz}", UriKind.Relative));
        }

        private void ZatwierdzButton_Click(object sender, RoutedEventArgs e)
        {
            string kod_pocztowy = pocztowyKod.Text;
            if (!kod_pocztowy.All(char.IsDigit))
            {
                MessageBox.Show("Kod musi sie składać z samych cyfr", "Błąd");
            }
            else if (kod_pocztowy.Length != 5)
            {
                MessageBox.Show("Nieprwaidłowa liczba cyfr w kodzie pocztowym", "Błąd");
            }
            else
            {
                MessageBox.Show("Dane przesyłki zostały wprowadzone", "Sukces", MessageBoxButton.OK, MessageBoxImage.Information);
            }
        }
    }
}