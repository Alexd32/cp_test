from pywinauto import Application
import time

# Запускаем приложение с backend="uia"
app = Application(backend="uia").start("notepad.exe")

time.sleep(1)  # Ждем, чтобы приложение успело запуститься

# Получаем окно
dlg = app.window(title_re=".*Блокнот.*")

# Вводим текст
dlg.child_window(class_name="Edit").type_keys("Привет, мир!", with_spaces=True)

# Закрываем блокнот
try:
    dlg.menu_select("Файл->Выход")
    print("Блокнот закрыт.")
except Exception as e:
    print("Не удалось закрыть блокнот.")
