using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace inf4_st24_prak1
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

        private void zmienObrazy(object sender, RoutedEventArgs e)
        {
            string numer = numerBox.Text;

            if (numer == "111")
            {
                obrazOdcisk.Source = new BitmapImage(new Uri("images/111-odcisk.jpg", UriKind.Relative));
                obrazOsoba.Source = new BitmapImage(new Uri("images/111-zdjecie.jpg", UriKind.Relative));
            }
            else if (numer == "333")
            {
                obrazOdcisk.Source = new BitmapImage(new Uri("images/333-odcisk.jpg", UriKind.Relative));
                obrazOsoba.Source = new BitmapImage(new Uri("images/333-zdjecie.jpg", UriKind.Relative));
            }
            else if (numer == "000")
            {
                obrazOdcisk.Source = new BitmapImage(new Uri("images/000-odcisk.jpg", UriKind.Relative));
                obrazOsoba.Source = new BitmapImage(new Uri("images/000-zdjecie.jpg", UriKind.Relative));
            }
        }

        private void OK_Btn(object sender, RoutedEventArgs e)
        {
            string imie = imieBox.Text;
            string nazwisko = nazwiskoBox.Text;
            string oczy = "";

            if (niebieskieRadio.IsChecked == true)
            {
                oczy = "niebieski";
            }
            else if (zieloneRadio.IsChecked == true)
            {
                oczy = "zielone";
            }
            else if (piwneRadio.IsChecked == true)
            {
                oczy = "piwne";
            }
            else
            {
                MessageBox.Show("Wybierz kolor oczu", "Błąd");
                return;
            }

            if (string.IsNullOrWhiteSpace(imie) || string.IsNullOrWhiteSpace(nazwisko))
            {
                MessageBox.Show("Wprowadź dane", "Błąd");
                return;
            }
            else
            {
                MessageBox.Show($"{imie} {nazwisko} kolor oczu {oczy}");
            }
        }
    }
}