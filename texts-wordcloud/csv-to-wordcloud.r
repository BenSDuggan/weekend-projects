# Create a wordcloud image from messages in a CSV

#install.packages("wordcloud2")
library(wordcloud2) 
library(webshot)
webshot::install_phantomjs()
library("htmlwidgets")

remove_words <- c("and", "whether", "or", "but", "either", "neither", "nor", "just", "so", "the", "as", "if", "then", "rather", "than", "such", "that", "it", "a", "with", "to", "too", "to", "didn't", "this", "it's", "didn't", "be", "is", "of", "in", "wasn't", "he's", "she","her", "im", "for", "on", "them", "his", "at", "was", "dose", "off", "did", "him", "it’s", "they", "have", "has", "he", "an", "are", "also", "though", "which", "having", "thought", "get", "got", "were", "went", "i", "you", "me", "it?", "dad", "do", "i’m", "mom", "that’s", "my", "she's")


messages <- read.csv("messages.csv")

words <- c()
for(i in 1:nrow(messages)) {
  words <- c(words, unlist(strsplit(messages$text[i], " ")))
}

words.bk <- words

# Remove empty characters
words <- unname(sapply(words, FUN=function(x) trimws(x, which = c("both", "left", "right"), whitespace = "[ \t\r\n]")))

words <- tolower(words)

words <- words[which(words != "")]

# Remove uninteresting words
words <- words[which(!(words %in% remove_words))]

counts <- table(words)

words_count <- data.frame(word=names(counts), freq=unname(counts))
words_count <- words_count[, c(1,3)]
names(words_count) <- c("text", "freq")

words_count <- words_count[order(words_count$freq, decreasing=TRUE), ]
row.names(words_count) <- 1:nrow(words_count)

wordcloud2(data=words_count, size=.8, color='random-dark', backgroundColor="#eee", shuffle=FALSE, minRotation = -pi/2, maxRotation = pi/2, ellipticity = 2)


option <- wordcloud2(data=words_count, size=.8, color='random-dark', backgroundColor="#eee", shuffle=FALSE, minRotation = -pi/2, maxRotation = pi/2, ellipticity = .65, shape="circle")





saveWidget(option,"output/option.html",selfcontained = F)
# and in png
webshot("output/option.html","output/option_5.png", delay = 5, vwidth = 1000, vheight=800) # changed to png.


