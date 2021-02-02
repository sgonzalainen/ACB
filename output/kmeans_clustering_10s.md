# ACB Players Clustering (10s decade) by PCA + KMeans

 <div style="text-align:center"><img src="../img/banner_10s.jpg" /></div>


 ## Introduction

 The scope of this project is to classify ACB Basketball players of the 10s into different groups purely based their game stats and see how they cluster each other.

 ## Data Source

 The game stats of each player per season were scraped from the [ACB](http://www.acb.com/) official website.

 ## Features

 Player stats were redefined by a 20-min played unit since the purpose is to compare players regardless of how many minutes or games they played.

 Seasonal records with less than 5 minutes avg. or 10 games played were considered irrelevant and discarded.

 17 features were used: 

 * `points`: total points scored
 * `3p_try`: 3-point shots tried
 * `3p_perc`: 3-point shots conversion percentage 
 * `2p_try`: 2-point shots tried
 * `2p_perc`: 2-point shots conversion percentage
 * `free_try`: free-throws tried
 * `free_perc`: free-throws conversion percentage
 * `reb_def`: defensive rebounds
 * `reb_att`: attacking rebounds
 * `reb_tot`: total rebounds
 * `assis`: assists
 * `steals`: steals
 * `turnovers`: turnovers
 * `block_fav`: given blocks 
 * `block_con`: received blocks
 * `dunks`: dunks
 * `foults_rec`: received foults

The feature `commited foults` was discarded since it produced a lot of impact when clustering and from my point of view, it does not tell much whether a player has 2 foults or 3 foults on average and also in many last-minute situations, foults are forced on purpose by players.

## PCA for dimensionality reduction

Ok, so those 17 parameters features the players, but before applying clustering by Kmeans algorithm, a PCA pre-step is performed in order to mititage the [curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality).

But how many PCs? Let's keep the PCs that can attain at least the 80% of the variance. In this case was the first 6.

 <div style="text-align:center"><img src="../img/variance.jpg", height = 200px /></div>

 <div style="text-align:center"><img src="../img/vari.png",  /></div>

The 1st PC retains 37% of total variance, the 2nd PC retains the 17%...

Let's see the Eigen vector of each PC and try to get insights of it.

 <div style="text-align:center"><img src="../img/eigenvectors.png",  /></div>


And this is how I see them:

* **PC1**: Inside the Paint game
* **PC2**: Lack of contribution to the game
* **PC3**: Ball distribution and usage
* **PC4**: Bad choice shooter
* **PC5**: Steal capacity
* **PC6**: Penetration skill

Based on above, it seems the first quality to classify players is whether they usually play close or afar from basket.


## Kmeans Clustering

Ok, now in the new feature space, Kmeans clustering is applied. But again, how many number of cluster do we set?

By looking at the silhouette, distortion and calinski_harabasz scores, I finally ended up with **7** clusters.

<div style="text-align:center"><img src="../img/silhouette.jpg" height= 200  /></div>

<div style="text-align:center"><img src="../img/distortion.jpg" height= 200   /></div>

<div style="text-align:center"><img src="../img/calinski_harabasz.jpg" height= 200  /></div>























