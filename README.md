Step 1: Open a Terminal or Command Prompt
Open your terminal or command prompt. You can find it on your computer as follows:

On Windows, you can use Command Prompt or PowerShell.
On macOS and Linux, you can use the Terminal.

Step 2: Navigate to Your Project Directory
Use the cd command to navigate to the directory where your project is located. For example:

code : cd path/to/your/project

Step 3: Install virtualenv (if not already installed)
If you don't have virtualenv installed, you can install it using the following command:

code : pip install virtualenv

Step 4: Create a Virtual Environment
Create a virtual environment in your project directory. Replace venv with the desired name for your virtual environment:

code : python -m venv venv
On older versions of Python, you might use:

code : virtualenv venv

Step 5: Activate the Virtual Environment
Activate the virtual environment:

On Windows (Command Prompt) : .\venv\Scripts\activate (or)
On Windows (PowerShell) : .\venv\Scripts\Activate.ps1 (or)
On macOS and Linux : source venv/bin/activate

Step 6: Verify Activation
You should see the virtual environment name in your command prompt or terminal. For example:
code : (venv) $

Step 7: Install Dependencies
Now that the virtual environment is active, you can install project dependencies using pip. For example:

code : pip install flask

Step 8: Run Your Application
Run your Flask application or any other project within the activated virtual environment.

Step 9: Deactivate the Virtual Environment (Optional)
When you're done working on your project, you can deactivate the virtual environment using:

code : deactivate
This will return you to the global Python environment.
