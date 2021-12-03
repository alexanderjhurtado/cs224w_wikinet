# cs224w_final
https://github.com/jbcdnr/gretel-path-extrapolation

# cs224w_final
Node features: \
= from Jean-Baptiste paper: \
- node's in & out degrees \
= our ideas: \
 	- multi-hot vector representing categories of articles \
 		^[IDEA: given the hierarchichal nature of the category data, maybe we have a multi-hot vector for each level of category] \
 	- aggregate word embeddings for most important words in articles \
 		^[REACH: leave for future work] \

Edge features: \
 = from Jean-Baptiste paper: \
 	- TF-IDF similarity from source to destination articles \
 	- number of times a source->destination link was followed as a path (in training dataset) \
 		^ [Alex: we could probably do a log likelihood instead] \
