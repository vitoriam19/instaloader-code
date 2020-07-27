#>>> pip install instaloader
import instaloader

if __name__ == '__main__':

	# >> To see the attributes of each class and have more information: https://instaloader.github.io/as-module.html
	loader = instaloader.Instaloader()

	# The interactive_login receives username as a parameter, necessary for some processes and for the collection of private profiles.
	# The password must be filled in at the terminal.

	loader.interactive_login('--user--')

	# Collection of profile information
	'''
	username = "--user--"
	profile = instaloader.Profile.from_username(loader.context, username)
	user_id = profile.userid
	full_name = profile.full_name
	print('Name: ' + str(full_name) + '  --  ID: ' + str(user_id))
	print('Private? ' + str(profile.is_private))
	print('\n')
	'''

	#Download User Profile Image
	'''
	loader.download_profilepic(profile)
	'''

	# Collect highlights from a profile
	# >> You must be logged into Instagram
	'''
	for highlight in loader.get_highlights(profile):
		for item in highlight.get_items():
			loader.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))
	'''

	# Collect posts from a profile
	# >> You must follow the private profile to collect this information
	'''
	posts = profile.get_posts()

	# With a post you can collect comments and with a comment, his replies
	
	counter = 1
	for post in posts:
	
		print('Post ' + str(counter))
		loader.download_post(post, username)
		print(post.caption)
		print(post.owner_profile)
		print('Data de postagem: ' + str(post.date_local))
		print('tagged users: '+str(post.tagged_users))
		
		comments = post.get_comments()

		for comment in comments:
			print(comment.text)
			replies = comment.answers

			for reply in replies:
				pass

		print('\n')
		counter += 1
    '''

	# Profile network collection
	# >> You must be logged into Instagram
	'''
	loader.login("user","password")
	followers = profile.get_followers()
	followees = seed_user_profile.get_followees()

	for follower in followers:
		pass
	'''

	# Collection of stories from a profile
	# >> You must be logged into Instagram
	'''
	loader.download_stories(userids=[profile.userid], filename_target='{}'.format(profile.username), fast_update=True)
	'''

	# Collects information from a hashtag
	'''
	tag = "--name_of_hashtag--"
	hashtag = instaloader.Hashtag.from_name(loader.context, tag)
	tag_id = hashtag.hashtagid
	print('Hashtag: #' + str(hashtag.name) + '  --  ID: ' + str(tag_id))
	print('Posts count: ' + str(hashtag.mediacount))
	print('\n')
	#Download the posts associated with the hashtag
	for post in hashtag.get_posts():
		loader.download_post(post, target="#"+hashtag.name)
	'''
