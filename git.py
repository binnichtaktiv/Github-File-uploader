from github import Github

token = 'your_personal_token'

repo_path = 'user/repo'

file_path = 'file_path'

file_label = 'filename_in_release'

g = Github(token)

repo = g.get_repo(repo_path)

release = repo.create_git_release(tag='v1.0', name='Release v1.0', message='Release v1.0')

asset = release.upload_asset(file_path, label=file_label)

download_url = asset.browser_download_url

print(f'Direct-Download-Link: {download_url}')
