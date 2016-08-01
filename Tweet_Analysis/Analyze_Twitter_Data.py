import matplotlib.pyplot as plt
import operator
from Tweet_Analysis import TweetAnalysis


"""Plots Word Counts of each candidate on bar graph
@param top_15_words
    Ordered Dictionary of top 15 words and word counts used by candidate
@param author
    Twitter Name of candidate"""
def plotWordCounts(top_15_words, author):
    words = []
    word_counts = []
    for word, word_count in top_15_words:
        words.append(word)
        word_counts.append(word_count)
    plt.bar(range(len(word_counts)), word_counts, align='center')
    plt.xticks(range(len(words)), words)
    plt.show()


"""Takes the top 15 words and corresponding word counts from @code word_freq.
@param word_freq
    dictionary of words and word counts for a candidate
@return top_15_words
    ordered dictionary of top 15 words for candidate"""
def getTop15Words(word_freq):
    word_freq = sorted(word_freq.items(), key=operator.itemgetter(1))
    top_15_words = word_freq[len(word_freq)-15:]
    return top_15_words


"""Gets the top 15 words used by each candidates and then plots word count data.
@param candidates_word_maps
    JSON object containing words and word counts for each candidate"""
def processResults(candidates_word_maps):
    for author, word_freq in candidates_word_maps.items():
        top_15_words = getTop15Words(word_freq)
        plotWordCounts(top_15_words, author)


"""Main Method"""
def main():
    test = TweetAnalysis()
    test.setFilePath('/home/dragon/Programs/TwitterApp/Twitter_Political_Analysis/candidate_tweets.txt')
    test.createTweetLists()
    test.detTweetFrequencies()
    print test.getTweetFrequencies()
    test.detWordFrequencies()
    candidates_word_maps = test.getWordFrequencies()
    processResults(candidates_word_maps)


if __name__ == '__main__':
    main()