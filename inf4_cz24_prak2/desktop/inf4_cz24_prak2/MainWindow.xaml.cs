using System.IO;
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

namespace inf4_cz24_prak2
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private List<Album> albums;
        private int index = 0;
        public MainWindow()
        {
            InitializeComponent();
            odczytajDane();
            zaczytajDane();
        }

        private void odczytajDane()
        {
            albums = new List<Album>();
            string[] lines = File.ReadAllLines("dane1.txt");

            for (int i = 0; i < lines.Length; i += 5)
            {
                var album = new Album
                {
                    Artysta = lines[i].Trim(),
                    Tytul = lines[i + 1].Trim('"').Trim(),
                    Utwory = int.Parse(lines[i + 2].Trim()),
                    Rok = int.Parse(lines[i + 3].Trim()),
                    IloscPobran = int.Parse(lines[i + 4].Trim())
                };
                albums.Add(album);
            }
        }

        private void zaczytajDane()
        {
            var album = albums[index];
            TxtArtysta.Text = album.Artysta;
            TxtTytul.Text = album.Tytul;
            TxtUtwory.Text = $"{album.Utwory} utworów";
            TxtRok.Text = $"{album.Rok}";
            TxtPobrania.Text = $"{album.IloscPobran}";
        }

        public void Btn_Lewo(object sender, RoutedEventArgs e)
        {
            index = (index - 1 + albums.Count) % albums.Count;
            zaczytajDane();
        }

        public void Btn_Prawo(object sender, RoutedEventArgs e)
        {
            index = (index + 1 + albums.Count) % albums.Count;
            zaczytajDane();
        }

        public void Btn_Pobierz(object sender, RoutedEventArgs e)
        {
            albums[index].IloscPobran++;
            zaczytajDane();
        }
    }
}