from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.widget import Widget

class KebugaranApp(App):
    def build(self):
        self.title = "Cek Kebugaran Harian"
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # Header
        header = Label(
            text='CEK KEBUGARAN HARIAN',
            font_size=dp(24),
            size_hint_y=None,
            height=dp(60),
            color=(0.2, 0.6, 0.8, 1)
        )
        main_layout.add_widget(header)
        
        # Scroll view for inputs
        scroll = ScrollView()
        input_layout = GridLayout(cols=1, spacing=dp(10), size_hint_y=None)
        input_layout.bind(minimum_height=input_layout.setter('height'))
        
        # Input fields
        self.inputs = {}
        
        fields = [
            ('usia', 'Usia (tahun)', 'number'),
            ('berat', 'Berat badan (kg)', 'number'),
            ('tinggi', 'Tinggi badan (cm)', 'number'),
            ('detak_jantung', 'Detak jantung istirahat (BPM)', 'number'),
            ('langkah', 'Jumlah langkah hari ini', 'number'),
            ('nyeri', 'Skor nyeri otot (1-10)', 'number')
        ]
        
        for field_id, label_text, input_type in fields:
            # Container for each input
            field_container = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(80))
            
            # Label
            label = Label(
                text=label_text,
                size_hint_y=None,
                height=dp(30),
                text_size=(None, None),
                halign='left',
                color=(0.3, 0.3, 0.3, 1)
            )
            
            # Input
            text_input = TextInput(
                multiline=False,
                input_type=input_type,
                size_hint_y=None,
                height=dp(40),
                background_color=(0.95, 0.95, 0.95, 1),
                foreground_color=(0.2, 0.2, 0.2, 1),
                cursor_color=(0.2, 0.6, 0.8, 1)
            )
            
            self.inputs[field_id] = text_input
            
            field_container.add_widget(label)
            field_container.add_widget(text_input)
            input_layout.add_widget(field_container)
        
        scroll.add_widget(input_layout)
        main_layout.add_widget(scroll)
        
        # Button
        btn_layout = BoxLayout(size_hint_y=None, height=dp(60), padding=(0, dp(10)))
        
        check_btn = Button(
            text='CEK KEBUGARAN',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.2, 0.6, 0.8, 1),
            color=(1, 1, 1, 1)
        )
        check_btn.bind(on_press=self.cek_kebugaran)
        
        btn_layout.add_widget(check_btn)
        main_layout.add_widget(btn_layout)
        
        return main_layout
    
    def cek_kebugaran(self, instance):
        try:
            # Get input values
            usia = int(self.inputs['usia'].text or 0)
            berat = int(self.inputs['berat'].text or 0)
            tinggi = int(self.inputs['tinggi'].text or 0)
            detak_jantung = int(self.inputs['detak_jantung'].text or 0)
            langkah = int(self.inputs['langkah'].text or 0)
            nyeri = int(self.inputs['nyeri'].text or 0)
            
            # Validation
            if not all([usia, berat, tinggi, detak_jantung]):
                self.show_popup('Error', 'Mohon isi semua field yang diperlukan!')
                return
            
            if tinggi <= 0:
                self.show_popup('Error', 'Tinggi badan harus lebih dari 0!')
                return
                
            if nyeri < 1 or nyeri > 10:
                self.show_popup('Error', 'Skor nyeri harus antara 1-10!')
                return
            
            # Kalkulasi BMI
            bmi = berat / ((tinggi/100) ** 2)
            
            # Hasil analisis
            hasil = "=== HASIL ANALISIS ===\n\n"
            
            # 1. BMI
            if bmi < 18.5:
                kategori_bmi = "Kurus"
            elif 18.5 <= bmi < 25:
                kategori_bmi = "Normal"
            elif 25 <= bmi < 30:
                kategori_bmi = "Gemuk"
            else:
                kategori_bmi = "Obesitas"
            hasil += f"📊 BMI Anda: {bmi:.1f} ({kategori_bmi})\n\n"
            
            # 2. Kebugaran jantung
            if detak_jantung < 60:
                status_jantung = "Sangat baik (atletik)"
            elif 60 <= detak_jantung < 80:
                status_jantung = "Baik"
            else:
                status_jantung = "Perlu perhatian"
            hasil += f"❤️ Detak jantung istirahat: {detak_jantung} BPM ({status_jantung})\n\n"
            
            # 3. Saran langkah
            target_langkah = 8000
            if langkah < target_langkah:
                hasil += f"🚶 Langkah hari ini: {langkah}\n   Kurang {target_langkah - langkah} dari target 8.000\n\n"
            else:
                hasil += f"🚶 Langkah hari ini: {langkah}\n   Target tercapai! 🎉\n\n"
            
            # 4. Rekomendasi nyeri
            if nyeri <= 3:
                hasil += "💪 Nyeri otot rendah\n   Lanjutkan aktivitas normal!"
            elif 4 <= nyeri <= 6:
                hasil += "⚠️ Nyeri otot sedang\n   Lakukan peregangan 5 menit"
            else:
                hasil += "🛑 Nyeri otot tinggi\n   Istirahatkan otot + kompres hangat!"
            
            self.show_popup('Hasil Kebugaran', hasil)
            
        except ValueError:
            self.show_popup('Error', 'Mohon masukkan angka yang valid!')
        except Exception as e:
            self.show_popup('Error', f'Terjadi kesalahan: {str(e)}')
    
    def show_popup(self, title, content):
        # Create popup content
        popup_layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # Content label
        content_label = Label(
            text=content,
            text_size=(dp(300), None),
            halign='left',
            valign='top',
            color=(0.2, 0.2, 0.2, 1)
        )
        popup_layout.add_widget(content_label)
        
        # Close button
        close_btn = Button(
            text='Tutup',
            size_hint_y=None,
            height=dp(40),
            background_color=(0.2, 0.6, 0.8, 1)
        )
        
        popup = Popup(
            title=title,
            content=popup_layout,
            size_hint=(0.9, 0.7),
            auto_dismiss=True
        )
        
        close_btn.bind(on_press=popup.dismiss)
        popup_layout.add_widget(close_btn)
        
        popup.open()

if __name__ == '__main__':
    KebugaranApp().run()