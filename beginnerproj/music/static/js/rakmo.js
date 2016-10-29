  //Initialize the plugin
   $('body').ttwMusicPlayer(myPlaylist, {options});

   //You can specify the following options in the options object:
   {
        currencySymbol:'$',
        buyText:'BUY',
        tracksToShow:5,
        autoplay:false,
        ratingCallback:function(index, playlistItem, rating){
                //some logic to process the rating, perhaps through an ajax call
        }
   }
