# **Automated Keyboard and Mouse Control**

This project allows you to automate keyboard and mouse actions based on custom configurations. You can automate pressing specific keys or clicking mouse buttons repeatedly with adjustable speeds. The tool features a simple, user-friendly GUI built with Python's Tkinter library, and allows you to save and load your settings from a JSON configuration file.

---

## **Features**

- **Customizable Automation**: Choose the key or mouse button to automate (e.g., keyboard keys, left/right mouse button, or specific mouse positions).
- **Adjustable Speed**: Set the speed of the automation for more precise control.
- **Save and Load Settings**: Store configurations in a JSON file for later use.
- **Real-Time Click Counter**: View the number of automated actions (clicks/keypresses) in real-time.
- **Keyboard Shortcuts**: Use F1 to start and stop the automation at any time.
- **Cross-Platform**: Works on any platform supported by Python and the required libraries.

---

## **Installation**

### Requirements

To run this project, you will need the following:

- Python 3.x (preferably 3.7 or higher)
- `pyautogui` library
- `keyboard` library
- `tkinter` (usually comes pre-installed with Python)
- `json` (standard Python library)

### Steps to Install

1. Clone the repository:

    ```bash
    git clone https://github.com/LCodeBase/Auto-click.git
    ```

2. Navigate to the project directory:

    ```bash
    cd automated-keyboard-mouse
    ```

3. Install the required Python packages:

    ```bash
    pip install pyautogui keyboard
    ```

4. Run the script:

    ```bash
    python automation_gui.py
    ```

---

## **Usage**

Once the program is running, you can:

1. **Configure Automation**:
   - Enter the key or mouse button you want to automate in the input field.
   - For mouse automation, use `"mouse1"` for the left mouse button, `"mouse2"` for the right mouse button, or `"posicao"` to capture the current mouse position.
   - Set the desired automation speed (optional).
   - Click "Save Configurations" to apply your settings.

2. **Start Automation**:
   - Press `F1` to start the automation. The automation will start clicking or pressing the specified key/button continuously.
   - The number of clicks/keypresses will be shown in real-time.

3. **Stop Automation**:
   - Press `F1` again to stop the automation.

4. **Save and Load Settings**:
   - You can save your configurations to a JSON file for future use by clicking "Save Configurations to File."
   - To load a previously saved configuration, click "Load Configurations from File."

---

## **Keyboard Shortcuts**

- **F1**: Toggle between starting and stopping the automation.

---

## **Configuration File**

The settings for the automation are stored in a `configuracoes.json` file. This file contains the following settings:

```json
{
    "tecla_ou_botao": "mouse1",     // Key or mouse button to automate
    "velocidade": 10,                // Speed of automation (seconds between actions)
    "posicao_click": [x, y]          // Position of the mouse if "posicao" is used
}

```
## Contributing
If you'd like to contribute to this project, feel free to fork it, submit issues, or create pull requests with bug fixes or new features.

## Acknowledgements
- PyAutoGUI: Library used to automate keyboard and mouse actions.
- Keyboard: Library used to listen for key events.

