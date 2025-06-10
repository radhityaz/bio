from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.core.window import Window

class KebugaranApp(App):
    def build(self):
        # Set window size for desktop testing
        Window.size = (400, 700)
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        
        # Title
        title = Label(
            text='CEK KEBUGARAN HARIAN',
            font_size=dp(24),
            size_hint_y=None,
            height=dp(50),
            bold=True
        )
        main_layout.add_widget(title)
        
        # Scroll view for inputs
        scroll = ScrollView()
        input_layout = BoxLayout(orientation='vertical', spacing=dp(15), size_hint_y=None)
        input_layout.bind(minimum_height=input_layout.setter('height'))
        
        # Input fields
        self.inputs = {}
        
        # Usia
        usia_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(80))
        usia_layout.add_widget(Label(text='Usia (tahun):', size_hint_y=None, height=dp(30), halign='left'))
        self.inputs['usia'] = TextInput(
            multiline=False,
            input_filter='int',
            size_hint_y=None,
            height=dp(40)
        )
        usia_layout.add_widget(self.inputs['usia'])
        input_layout.add_widget(usia_layout)
        
        # Berat badan
        berat_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(80))
        berat_layout.add_widget(Label(text='Berat badan (kg):', size_hint_y=None, height=dp(30), halign='left'))
        self.inputs['berat'] = TextInput(
            multiline=False,
            input_filter='int',
            size_hint_y=None,
            height=dp(40)
        )
        berat_layout.add_widget(self.inputs['berat'])
        input_layout.add_widget(berat_layout)
        
        # Tinggi badan
        tinggi_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(80))
        tinggi_layout.add_widget(Label(text='Tinggi badan (cm):', size_hint_y=None, height=dp(30), halign='left'))
        self.inputs['tinggi'] = TextInput(
            multiline=False,
            input_filter='int',
            size_hint_y=None,
            height=dp(40)
        )
        tinggi_layout.add_widget(self.inputs['tinggi'])
        input_layout.add_widget(tinggi_layout)
        
        # Detak jantung
        detak_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(80))
        detak_layout.add_widget(Label(text='Detak jantung istirahat (BPM):', size_hint_y=None, height=dp(30), halign='left'))
        self.inputs['detak_jantung'] = TextInput(
            multiline=False,
            input_filter='int',
            size_hint_y=None,
            height=dp(40)
        )
        detak_layout.add_widget(self.inputs['detak_jantung'])
        input_layout.add_widget(detak_layout)
        
        # Langkah
        langkah_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(80))
        langkah_layout.add_widget(Label(text='Jumlah langkah hari ini:', size_hint_y=None, height=dp(30), halign='left'))
        self.inputs['langkah'] = TextInput(
            multiline=False,
            input_filter='int',
            size_hint_y=None,
            height=dp(40)
        )
        langkah_layout.add_widget(self.inputs['langkah'])
        input_layout.add_widget(langkah_layout)
        
        # Nyeri otot
        nyeri_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(80))
        nyeri_layout.add_widget(Label(text='Skor nyeri otot (1-10):', size_hint_y=None, height=dp(30), halign='left'))
        self.inputs['nyeri'] = TextInput(
            multiline=False,
            input_filter='int',
            size_hint_y=None,
            height=dp(40)
        )
        nyeri_layout.add_widget(self.inputs['nyeri'])
        input_layout.add_widget(nyeri_layout)
        
        scroll.add_widget(input_layout)
        main_layout.add_widget(scroll)
        
        # Button
        check_button = Button(
            text='CEK KEBUGARAN',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.2, 0.6, 0.8, 1)
        )
        check_button.bind(on_press=self.cek_kebugaran)
        main_layout.add_widget(check_button)
        
        return main_layout
    
    def cek_kebugaran(self, instance):
        try:
            # Validasi input
            for key, input_field in self.inputs.items():
                if not input_field.text.strip():
                    self.show_popup('Error', f'Mohon isi {key}!')
                    return
            
            # Ambil data input
            usia = int(self.inputs['usia'].text)
            berat = int(self.inputs['berat'].text)
            tinggi = int(self.inputs['tinggi'].text)
            detak_jantung = int(self.inputs['detak_jantung'].text)
            langkah = int(self.inputs['langkah'].text)
            nyeri = int(self.inputs['nyeri'].text)
            
            # Validasi range
            if not (1 <= nyeri <= 10):
                self.show_popup('Error', 'Skor nyeri harus antara 1-10!')
                return
            
            if tinggi <= 0 or berat <= 0:
                self.show_popup('Error', 'Tinggi dan berat harus lebih dari 0!')
                return
            
            # Kalkulasi BMI
            bmi = berat / ((tinggi/100) ** 2)
            
            # Analisis BMI
            if bmi < 18.5:
                kategori_bmi = "Kurus"
            elif 18.5 <= bmi < 25:
                kategori_bmi = "Normal"
            elif 25 <= bmi < 30:
                kategori_bmi = "Gemuk"
            else:
                kategori_bmi = "Obesitas"
            
            # Analisis detak jantung
            if detak_jantung < 60:
                status_jantung = "Sangat baik (atletik)"
            elif 60 <= detak_jantung < 80:
                status_jantung = "Baik"
            else:
                status_jantung = "Perlu perhatian"
            
            # Analisis langkah
            target_langkah = 8000
            if langkah < target_langkah:
                status_langkah = f"Kurang {target_langkah - langkah} dari target 8.000"
            else:
                status_langkah = "Target tercapai!"
            
            # Analisis nyeri
            if nyeri <= 3:
                status_nyeri = "Nyeri rendah - Lanjutkan aktivitas normal!"
            elif 4 <= nyeri <= 6:
                status_nyeri = "Nyeri sedang - Lakukan peregangan 5 menit"
            else:
                status_nyeri = "Nyeri tinggi - Istirahatkan otot + kompres hangat!"
            
            # Buat hasil
            hasil = f"""HASIL ANALISIS KEBUGARAN

📊 BMI: {bmi:.1f} ({kategori_bmi})

❤️ Detak Jantung: {detak_jantung} BPM
   Status: {status_jantung}

🚶 Langkah: {langkah}
   {status_langkah}

💪 Nyeri Otot: {nyeri}/10
   {status_nyeri}"""
            
            self.show_popup('Hasil Kebugaran', hasil)
            
        except ValueError:
            self.show_popup('Error', 'Mohon masukkan angka yang valid!')
        except Exception as e:
            self.show_popup('Error', f'Terjadi kesalahan: {str(e)}')
    
    def show_popup(self, title, content):
        popup_layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # Content label
        content_label = Label(
            text=content,
            text_size=(dp(300), None),
            halign='left',
            valign='top'
        )
        popup_layout.add_widget(content_label)
        
        # Close button
        close_button = Button(
            text='Tutup',
            size_hint_y=None,
            height=dp(40)
        )
        popup_layout.add_widget(close_button)
        
        # Create popup
        popup = Popup(
            title=title,
            content=popup_layout,
            size_hint=(0.9, 0.7)
        )
        
        close_button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    KebugaranApp().run()