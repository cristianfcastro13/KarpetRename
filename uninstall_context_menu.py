from PySide6.QtWidgets import QMessageBox
import os
import winreg as reg

try:
    '''Removes the Advanced context menu entry'''
    advanced_key_path = r'Directory\\Background\\shell\\KarpetRenameAdvanced' #The key in the registry where folder context menus are defined
    reg.DeleteKey(reg.HKEY_CLASSES_ROOT, advanced_key_path + r'\command') #Deletes the 'command' subkey first
    reg.DeleteKey(reg.HKEY_CLASSES_ROOT, advanced_key_path) #Deletes the main key
    print("Successfully removed Advanced context menu entry")
except Exception as e:
    print(f"Failed to remove Advanced context menu entry: {e}")
    QMessageBox.critical(None, "Error", f"Failed to remove ADVANCED context menu entry: {e} \n Try running the program as an administrator.")


try:
    '''Removes the Simple context menu entry'''
    simple_key_path = r'Directory\\Background\\shell\\KarpetRenameFast' #The key in the registry where folder context menus are defined
    reg.DeleteKey(reg.HKEY_CLASSES_ROOT, simple_key_path + r'\command') #Deletes the 'command' subkey first
    reg.DeleteKey(reg.HKEY_CLASSES_ROOT, simple_key_path) #Deletes the main key
    print("Successfully removed Fast context menu entry")
except Exception as e:
    print(f"Failed to remove Fast context menu entry: {e}")
    QMessageBox.critical(None, "Error", f"Failed to remove FAST context menu entry: {e} \n Try running the program as an administrator.")