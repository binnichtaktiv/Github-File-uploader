from github import Github
from datetime import datetime

token = 'your_personal_token'

repo_path = 'user/repo'

file_path = 'file_path'

file_name = file_path.split('/')[-1]

g = Github(token)

repo = g.get_repo(repo_path)

release_tag = datetime.now().strftime("%H-%M-%S")

release_name = f'Release {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'

try:
    release = repo.create_git_release(tag=release_tag, name=release_name, message='', draft=False, prerelease=False)
    
    asset = release.upload_asset(file_path, label=file_name)
    
    download_url = asset.browser_download_url
    
    print(f'Direct-Download-Link: {download_url}')
except Exception as e:
    print(f"Error creating release: {e}")

