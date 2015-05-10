# twitter.py

import Tweet, pickle



def main():

    tweet_file_name = "tweets.dat"
    tweets = load_tweets(tweet_file_name)
    
    while (True):
        print_menu()
        choice = get_menu_choice()

        # Make a Tweet
        if (choice == 1):
            create_tweet(tweets)
            save_tweets(tweet_file_name, tweets)
            
        # View Recent Tweets
        elif (choice == 2):
            view_recent_tweets(tweets, 5)
            
        # Search Tweets
        elif (choice == 3):
            search_tweets(tweets)
            
        # Exit
        else:
            print("\nThank you for using the Tweet Manager!")
            break



def load_tweets(tweet_file_name):
    try:
        # Attempt to open tweet_file_name
        tweet_file = open(tweet_file_name, "rb")
        tweets = pickle.load(tweet_file)
        tweet_file.close()
    except:
        # If tweet_file_name cannot be loaded, start with an empty list
        tweets = []

    # Return Tweet list
    return tweets



def save_tweets(tweet_file_name, tweets):
    try:
        # Attempt to save the Tweet list
        output_file = open(tweet_file_name, "wb")
        pickle.dump(tweets, output_file)
        output_file.close()
    except:
        print("Error: The Tweets could not be saved.")



def print_menu():
    # Print the Tweet Menu
    print("\nTweet Menu")
    print("----------")
    print("1. Make a Tweet")
    print("2. View Recent Tweets")
    print("3. Search Tweets")
    print("4. Quit")



def get_menu_choice():
    # Prompt for a choice and validate it
    while (True):
        try:
            choice = int(input("\nWhat would you like to do? "))
            if (choice < 1 or choice > 4):
                print("Please select a valid option.")
                continue
        except:
            print("Please enter a numeric value.")
        else:
            break

    return choice



def create_tweet(tweets):
    # Ask for the user's name
    name = input("\nWhat is your name? ")
    
    while (True):
        # Ask for the user's message
        text = input("What would you like to tweet? ")

        # If the tweet is too long, display an error and ask again
        if (len(text) > 140):
            print("\nTweets can only be 140 characters!\n")
        else:
            # ...otherwise, the tweet is <140 characters, so stop looping
            break

    # Create a Tweet object using the user's name and message
    tweet = Tweet.Tweet(name, text)

    # Add the Tweet to the tweets list
    tweets.append(tweet)

    # Print a confirmation that the Tweet has been made
    print(name, ", your tweet has been saved.", sep="")



def view_recent_tweets(tweets, count):
    print("\nRecent Tweets")
    print("-------------")

    # Check if there are any Tweets
    if (len(tweets) < 1):
        print("There are no recent tweets.")
    else:
        # If there are Tweets, get the five most recent and reverse their order
        reordered_last_five_tweets = reversed(tweets[-5:])

        # Loop through and print the recent Tweets
        for tweet in reordered_last_five_tweets:
            print_tweet(tweet)



def search_tweets(tweets):
    # Check if there are any Tweets
    if (len(tweets) < 1):
        print("\nThere are no tweets to search.")
    else:
        # Ask the user for a search term
        search_term = input("\nWhat would you like to search for? ")

        print("\nSearch Results")
        print("--------------")

        # Reorder the Tweets to show the most recent first
        reordered_tweets = reversed(tweets)
        found_term = False

        # Loop through the Tweets
        for tweet in reordered_tweets:
            # Look for the search term in each Tweet's text
            if (search_term in tweet.get_text()):
                print_tweet(tweet)
                found_term = True

        if (not found_term):
            print("No tweets contained", search_term)



def print_tweet(tweet):
    print(tweet.get_author(), "-", tweet.get_age())
    print("", tweet.get_text(), "\n")
    


# Call main
main()
