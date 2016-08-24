#CS496  

##Dennis Tat  

Live page: [cs496-1373.appspot.com/](http://cs496-1373.appspot.com/)  

Mobile-optimized front-end: [cs496-1373.appspot.com/appIndex/](http://cs496-1373.appspot.com/appIndex)  

Explore the API: [cs496-1373.appspot.com/_ah/api/explorer](https://cs496-1373.appspot.com/_ah/api/explorer)  
	Click Services. Select mylibrary API v1 CS496. Select desired function. Input appropriate parameters. Click Execute without OAuth.  

This application is backed by Google Cloud Datastore NDB. The non-relational database contains two entities: items and locations. Items and locations have a 1-to-many relationship -- many items can be stored at one location.  

The main page can view, edit, and delete all items and locations. The mobile front-end includes support for user accounts. Locations are shared across all accounts, but items can only be viewed, edited, or deleted when associated with a specific account.  

The mobile front-end uses an API created with the Endpoints Proto Datastore API. The mobile front-end uses the API to interact with the non-relational database.  

