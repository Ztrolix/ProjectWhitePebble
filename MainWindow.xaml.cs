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
using System.Threading;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.ComponentModel;

namespace Loader
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

        private void ProgressBar_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {

            for (int i = 0; i < 100; i++)
            {
                pbStatus.Value++;
                if (pbStatus.Value >= 99)
                {
                    System.Diagnostics.Process.Start(@"Installer.py");
                }
            }
        }
    }
}