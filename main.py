from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from TikTokLive import TikTokLiveClient
import pyautogui
from TikTokLive.types.events import LikeEvent
import threading


class TikTokApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10)

        self.start_button = Button(text='Старт', size_hint=(None, None))
        self.start_button.bind(on_press=self.start_script)
        self.layout.add_widget(self.start_button)

        self.status_label = Label(text='Ожидание запуска', size_hint=(None, None))
        self.layout.add_widget(self.status_label)

        return self.layout

    def start_script(self, instance):
        self.status_label.text = 'Скрипт запущен'
        threading.Thread(target=self.run_script).start()

    def run_script(self):
        client = TikTokLiveClient(unique_id="@oolipil")

        @client.on("like")
        async def on_like(event: LikeEvent):
            pyautogui.click()

        client.run()


if __name__ == '__main__':
    TikTokApp().run()



