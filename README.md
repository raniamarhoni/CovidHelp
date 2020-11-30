# Covid Help UK 
This website is used to connect people who need help during the pandemic to those who are willing to help. 

People and businesses can write posts on how they can help in there local area and people who need help can see what help is offered in their local community or write a post on what help they need 

## UX

### Surface 
#### Colour Scheme 
I wanted to use a simple colour scheme which is white, black and grey(#858585). Which are the only 3 colours used on the project.

#### Consistent design 
As the website uses multiple forms I wanted to keep the design the same for all of them. This is done by setting all the classes the same on CSS so they can only be changed in 1 place for the design to stay the same.

#### Typography 
I wanted to have the same font everywhere except the title so it can stand out. I picked the fonts from google fonts "Acme" for the title and sans-serif for the rest of the project 

#### Images
The only picture used on the project, which is on every page, is a hand shake. I used this as i think this represent a helping hand which is what the site is about. 

#### Design 
I wanted the project to have a simple design which would be easy to navigate which I've done as everything can be done through the navigation on the top which is fixed so the user will always see it and navigate to any page they can. 


### Skeleton

#### Wireframes
I created mock ups on adobe XD, Each page was created for 3 screens mobile, tablet and webpage.

* [Home Wireframe](https://e909c6aa-ce98-4438-9132-5f085b935b19.ws-eu01.gitpod.io/files/download/?id=5aae8f3a-e277-4dc7-b766-cd9e67def832)
* [All Posts Wireframe](https://e909c6aa-ce98-4438-9132-5f085b935b19.ws-eu01.gitpod.io/files/download/?id=6f14b072-4e26-40bb-8960-7e95f1c5ba3b)
* [View Post Wireframe](https://e909c6aa-ce98-4438-9132-5f085b935b19.ws-eu01.gitpod.io/files/download/?id=2f08bcdb-8c2e-4dfd-8a61-79a90caccce6)
* [Register Wireframe](https://e909c6aa-ce98-4438-9132-5f085b935b19.ws-eu01.gitpod.io/files/download/?id=7f9c63f5-1e7d-4793-8436-d6f4d83ef5e5)
* [Log In Wireframe](https://e909c6aa-ce98-4438-9132-5f085b935b19.ws-eu01.gitpod.io/files/download/?id=04d71d4e-e566-4e10-a666-0a3a0f2390dd)
* [Profile Wireframe](https://e909c6aa-ce98-4438-9132-5f085b935b19.ws-eu01.gitpod.io/files/download/?id=032c9ee0-8274-48b7-bde9-c2a826d51eac)
* [Manage Posts Wireframe](https://e909c6aa-ce98-4438-9132-5f085b935b19.ws-eu01.gitpod.io/files/download/?id=1d69faa8-4d3a-4916-ad18-b39fca3bc2d0)
* [Add a Post Wireframe](https://e909c6aa-ce98-4438-9132-5f085b935b19.ws-eu01.gitpod.io/files/download/?id=28d53385-acc0-46f4-a9cb-93082c2e261e)
* [Edit Post Wireframe](https://e909c6aa-ce98-4438-9132-5f085b935b19.ws-eu01.gitpod.io/files/download/?id=9c7d1eb0-9d56-4d83-843f-520dd9340e2e)

### Structure

#### MongoDB Database
This project uses MongoDB to store the data. 1 database is created with 2 collections, posts and users. 

Each User will need to have a unique username and email. They will need to specify if the user is a personal account or a business account and have a password which will be protected using  werkzeug.security to generate a password hash so the password will never be known by me and admin either and check password hash to make sure we can check the password is correct without seeing it either. 

Photo of mongodb user collection here 

Each Post will need to specify if they are offering or finding help which will help to filter it when people are searching up the post. Location will be entered to help sort it to whoever is searching up posts to the ones closest to them. Username so we can get the email off them and title and description so people can know what the post is about. Last of all when it was posted so that users can sort it the most recent if they wish. 

Photo of mongodb posts collection here 

#### Structure of the front-end development 
The structure is done so all the pages needed can easily be found in the navbar. Also the navbar will change depending on if there logged in so people don't go on pages they shouldn't if there not logged in. 


### Scope 

#### Sorting and filtering posts 
To make the website as easy as possible users can sort the posts from location to most recent adding filters on what kind of posts they are looking for. This helps the user find posts a lot easier and not have to scroll through posts wasting time 

#### Managing Posts 
Users can edit posts and delete posts whenever they wish to avoid people contacting them if they don't need help or are helping anymore. They can edit if they forgot to mention something or want to add more information. 

### Strategy 
This projects aim is to connect with people from your local community. People who are looking for help e.g. People who have to self-isolate, shield during this time to people who are willing to help during this time. 

#### People who are willing to help 
They can go through posts people have posted asking for help and respond. Also they can put up a post up allowing people to contact them on ways they can help. 

#### People who need help 
They can search up posts people have posted on ways they can help and respond asking for help or put up a post where people can contact them.

## Features
 
### Existing Features

### Sort and Filter Database 


### Features Left to Implement

## Technologies Used

* HTML5
* CSS3
* Bootstrap4 
* JavaScript
* jQuery
* Python
* MongoDB


## Testing

### Bugs Fixed 

#### Collection name saved different 
When adding or editing a post I realised it wasn't showing up on the manage tasks page but would add or edit in the mongodb database. I noticed when adding a post it was saving the user under username instead of user which would add to the database but wouldn't show up on the users manage posts. Therefore it was changed to user 
I then changed it all back to username to avoid confusion

#### Anyone can add a post even if they didnt have an account  
I realised anyone was able to add a post if they typed it into the url therefor i changed it so you can only add a post if you are logged in 

#### Anyone can edit the post if they had the post_id 
I realised that if someone had the post_id they would be able to edit the post even through they are not logged in i changed this so you can only access that page if you are logged in 

#### Post wasn't updating
When updating a post not everything was getting updated as it wasn't being on the list to get updated 


### Validators

I've used a validator for very language used 
* [Python Validator](http://pep8online.com/)

## Deployment

How I deployed the site 
	
1. As I was going to use Gitpod I used this [template](https://github.com/Code-Institute-Org/gitpod-full-template) to open a GitHub repository 
2. To set up on Heroku you need to have a requirement.txt which will tell the application which applications and dependencies are required to run the app. You would also need a Procfile to know which file runs the app
3. Once I set up the requirement.txt and profile I went onto Heroku and set up a new app and selected the region closest to me 
4. I then connected my Heroku to GitHub so it can automatically deploy when deploying to GitHub.  
5. I did this by going onto the Heroku app and under the tab deploy I selected GitHub 
6. I then went onto automatic deploys and added in my repository
7. Before I clicked enable automatic deploys go onto settings and click on Reveal Config Vars. Once selected I added in the IP, Port, Secret key, Mongo URI, and Mongo Database 
8. I went back to Gitpod and committed and push all the new files requirement.txt and profile to Github. 
9. Then I went back to Heroku and selected Enable Automatic Deploys which will then build the app. 
 
## Credits

### Content
### Media

Photo of shaking hands was taken from pexels see [Link to photo](https://www.pexels.com/photo/monochrome-photo-of-couple-holding-hands-1004014/)

### Acknowledgements
