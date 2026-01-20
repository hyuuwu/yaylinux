#!/usr/bin/env python3
"""
Kivy YAYLinux app (Buildozer-ready).

Features:
- Terminal-style UI
- First-run setup popup
- File picker for audio (Kivy's FileChooser)
- Play audio via Android intent (ACTION_VIEW) if available
- Run shell commands on device (optionally as root via "Run as root" toggle)
- Secure password storage via Java EncryptedSharedPreferences helper (pyjnius) if available
- Fallback to littu.py if present, else plaintext storage (not recommended)
"""

import os
import subprocess
import threading
from pathlib import Path

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.togglebutton import ToggleButton

# Try to import littu for backward compatibility (optional)
try:
    import littu as lil
except Exception:
    lil = None

# Try to import pyjnius and the SharedPrefs helper
try:
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    SharedPrefsHelper = autoclass('org.example.secure.SharedPrefsHelper')
    has_shared_helper = True
except Exception:
    PythonActivity = None
    SharedPrefsHelper = None
    has_shared_helper = False

KV = """
<RootWidget>:
    orientation: "vertical"
    padding: 6
    spacing: 6

    ScrollView:
        size_hint_y: 0.78
        do_scroll_x: False

        TextInput:
            id: console
            text: root.console_text
            readonly: True
            font_size: '13sp'
            foreground_color: 0,1,0,1
            background_color: 0,0,0,1
            size_hint_y: None
            height: max(self.minimum_height, root.height*0.78)
            multiline: True

    BoxLayout:
        size_hint_y: 0.22
        orientation: "vertical"
        spacing: 6

        BoxLayout:
            size_hint_y: 0.55
            orientation: "horizontal"
            spacing: 6

            TextInput:
                id: command_input
                hint_text: "Enter command"
                multiline: False
                on_text_validate: root.on_send()

            Button:
                text: "Send"
                size_hint_x: 0.18
                on_release: root.on_send()

        BoxLayout:
            size_hint_y: 0.45
            orientation: "horizontal"
            spacing: 6

            ToggleButton:
                id: root_toggle
                text: "Run as root"
                size_hint_x: 0.33
                state: "normal"

            Button:
                text: "Pick Audio"
                size_hint_x: 0.33
                on_release: root.open_filechooser()

            Button:
                text: "Clear"
                size_hint_x: 0.34
                on_release: root.clear_console()
"""

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.console_text = ""
        self.app = App.get_running_app()
        self.ensure_config()
        Clock.schedule_once(lambda dt: self.post_startup(), 0.2)

    def ensure_config(self):
        cfg = Path(self.app.user_data_dir)
        cfg.mkdir(parents=True, exist_ok=True)
        self.config_dir = cfg
        self.user_file = cfg / "user"
        self.hostname_file = cfg / "hostname"
        self.password_key = "yay_password"
        self.sentinel = cfg / "dontdeletethis.file"

    def post_startup(self):
        if self.is_first_run():
            self.show_first_run_popup()
        self.append_console("Welcome to YAYLinux (Kivy)\n")
        self.append_console(self.get_prompt())

    def is_first_run(self):
        return not self.sentinel.exists()

    def show_first_run_popup(self):
        layout = BoxLayout(orientation="vertical", spacing=6, padding=6)
        username_in = TextInput(hint_text="Username", multiline=False)
        hostname_in = TextInput(hint_text="Hostname", multiline=False)
        password_in = TextInput(hint_text="Password", password=True, multiline=False)
        info = Label(text="First run setup: enter username, hostname and password", size_hint_y=None, height=40)

        btn_layout = BoxLayout(size_hint_y=None, height=40, spacing=6)
        ok_btn = Button(text="OK")
        cancel_btn = Button(text="Cancel")
        btn_layout.add_widget(ok_btn)
        btn_layout.add_widget(cancel_btn)

        layout.add_widget(info)
        layout.add_widget(username_in)
        layout.add_widget(hostname_in)
        layout.add_widget(password_in)
        layout.add_widget(btn_layout)

        popup = Popup(title="Initial setup", content=layout, size_hint=(0.9, 0.6), auto_dismiss=False)

        def on_ok(_):
            username = username_in.text.strip() or "User"
            hostname = hostname_in.text.strip() or "localhost"
            password = password_in.text or ""
            try:
                self.user_file.write_text(username)
                self.hostname_file.write_text(hostname)
                # Use Java EncryptedSharedPreferences if available
                if has_shared_helper and PythonActivity:
                    try:
                        SharedPrefsHelper.savePassword(PythonActivity.mActivity, self.password_key, password)
                    except Exception:
                        # fallback to littu or plaintext
                        if lil:
                            try:
                                lil.crypt(password, str(Path(self.app.user_data_dir) / "password"))
                            except Exception:
                                (Path(self.app.user_data_dir) / "password").write_text(password)
                        else:
                            (Path(self.app.user_data_dir) / "password").write_text(password)
                else:
                    # fallback
                    if lil:
                        try:
                            lil.crypt(password, str(Path(self.app.user_data_dir) / "password"))
                        except Exception:
                            (Path(self.app.user_data_dir) / "password").write_text(password)
                    else:
                        (Path(self.app.user_data_dir) / "password").write_text(password)

                self.sentinel.write_text("initialized")
                popup.dismiss()
                self.append_console("Setup complete.\n")
                self.append_console(self.get_prompt())
            except Exception as e:
                popup.content.add_widget(Label(text=f"Error saving config: {e}"))

        def on_cancel(_):
            self.sentinel.write_text("skipped")
            popup.dismiss()
            self.append_console("First-run setup skipped. Using defaults.\n")
            self.append_console(self.get_prompt())

        ok_btn.bind(on_release=on_ok)
        cancel_btn.bind(on_release=on_cancel)
        popup.open()

    def get_prompt(self):
        try:
            user = self.user_file.read_text().strip() if self.user_file.exists() else "User"
        except Exception:
            user = "User"
        try:
            host = self.hostname_file.read_text().strip() if self.hostname_file.exists() else "localhost"
        except Exception:
            host = "localhost"
        return f"{user}@{host} $ ~/ "

    def append_console(self, text):
        def _append(dt):
            self.console_text += str(text)
            if hasattr(self.ids, "console"):
                self.ids.console.text = self.console_text
        Clock.schedule_once(_append, 0)

    def on_send(self):
        cmd = self.ids.command_input.text.strip()
        if not cmd:
            return
        self.append_console(cmd + "\n")
        self.ids.command_input.text = ""
        threading.Thread(target=self._run_command_thread, args=(cmd,), daemon=True).start()

    def _run_command_thread(self, cmd):
        run_as_root = self.ids.root_toggle.state == "down"
        # builtins
        if cmd == "ls":
            out = self._builtin_ls()
            self.append_console(out + "\n" + self.get_prompt())
            return
        if cmd.startswith("cd "):
            arg = cmd.split(" ", 1)[1].strip()
            out = self._builtin_cd(arg)
            self.append_console(out + "\n" + self.get_prompt())
            return
        if cmd == "help":
            out = (
                "LIST OF COMMANDS:\nhelp, ls, cd <dir>, exit, source, whoamiyay, calc, audioplayer\n"
                "Other commands forwarded to device shell. Toggle 'Run as root' to use su -c.\n"
            )
            self.append_console(out + self.get_prompt())
            return
        if cmd == "whoamiyay":
            try:
                out = self.user_file.read_text().strip() if self.user_file.exists() else "User"
            except Exception:
                out = "User"
            self.append_console(out + "\n" + self.get_prompt())
            return
        if cmd == "source":
            self.append_console("Open https://github.com/hyuuwu/yaylinux in the device browser.\n")
            # Launch browser intent
            try:
                if PythonActivity:
                    Intent = autoclass('android.content.Intent')
                    Uri = autoclass('android.net.Uri')
                    intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://github.com/hyuuwu/yaylinux"))
                    PythonActivity.mActivity.startActivity(intent)
            except Exception:
                pass
            self.append_console(self.get_prompt())
            return
        if cmd == "exit":
            self.append_console("Exiting app...\n")
            Clock.schedule_once(lambda dt: App.get_running_app().stop(), 0)
            return

        # fallback: run shell command
        out = run_shell_command(cmd, as_root=run_as_root)
        self.append_console(out + "\n" + self.get_prompt())

    def _builtin_ls(self):
        try:
            cwd = os.getcwd()
            items = os.listdir(cwd)
            return cwd + "\n" + "\n".join(items)
        except Exception as e:
            return f"Error listing directory: {e}"

    def _builtin_cd(self, directory):
        try:
            os.chdir(directory)
            return f"Directory changed to: {os.getcwd()}"
        except Exception as e:
            return f"Error changing directory: {e}"

    def clear_console(self):
        self.console_text = ""
        if hasattr(self.ids, "console"):
            self.ids.console.text = ""

    def open_filechooser(self):
        chooser = FileChooserListView(path=str(Path.home()), filters=['*.mp3', '*.wav', '*.ogg'], size_hint=(1, 1))
        btn_layout = BoxLayout(size_hint_y=None, height=40, spacing=6)
        select_btn = Button(text="Play")
        cancel_btn = Button(text="Cancel")
        btn_layout.add_widget(select_btn)
        btn_layout.add_widget(cancel_btn)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(chooser)
        layout.add_widget(btn_layout)
        popup = Popup(title="Pick audio file", content=layout, size_hint=(0.95, 0.95))

        def on_select(_):
            selection = chooser.selection
            if selection:
                path = selection[0]
                self.play_audio(path)
            popup.dismiss()

        def on_cancel(_):
            popup.dismiss()

        select_btn.bind(on_release=on_select)
        cancel_btn.bind(on_release=on_cancel)
        popup.open()

    def play_audio(self, filepath):
        # Try to open audio via Android intent (ACTION_VIEW)
        try:
            if PythonActivity:
                Intent = autoclass('android.content.Intent')
                Uri = autoclass('android.net.Uri')
                File = autoclass('java.io.File')
                file_obj = File(filepath)
                uri = Uri.fromFile(file_obj)
                intent = Intent(Intent.ACTION_VIEW)
                intent.setDataAndType(uri, "audio/*")
                intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                PythonActivity.mActivity.startActivity(intent)
                return
        except Exception:
            pass
        # fallback: use 'am' command
        try:
            subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", "file://" + filepath], check=False)
        except Exception as e:
            self.append_console(f"Could not launch audio: {e}\n")

def has_su():
    for p in ("/system/xbin/su", "/system/bin/su", "/sbin/su", "/vendor/bin/su"):
        if Path(p).exists():
            return True
    return False

def run_shell_command(cmd, as_root=False, timeout=60):
    if not cmd:
        return "(no command)"
    try:
        if as_root and has_su():
            final = ["su", "-c", cmd]
        else:
            final = ["sh", "-c", cmd]
        proc = subprocess.Popen(final, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        output = []
        for line in proc.stdout:
            output.append(line.rstrip("\n"))
        proc.wait(timeout=timeout)
        return "\n".join(output) or "(no output)"
    except Exception as e:
        return f"Error running command: {e}"

class YAYApp(App):
    def build(self):
        Builder.load_string(KV)
        return RootWidget()

if __name__ == "__main__":
    YAYApp().run()
