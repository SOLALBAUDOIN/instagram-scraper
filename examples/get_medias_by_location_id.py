from igramscraper.instagram import Instagram

instagram = Instagram()
instagram.with_credentials('username', 'password', 'path/to/cache/folder')
instagram.login()

medias = instagram.get_medias_by_location_id('1', 20)
media = medias[0]
print(media)
print('Account info:')
account = media.owner
print('Id', account.identifier)
# print('Username', account.username)
# print('Full Name', account.full_name)
# print('Profile Pic Url', account.get_profile_picture_url_hd())