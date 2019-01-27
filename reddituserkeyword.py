import pprint, os
import praw

def main():
    reddit = praw.Reddit(client_id='Your client ID',
                     client_secret='Your client secret',
                     user_agent=' /u/Your username, https://github.com/Fitzy1293/reddituserkeyword')               
    
     
    userstr = input('Enter a username:\n')
    user = reddit.redditor(userstr)
    
    comments = userComments(user)
    
    keyword = input('Enter a keyword:\n')

    for comment in comments:
        for word in comment[1]:
            if keyword.lower() + 's' == word.lower() + 's':
                print(comment[0])
                print(' '.join(comment[1]))
                print()
        
def userComments(user):
    userComments = []
    for comment in user.comments.new(limit=None):
        link = 'https:/www.reddit.com' + str(comment.permalink)

        comment = str(comment.body.encode('utf-8'))
        comment = comment.lstrip('\"b')
        comment = comment.lstrip('\'b')
        comment = comment.rstrip('\"')
        comment = comment.rstrip('\'')
        comment = comment.rstrip('\n"')
        comment = '\n\n'.join(comment.split('\\n\\n'))
        comment = '\''.join(comment.split('\\\''))
        comment = comment.split(' ')

        commentInfo = (link, comment)
        
        userComments.append(commentInfo)
    return userComments
main()