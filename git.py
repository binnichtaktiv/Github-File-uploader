from github import Github
from datetime import datetime

token = 'your_personal_token'

repo_path = 'user/repo'

file_path = input("Enter the filepath to your file that you want to upload:\n")

# get file name from file_path
file_name = file_path.split('/')[-1]

g = Github(token)

repo = g.get_repo(repo_path)

# get current time for the tag in release
release_tag = datetime.now().strftime("%H-%M-%S")

# release name with date and time
release_name = f'Release {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'

try:
    release = repo.create_git_release(tag=release_tag, name=release_name, message='', draft=False, prerelease=False)
    
    asset = release.upload_asset(file_path, label=file_name)
    
    # get ddl
    download_url = asset.browser_download_url
    
    print(f'Direct-Download-Link: {download_url}')
except Exception as e:
    print(f"Error creating release: {e}")
