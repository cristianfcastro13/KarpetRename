from PySide6.QtWidgets import QMessageBox
import os
import winreg as reg

#Gets the full path to the executable
current_dir = os.path.dirname(os.path.realpath(__file__))
exe_path = os.path.join(current_dir, 'dist', 'gui_main.exe')

try:
    '''Advanced context menu entry that opens the GUI and allows for prefix/suffix customization'''
    advanced_key_path = r'Directory\\Background\\shell\\AdvancedKarpetRename' #The key in the registry where folder context menus are defined
    key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, advanced_key_path) #Creates the main key
    reg.SetValue(key, '', reg.REG_SZ, 'Advanced Karpet Rename') #Sets the default value ('') the text that appears in the context menu
    reg.SetValueEx(key, 'Icon', 0, reg.REG_SZ, f'"{exe_path}",0') #Sets the icon for the context menu voice and links to the main executable

    #Creates the 'command' subkey within the main key
    command_key = reg.CreateKey(key, 'command') #'Key that runs the main script with the target directory as an argument
    reg.SetValue(command_key, '', reg.REG_SZ, f'"{exe_path}" "%V"')#"%V" is a special Windows variable that gets replaced with the current folder path

    #Good practice to close the keys when done
    reg.CloseKey(command_key)
    reg.CloseKey(key)

    #TODO: Add error handling for permissions issues and erase these print statements for production deployment
    print(f"Successfully created ADVANCED context menu entry for {exe_path}")
    print("You can now right-click a folder background to use ADVANCED Karpet Rename!")
except Exception as e:
    print(f"Failed to create ADVANCED context menu entry: {e}")
    QMessageBox.critical(None, "Error", f"Failed to create ADVANCED context menu entry: {e} \n Try running the program as an administrator.")

try:
    '''Simple context menu entry setup that skips the GUI and uses default prefix/suffix(empty) to rename files immediately'''
    simple_key_path = r'Directory\\Background\\shell\\SimpleKarpetRename' #The key in the registry where folder context menus are defined
    key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, simple_key_path) #Creates the main key
    reg.SetValue(key, '', reg.REG_SZ, 'Simple Karpet Rename') #Sets the default value ('') the text that appears in the context menu
    reg.SetValueEx(key, 'Icon', 0, reg.REG_SZ, f'"{exe_path}",0') #Sets the icon for the context menu voice and links to the main executable

    #Creates the 'command' subkey within the main key
    command_key = reg.CreateKey(key, 'command') #'Key that runs the main script with the target directory as an argument
    reg.SetValue(command_key, '', reg.REG_SZ, f'"{exe_path}" "%V" "fast"')#"%V" is a special Windows variable that gets replaced with the current folder path

    #Good practice to close the keys when done
    reg.CloseKey(command_key)
    reg.CloseKey(key)

    #TODO: Add error handling for permissions issues and erase these print statements for production deployment
    print(f"Successfully created SIMPLE context menu entry for {exe_path}")
    print("You can now right-click a folder background to use SIMPLE Karpet Rename!")
except Exception as e:
    print(f"Failed to create SIMPLE context menu entry: {e}")
    QMessageBox.critical(None, "Error", f"Failed to create SIMPLE context menu entry: {e} \n Try running the program as an administrator.")
