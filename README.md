# GitHub Release File Uploader 📦

This script facilitates easy uploading of files to the releases in your private GitHub repository.

## Usage ✨

1. **Configuration:**
    - Replace `your_personal_token` with your personal access token.
    - Replace `user/repo` with the path to your private repository.
    - Modify `file_path` to the path of the file to be uploaded.
    - Change `file_label` to the name you want to give to the file in the release.

2. **Installation:**
    - Make sure you have Python installed.
    - Install the required libraries using `pip install PyGithub`.

3. **Execution:**
    - Run the script by typing `python3 git.py` in your command line.

## Note 🔑

Don't forget to check out the [GitHub documentation](https://docs.github.com/rest/reference/repos#releases) for more information on using the GitHub API.

### Creating a Personal Access Token for GitHub

1. **Navigate to GitHub Settings:**
    - Log in to your GitHub account and click on your profile icon in the top-right corner of the page.
    - From the dropdown menu, select "Settings".

2. **Access Developer Settings:**
    - In the left sidebar of the Settings page, scroll down and click on "Developer settings".

3. **Generate a New Token:**
    - In the Developer settings page, click on "Personal access tokens".
    - Then, click on the "Generate new token" button.

4. **Provide Token Description:**
    - Enter a descriptive name for your token in the "Note" field. This will help you identify the purpose of the token later on.

5. **Select Scopes:**
    - GitHub provides a variety of scopes that control the access level of the token. For this script, you'll need at least the "repo" scope, which grants full control of private repositories.
    - Check the box next to "repo" to select this scope.

6. **Generate Token:**
    - After selecting the appropriate scopes, scroll down and click on the "Generate token" button.
    - GitHub will generate a new personal access token for you.

7. **Copy the Token:**
    - Once the token is generated, GitHub will display it on the screen. Make sure to copy this token immediately.
    - Note: GitHub only shows the token once for security reasons. If you lose it, you'll need to generate a new token.

8. **Use the Token:**
    - In your script or application, replace `'your_personal_token'` with the token you just generated.

9. **Security Precautions:**
    - Treat your personal access token like a password. Keep it secure and do not share it publicly.
    - If you suspect that your token has been compromised, you can revoke it in the "Personal access tokens" section of your GitHub account settings.
