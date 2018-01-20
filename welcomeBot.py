from steem import Steem
from steem.blockchain import Blockchain
from steem.post import Post

#create steem instance and pass it your private posting key
s = Steem(keys = ["<your private posting key>"])
#create blockchain instance
b = Blockchain()

# Define your tag or multiple ones
keywords = ["introduceyourself", "adventure"]

# Define your username
steemuser = <your steem user account>
# Do you want to vote on post too? Fill out user & voting weight (power).
voting = 1
power = 100




while True:
    try:
        # stream the blockchain
        stream = map(Post, b.stream(filter_by=['comment']))
        # go through all the posts in the block
        for post in stream:
            # get all the tags of the post
            postTags = post.json_metadata.get('tags', [])
            # check if one of predefined tags is in the list of tags. You can add more tags
            if keywords in postTags:
                title = post.title
                # check if the post/comment has a title
                if title == "":
                    #title is empty so it's most likely a comment
                    pass

                else:
                    #We have a title so it's a fresh posts so let's welcome them
                    post.reply("Welcome to Steemit {post['author']}!", "", "Yours @steemuser")
                    print("... welcomed user ")
                    
                        #When voting is activated we vote on that post too
                        if voting == "1":
                        post.upvote(weight=upvote_pct, voter=steemuser)
                        print("... & voted on post.")
                        
                        else:
                            #When not - we skip voting
                            pass
                        
            else:
                #no introduceyourself tag so skip the post
                pass

    #Catch any unexpected exceptions
    except Exception as e:
        print("... NOT welcomed because:")
        print("Error: "+str(e))
        continue
