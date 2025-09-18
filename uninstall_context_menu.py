import os
import winreg as reg

try:
    '''Removes the Advanced context menu entry'''
    advanced_key_path = r'Directory\\Background\\shell\\KarpetRenameAdvanced' #The key in the registry where folder context menus are defined
    reg.DeleteKey(reg.HKEY_CLASSES_ROOT, advanced_key_path + r'\command') #Deletes the 'command' subkey first
    reg.DeleteKey(reg.HKEY_CLASSES_ROOT, advanced_key_path) #Deletes the main key
    print("Successfully removed Advanced context menu entry")
except Exception as e:
    print(f"Failed to remove Advanced context menu entry: {e} \n Try running the uninstall program as an administrator. You can find it in the folder where you installed the program.")


try:
    '''Removes the FAST context menu entry'''
    simple_key_path = r'Directory\\Background\\shell\\KarpetRenameFast' #The key in the registry where folder context menus are defined
    reg.DeleteKey(reg.HKEY_CLASSES_ROOT, simple_key_path + r'\command') #Deletes the 'command' subkey first
    reg.DeleteKey(reg.HKEY_CLASSES_ROOT, simple_key_path) #Deletes the main key
    print("Successfully removed Fast context menu entry")
except Exception as e:
    print(f"Failed to remove Fast context menu entry: {e} \m Try running the uninstall program as an administrator. You can find it in the folder where you installed the program.")
