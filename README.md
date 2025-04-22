<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Communities.win Down Vote Bot</title>
</head>
<body>
    <h1>Communities.win Down Vote Bot</h1>
    <p>This is a Python script using Selenium to automatically downvote posts on communities.win subreddits that have downvoting enabled.</p>
    <h2>Prerequisites</h2>
    <ul>
        <li>Python 3.6 or higher</li>
        <li>pip (Python package installer)</li>
    </ul>
    <h2>Installation</h2>
    <ol>
        <li>Clone the repository (if you have it):
            <pre><code>git clone https://github.com/Riotcoke123/communitieswin_downvotebot.git</code></pre>
        </li>
        <li>Navigate to the project directory:
            <pre><code>cd communitieswin_downvotebot</code></pre>
        </li>
        <li>Install the required Python libraries:
            <pre><code>pip install selenium webdriver-manager</code></pre>
        </li>
    </ol>
    <h2>Setup</h2>
    <p>Before running the script, you need to configure your bot account credentials:</p>
    <ol>
        <li>Go to <a href="https://communities.win/" target="_blank">https://communities.win/</a> and sign up for a new account.</li>
        <li>Use a separate account specifically for bot activity — this is recommended to avoid any issues with your main account.</li>
        <li>After signing up, open the Python script (likely named <code>main.py</code> or <code>downvoter.py</code>) in a text editor.</li>
        <li>Locate the following lines and replace them with your actual credentials:
            <pre><code class="language-python">USERNAME = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'</code></pre>
        </li>
    </ol>
    <p><strong>Optional but Recommended:</strong> Add your <a href="https://docs.scored.co/" target="_blank">Scored.co API key</a> to the script if you want improved access to site functionality or plan to scale usage.</p>
    <h2>Usage</h2>
    <p>To run the script on a specific communities.win subreddit (with downvoting enabled), modify the <code>URL</code> variable in the Python script before execution. For example, to target the <code>/c/funny/new</code> subreddit:</p>
    <ol>
        <li>Open the Python script in a text editor.</li>
        <li>Locate the <code>URL</code> variable:
            <pre><code class="language-python">URL = "https://communities.win/c/funny/new"</code></pre>
        </li>
        <li>Change the URL to the desired communities.win subreddit.</li>
        <li>Execute the script from your terminal:
            <pre><code>python your_script_name.py</code></pre>
        </li>
    </ol>
    <p>Replace <code>your_script_name.py</code> with the actual name of the Python file.</p>
    <h2>Description of the Code</h2>
    <p>The Python script performs the following actions:</p>
    <ol>
        <li>Imports necessary libraries from Selenium for browser automation, logging for status updates, and time for delays.</li>
        <li>Defines variables for your username, password, the target URL, and CSS selectors for various elements on the page (login button, username/password fields, submit button, and downvote buttons).</li>
        <li>Configures basic logging to display information and potential errors during the script execution.</li>
        <li>Sets up Chrome browser options, including maximizing the window, disabling extensions and GPU, running in a sandbox, and setting a user agent.</li>
        <li>Initializes a Chrome WebDriver using <code>webdriver-manager</code> to automatically handle ChromeDriver installation.</li>
        <li>Creates a <code>WebDriverWait</code> instance to wait for specific elements to become interactable.</li>
        <li>Opens the specified URL in the Chrome browser.</li>
        <li>Locates and clicks the login button.</li>
        <li>Finds the username and password input fields, enters your provided credentials, and clicks the submit button.</li>
        <li>Pauses for a few seconds to allow the login process to complete.</li>
        <li>Locates all the downvote buttons on the page using their CSS selector.</li>
        <li>Iterates through the found downvote buttons and attempts to click each one, with a small delay between clicks. Any errors during the click are logged as warnings.</li>
        <li>Includes error handling to catch and log any exceptions that occur during the process.</li>
        <li>Finally, closes the browser window.</li>
    </ol>
    <h2>Disclaimer</h2>
    <p>Use this script responsibly and ethically. Automating interactions on websites may violate their terms of service. The author is not responsible for any consequences resulting from the use of this script.</p>
    <h2>License</h2>
    <p>This project is licensed under the <a href="https://www.gnu.org/licenses/gpl-3.0.en.html" target="_blank">GNU General Public License v3.0</a>.</p>
</body>
</html>
